import json

class KnowledgeProvider:

	JSON_FILE_PATH = "./Licensing_Key.json"

	#function to retrieve the JSON data from the licensing data
	def getJsonData(self):
		with open(self.JSON_FILE_PATH, 'r') as doc:
			return json.load(doc)

#main function for the knowledge provider 
if __name__ == "__main__":
	knowledge_provider = KnowledgeProvider()
	print(knowledge_provider.get_json_data())