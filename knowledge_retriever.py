from knowledge_provider import KnowledgeProvider
import utlity

class KnowledgeRetriever:

	knowledge_provider = None

	#a list which will contain the pre-processing words from the heading 
	words = []

	#a list which will contain all the headings from the document
	categories = []

	#a list which will contain the tuple of words list and their categories
	words_categories = []


	def __init__(self):
		self.knowledge_provider = KnowledgeProvider()
		self.initialized_data()

	def initialized_data(self):

		licensing_json = self.knowledge_provider.get_json_data()

		#a list which will contain the pre-processing words from the heading 
		words = []

		#a list which will contain all the headings from the document
		categories = []

		#a list which will contain the tuple of words list and their categories
		words_categories = []

		for intent in licensing_json['intents']:
    
		    heading_text = intent['Heading']
		    content_text = intent['Content']
		    
		    stem_heading_list = utility.pre_processing(heading_text)
		    #print(stem_heading_list)
		    stem_content_list = utility.pre_processing(content_text)
		    #print(stem_content_list)
		    
		    intent['Heading_Keywords'] = stem_heading_list
		    intent['Content_Keywords'] = stem_content_list
		    
		    self.words.extend(stem_heading_list)
		    
		    self.words_categories.append((stem_heading_list, intent['Heading']))
		    
		    if intent['Heading'] not in categories:
		        self.categories.append(intent['Heading'])


	def get_words(self):
		#removing duplication of words and storing a sorted list 
		return sorted(list(set(self.words)))

	def get_categories(self):
		#removing duplication of categories and storing a sorted list 
		return sorted(list(set(self.categories)))

	def get_word_categories(self):
		return self.words_categories




