from knowledge_provider import KnowledgeProvider
import utility


#class to retrieve the words and categories list
class KnowledgeRetriever:

	knowledge_provider = None

	#list which will contain the pre-processing words from the heading 
	words = []

	#list which will contain all the headings from the document
	categories = []

	#list which will contain the tuple of words list and their categories
	words_categories = []


	def __init__(self):
		#print("Knowlege Retriever class is initialized.")
		self.knowledge_provider = KnowledgeProvider()
		self.words, self.categories, self.words_categories = self.initialized_data()

	
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
		    
		    words.extend(stem_heading_list)
		    
		    words_categories.append((stem_heading_list, intent['Heading']))
		    
		    if intent['Heading'] not in categories:
		        categories.append(intent['Heading'])

		words = sorted(list(set(words)))

		categories = sorted(list(set(categories)))

		return (words, categories, words_categories)


if __name__ == "__main__":
	#print("NLP Engine main function is executing.")
	knowledge_retriever = KnowledgeRetriever()
	print(knowledge_retriever.words)
