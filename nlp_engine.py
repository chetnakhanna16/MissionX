#from file name with relative path import class name
from knowledge_provider import KnowledgeProvider
import logging
from model.ann_model import AnnModel
from model.lstm_model import LstmModel


class NlpEngine:

	knowledge_provider = None
	logger = None
	ann_model = None
	lstm_model = None
	licensing = None

	def __init__(self):
		#print("NlpEngine class initiated")
		# self.knowledge_provider = KnowledgeProvider()
		# self.logger = logging.getLogger()
		# self.logger.setLevel(logging.INFO)
		# self.logger.addHandler(logging.StreamHandler())
		# self.ann_model = AnnModel()
		self.lstm_model = LstmModel()
		# self.licensing = self.knowledge_provider.get_json_data()

	#function to get the processed answer using knowledge provider's JSON data 
	def get_response(self, question, algorithm):
		self.logger.info("Algorithm used: " + algorithm)	
		json_file = self.knowledge_provider.get_json_data() 
		# intents_list = json_data.get("intents")
		# return intents_list[0]

	#return bag of words array: 0 or 1 for words that exist in sentence
	def bag_of_words(self, question, words):
	    
	    #bag of words - vocabulary matrix
	    bow = [0]*len(words)  
	    
	    for s in question:
	        for i, word in enumerate(words):
	            if word == s: 
	                #assign 1 if current word of pre-processed question is in the vocabulary of words
	                bow[i] = 1
	                #print the word found
	                print ("Found in bag: %s" % word)
	                    
	    return(np.array(bow))


	#predict the response 
	def predict(self, question, algorithm):
	    
	    p = self.bag_of_words(question, words)
	    
	    if algorithm == "LSTM": 
	        #prediction probability for each word using LSTM
	        pred_prob = self.lstm_model.predict(np.array([p]))[0]
	        #print(pred_prob)
	    elif algorithm == "ANN":
	        #prediction probability for each word using LSTM
	        pred_prob = self.ann_model.predict(np.array([p]))[0]
	        #print(pred_prob)
	        
	    
	    pred_prob_list = [[i,r] for i,r in enumerate(pred_prob)]
	    #print(pred_prob_list)
	    
	    #sorting acoording to the probabilities (in descending order)
	    pred_prob_list.sort(key=lambda x: x[1], reverse=True)
	    #print(pred_prob_list)
	    
	    sorted_heading_prob = []
	    
	    for r in pred_prob_list:
	        sorted_heading_prob.append({"topic": categories[r[0]], "probability": str(r[1])})
	        
	    return sorted_heading_prob


	#get top 1 response for the question as it is predicted with the highest probability
	def get_response(self, question, algorithm, json_file=licensing):
	    
	    intents = self.predict(question, algorithm)
	    tag = intents[0]['topic']
	    #print(tag)
	    
	    list_of_intents = json_file['intents']
	    
	    for i in list_of_intents:
	        if(i['Heading']== tag):
	            result = ("Link: {} ".format(i['Link']), i['Content'])
	            break
	            
	    return result


#main function for the NLP task
if __name__ == "__main__":
	nlp_engine = NlpEngine()
	print(nlp_engine.get_response("What is a cluster?", "LSTM"))