from nlp_engine import NlpEngine
import json
import nltk
#nltk.download("punkt")
from nltk import RegexpTokenizer
#nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import logging
import utility


class QueryEngine:

	nlp_engine = None
	logger = None

	def __init__(self):
		#print("QueryEngine class initiated")
		self.nlp_engine = NlpEngine()
		self.logger = logging.getLogger()
		self.logger.setLevel(logging.INFO)
		self.logger.addHandler(logging.StreamHandler())

	def get_answer(self, question):
		question_word_list = utility.pre_processing(question)
		return self.nlp_engine.get_response(question_word_list, "ANN")

#main function for the pre-processing task
if __name__ == "__main__":
	query_engine = QueryEngine()
	query_engine.logger.info("\n")
	print(query_engine.get_answer("What are the requirements to license a cluster?"))



