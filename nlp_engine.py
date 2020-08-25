#from file name with relative path import class name
from knowledge_provider import KnowledgeProvider
import logging
from model.ann import AnnModel
from model.lstm import LstmModel
from knowledge_retriever import KnowledgeRetriever
import numpy as np

class NlpEngine:

	knowledge_provider = None
	logger = None
	ann = None
	lstm = None
	licensing = None
	know_retriever = None
	json_file = None

	def __init__(self):
		#print("NlpEngine class initiated")
		self.knowledge_provider = KnowledgeProvider()
		self.logger = logging.getLogger()
		self.logger.setLevel(logging.INFO)
		self.logger.addHandler(logging.StreamHandler())
		self.ann = AnnModel()
		self.lstm = LstmModel()
		self.licensing = self.knowledge_provider.get_json_data()
		self.know_retriever = KnowledgeRetriever()
		self.json_file = self.knowledge_provider.get_json_data() 

	#return bag of words array: 0 or 1 for words that exist in sentence
	def bag_of_words(self, question_word_list, words):
		
		#bag of words - vocabulary matrix
		bow = [0]*len(words)  
		
		for s in question_word_list:
			for i, word in enumerate(words):
				if word == s: 
					#assign 1 if current word of pre-processed question is in the vocabulary of words
					bow[i] = 1
					#print the word found
					#print ("Found in bag: %s" % word)
							
		return(np.array(bow))


	#predict the response 
	def predict(self, question_word_list, algorithm):
		
		p = self.bag_of_words(question_word_list, self.know_retriever.words)
		
		if algorithm == "LSTM": 
			#prediction probability for each word using LSTM
			pred_prob = self.lstm.model.predict(np.array([p]))[0]
			#print(pred_prob)
		elif algorithm == "ANN":
			#prediction probability for each word using LSTM
			pred_prob = self.ann.model.predict(np.array([p]))[0]
			
		threshold = 0.3
		pred_prob_list = [[i,r] for i,r in enumerate(pred_prob) if r > threshold]
		#print(pred_prob_list)
		
		#sorting acoording to the probabilities (in descending order)
		pred_prob_list.sort(key=lambda x: x[1], reverse=True)
		#print(pred_prob_list)
		
		sorted_heading_prob = []
		
		for r in pred_prob_list:
			sorted_heading_prob.append({"topic": self.know_retriever.categories[r[0]], "probability": str(r[1])})
			
		return sorted_heading_prob


	#get top 1 response for the question as it is predicted with the highest probability
	def get_response(self, question_word_list, algorithm):

		prediction = self.predict(question_word_list, algorithm)

		result = []

		if len(prediction) == 0:
			return []
		else:
			list_of_predictions = self.json_file['intents']

			for index in range(0,3):
				if len(prediction) < index + 1:
					break

				prediction_topic = prediction[index]['topic']

				#print(prediction)
				#print(prediction_topic)

				for pred in list_of_predictions:
					if(pred['Heading']== prediction_topic):
						#myDict = {}
						# myDict['Heading'] = pred['Heading']
						# myDict['Link'] = pred['Link']
						# myDict['Content'] = pred['Content']
						# result.append(myDict)
						result.append({"Heading": pred['Heading'], "Link" : pred['Link'], "Content": pred['Content']})
						continue
		
		return result

#main function for the NLP task
if __name__ == "__main__":
	nlp_engine = NlpEngine()
	print(nlp_engine.get_response(["product", "requir", "licens"], "ANN"))


