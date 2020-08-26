import json
import nltk
#nltk.download("punkt")
from nltk import RegexpTokenizer
#nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


#function to remove stop words
def remove_stop_words(myList):
    #setting stop words to English
    stop_words = set(stopwords.words("english"))
    
    newList = []
    
    for words in myList:
        if words not in stop_words:
            newList.append(words)

    return newList


#function to convert words to their stem
def word_stemming(myList):
    ps = PorterStemmer()
    
    newList = []
    
    for words in myList:
        stemmed_word = ps.stem(words)
        newList.append(stemmed_word) 

    return newList


#function to pre-process the question to be used in the algorithms
def pre_processing(text):

    text_lowercase = text.lower()
    tokenizer = RegexpTokenizer(r"\w+")
    tokenize_words = tokenizer.tokenize(text_lowercase)
    refined_list = remove_stop_words(tokenize_words)
    stem_list = word_stemming(refined_list)

    return stem_list


#function to create training data
def training_data(categories, words_categories):

	#a list which will store the training data (X and y)
	training_data = []

	#An array of zeroes to store the output which has length same as the length of categories
	output = [0] * len(categories)

	for i in words_categories:
	    bag_of_words = []
	    word_patterns = i[0]
	    
	    for j in words:
	        if j in word_patterns:
	            bag_of_words.append(1) 
	        else:
	            bag_of_words.append(0)
	            
	    output_row = list(output)
	    output_row[categories.index(i[1])] = 1
	    training_data.append([bag_of_words, output_row])

	#random shuffling the data to avoid ordering
	random.shuffle(training_data)

	#storing the training data as a numpy array
	training_data = np.array(training_data)

	#separating X and y from the training data
	train_X = list(training_data[:,0])
	train_y = list(training_data[:,1])

	return (train_X, train_y)


#function to add trailing zeros at the end of the answer
def add_trailing_dots(text):
    
    text_with_dots = text
    
    if text[len(text)-1] != ".":
        text_with_dots += "..."
        
    return text_with_dots


#function to format the answer
#if the alphabet is capital and does not have another capital alphabet, 
#a space and an opening bracket before it then add move the text to next line.

def formatted_text(text):
    
    formatted_str = text[0]
    
    for i in range(1, len(text)):
        if ord(text[i]) in range(65,91): 
            if ord(text[i-1]) not in range(65,91) and text[i-1] != " " and text[i-1] != "(":
                formatted_str += "\n\n" + text[i]
            else: 
                formatted_str += text[i]
        else:
            formatted_str += text[i]
            
    formatted_answer = add_trailing_dots(formatted_str)

    return formatted_answer





