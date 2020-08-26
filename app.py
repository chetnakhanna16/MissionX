import os
import logging
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
from query_engine import QueryEngine
import utility 


# Initialize a Flask app to host the events adapter
app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(os.environ['SLACK_SIGNING_SECRET'], "/slack/events", app)


# Initialize a Web API client
slack_web_client = WebClient(token = os.environ['SLACK_BOT_TOKEN'])


# MESSAGE EVENTS
# When a user sends a direct message, the event type will be 'message'
# Linking the message callback to the 'message' event
@slack_events_adapter.on("message")


#message function to retrieve different elements from the message that was posted on Slack
def message(msg):

    #retrieve the event from the slack message
    event = msg.get("event", {})

    #retrieve the channel_id, user_id, text from the event
    channel_id = event.get("channel")
    user_id = event.get("user")

    #the text here also contains the bot's ID
    text = event.get("text")

    #retrieve the authorised user from the slack message
    authed_users = msg.get("authed_users", [])

    #retrieve the blocks from the event to access the user_id of the bot and text sent by the user
    blocks = event.get("blocks")

    thread_ts_id = event.get("thread_ts")
    #print("thread_ts_id: ", thread_ts_id)
    ts_id = event.get("ts")
    #print("ts_id: ", ts_id)

    if(thread_ts_id == None):
        thread_ts_id = ts_id

   #print(msg)

    if blocks != None:
        outer_elements = blocks[0].get("elements")
        inner_elements = outer_elements[0].get("elements")

        called_user = None
        called_text = None

        if len(inner_elements) > 1:
            called_user = inner_elements[0].get("user_id")
            called_text = inner_elements[1].get("text")

            #print(msg)

            #allowing the bot to answer only when called 
            if user_id not in authed_users and called_user in authed_users:
            
                #calling the query function to find answer for user's query
                processed_text = query_engine.get_answer(called_text)

                result_str = ""

                if len(processed_text) == 0:
                    result_str = "Please contact the customer support for assistance regarding the same."
                if len(processed_text) >= 1:
                    result_str = "<" + processed_text[0]["Link"] + "|" + processed_text[0]["Heading"] + ">\n"
                    result_str += utility.formatted_text(' '.join(processed_text[0]["Content"].split()[:100])) + "\n"
                if len(processed_text) >= 2:
                    result_str += "*Related article(s):*" + "\n"
                    result_str += "<" + processed_text[1]["Link"] + "|" + processed_text[1]["Heading"] + ">\n"
                if len(processed_text) >= 3:
                    result_str += "<" + processed_text[2]["Link"] + "|" + processed_text[2]["Heading"] + ">\n"  
                #print(result_str)

                #posting the message to the slack channel
                slack_web_client.chat_postMessage(channel=channel_id, text=result_str, thread_ts=thread_ts_id)


#main function for the app
if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    query_engine = QueryEngine()

    app.run(port=3000)    