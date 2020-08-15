#from nlp_engine import NlpEngine
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
		#self.nlp_engine = NlpEngine()

		self.logger = logging.getLogger()
		self.logger.setLevel(logging.INFO)
		self.logger.addHandler(logging.StreamHandler())


#main function for the pre-processing task
if __name__ == "__main__":
	query_engine = QueryEngine()
	query_engine.logger.info("\n")
	print(utility.pre_processing("I have a Nutanix account and my enterprise wants to license a cluster. Is it possible to license a Prism cluster with my account?"))


