import nltk
import numpy as np
import pandas as pd

# nltk.download_shell()         # Uncomment this line to download NLTK data files

# Load the dataset and use PANDAS to read it into a DataFrame 
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/sms.tsv"
messages = pd.read_csv(url, sep='\t', header=None, names=['label', 'message'])
#print(messages.head())
#print(len(messages))                                                # Print the number of messages in the dataset

'''
# Instead of using PANDAS built-in functions, we can use Python's standard functions to read and print the first 10 messages
for message_no, message in enumerate(messages['message'][0:10]):
    print(message_no+1, {message})                                  # Print the first 10 messages
    print('\n')
'''
    
#print(messages.describe())                                                     # Get a statistical summary of the dataset
#print(messages.groupby('label').describe())                                    # Group by label and get statistical summary

# Add a new column 'length' to the DataFrame that contains the length of each message
# This is done to better understand the data and for potential feature engineering
messages['length'] = messages['message'].apply(len)
#print(messages.head())

# Visualizations
import matplotlib.pyplot as plt
import seaborn as sns

messages['length'].plot(bins=50, kind='hist')               # Histogram of message lengths
#plt.show()

## Statistical summary of message lengths
## The results show count, mean, std, min, max etc length of messages
## The longest message has 910 characters
#print(messages.length.describe())                                                        

#print(messages[messages['length'] == 910]['message'].iloc[0])    # Print the longest message

## Histogram of message lengths by label (ham/spam)
messages.hist(column='length', by='label', bins=50, figsize=(12,4))
#plt.show()

#   WE ALREADY MADE A DISCOVERY FROM THE ABOVE HISTOGRAM                  #
#   IT SHOWS THAT SPAM MESSAGES TEND TO BE LONGER THAN HAM MESSAGES !!!   #





### TEXT PREPROCESSING ###

import nltk

import numpy as np
import pandas as pd

# Remove punctuation and stop words from the messages
import string

mess = 'Sample message! Notice: it has punctuation.'

nopunc = [char for char in mess if char not in string.punctuation]                              # Remove punctuation
nopunc = ''.join(nopunc)                                                                        # Join the characters back to form the string
print(nopunc)

from nltk.corpus import stopwords
stopwords = stopwords.words('english')                                                          # Get the list of English stop words (common words that do not provide significant meaning)   
#print(stopwords)

nopunc.split()                                                                                  # Split the message into words
clean_mess = [word for word in nopunc.split() if word.lower() not in stopwords]                 # Remove stop words
print(clean_mess)                                                                               # Print the cleaned message (without punctuation and stop words)

### FUNCTION TO PROCESS TEXT MESSAGES. DOES ALL THE STEPS WE PERFORMED ABOVE BUT IN A FUNCTION ###
def text_process(mess):
    """
    1. Remove punctuation
    2. Remove stop words
    3. Return a list of clean words
    """
    nopunc = [char for char in mess if char not in string.punctuation]                          # Remove punctuation
    nopunc = ''.join(nopunc)                                                                      # Join the characters back to form the string
    return [word for word in nopunc.split() if word.lower() not in stopwords]                     # Remove stop words and return clean words

print(text_process(mess))                  # Test the function

### APPLY THE FUNCTION TO THE DATAFRAME MESSAGES ###
messages['message'].head(5).apply(text_process)                                                  # Apply the function to the first 5 messages
print(messages.head())                                                                           # Print the DataFrame to see the changes

## PLEASE NOTE THERE IS MUCH MORE TEXT PREPROCESSING/ NORMALIZATION THAT CAN BE DONE BUT FOR THE SAKE OF THIS EXAMPLE, WE WILL KEEP IT SIMPLE ##


### TOKENIZATION AND VECTORIZATION ###

'''
We'll do that in three steps using the BAG-OF-WORDS model:
    1. Count how many times does a word occur in each message (Known as term frequency)
    2. Weigh the counts, so that frequent tokens get lower weight (inverse document frequency)
    3. Normalize the vectors to unit length, to abstract from the original text length (L2 norm)
'''

from sklearn.feature_extraction.text import CountVectorizer

# Create an instance of CountVectorizer with our text_process function as the analyzer
bow_transformer = CountVectorizer(analyzer=text_process).fit(messages['message'])             # Fit the CountVectorizer to the messages (bow = bag of words).
print(len(bow_transformer.vocabulary_))                                                       # Print the number of unique words. What this tells us is that there are 11425 unique words in the entire SMS corpus.

# Let's take a look at one of the messages and see how many times each word occurs in it
message4 = messages['message'][3]                                                              # Select the 4th message
print(message4)                                                                                 # Print the 4th message
bow4 = bow_transformer.transform([message4])                                                   # Transform the 4th message into a bag-of-words representation
print(bow4)                                                                                    # Print the bag-of-words representation (sparse matrix). Each row represents a message, and each column represents a unique word from the entire corpus. The values in the matrix indicate the count of each word in the message.
print(bow4.shape)                                                                              # Print the shape of the sparse matrix (1 message, 11425 unique words)
print(bow4.nnz)                                                                                # Print the number of non-zero entries in the sparse
print(bow_transformer.get_feature_names_out()[bow4.nonzero()[1]])                             # Print the words that occur in the 4th message

print(bow_transformer.get_feature_names_out()[4073])                                            # Print the word corresponding to index 4073
print(bow_transformer.get_feature_names_out()[9570])                                        # Print the word corresponding to index 9570

## Now let's see how to transform the entire DataFrame of messages.
messages_bow = bow_transformer.transform(messages['message'])
print('Shape of Sparse Matrix: ', messages_bow.shape)                                        # Print the shape of the sparse matrix for all messages. This shows there are 5572 messages and 11425 unique words.
print('Amount of Non-Zero occurences: ', messages_bow.nnz)                                   # Print the number of non-zero entries in the sparse matrix for all messages (50548 instances)

# Calculate sparsity. This is the percentage of non-zero entries in the matrix. A lower sparsity indicates that the matrix has more zero entries.
sparsity = (100.0 * messages_bow.nnz / (messages_bow.shape[0] * messages_bow.shape[1]))    # Calculate the sparsity of the matrix
print('Sparsity: {}'.format(sparsity))                                                       # Print the sparsity


### TF-IDF TRANSFORMATION # TF-IDF = Term Frequency - Inverse Document Frequency
# The idea is to downweight words that occur frequently across all documents and are therefore less informative than those that occur in a smaller portion of the documents.
# For example, words like "the", "is", "and" occur frequently in all messages and do not provide significant meaning. TF-IDF helps to highlight more meaningful words.

from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer().fit(messages_bow)                                    # Create an instance of TfidfTransformer and fit it to the bag-of-words representation of the messages
tfidf4 = tfidf_transformer.transform(bow4)                                                  # Transform the bag-of-words representation of the 4th message into TF-IDF representation
print(tfidf4)                                                                               # Print the TF-IDF representation of the 4th message
print(tfidf4.shape)                                                                         # Print the shape of the TF-IDF representation (1 message, 11425 unique words)

# Let's see the IDF (Inverse Document Frequency) values for some words
print(tfidf_transformer.idf_[bow_transformer.vocabulary_['u']])
print(tfidf_transformer.idf_[bow_transformer.vocabulary_['university']])

messages_tfidf = tfidf_transformer.transform(messages_bow)                             # Transform the entire bag-of-words representation of messages into TF-IDF representation

### TRAINING A CLASSIFIER ###
# Now that we have the TF-IDF representation of the messages, we can train a classifier to classify messages as spam or ham (not spam).
from sklearn.naive_bayes import MultinomialNB                                           # Import the Multinomial Naive Bayes classifier  
spam_detect_model = MultinomialNB().fit(messages_tfidf, messages['label'])                # Train the classifier using the TF-IDF representation of messages and their labels

# Let's try classifying our 4th message again
print('predicted:', spam_detect_model.predict(tfidf4)[0])                                              # Predict the label of the 4th message using the trained classifier    
print('expected:', messages.label[3])                                                   # Print the expected label of the 4th message
## We have successfully classified the 4th message as ham (not spam) ##

### PREDICTING ON THE TEST SET ###
all_predictions = spam_detect_model.predict(messages_tfidf)                             # Predict the labels for all messages in the dataset
print(all_predictions)                                                                    # Print all predicted labels

### EVALUATION ###
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(messages['label'], all_predictions))                             # Print the confusion matrix to evaluate the performance of the classifier
print(classification_report(messages['label'], all_predictions))                        # Print the classification report to evaluate the performance of the classifier


### SPLITTING DATA INTO TRAINING AND TEST SETS ###
from sklearn.model_selection import train_test_split
msg_train, msg_test, label_train, label_test = train_test_split(messages['message'], messages['label'], test_size=0.2)   # Split the dataset into training and testing sets (80% training, 20% testing)
print(len(msg_train), len(msg_test), len(msg_train) + len(msg_test))                   # Print the lengths of the training and testing sets

## Now we would NORMALLY NEED TO REPEAT the same steps as above but using the training and testing sets##
'''
# 1.  Create the bag-of-words transformer and fit it to the training messages
bow_transformer = CountVectorizer(analyzer=text_process).fit(msg_train)
# 2.  Transform the training and testing messages into bag-of-words representation
msg_train_bow = bow_transformer.transform(msg_train)
msg_test_bow = bow_transformer.transform(msg_test)
# 3.  Create the TF-IDF transformer and fit it to the training bag-of-words representation
tfidf_transformer = TfidfTransformer().fit(msg_train_bow)
# 4.  Transform the training and testing bag-of-words representation into TF-IDF representation
msg_train_tfidf = tfidf_transformer.transform(msg_train_bow)
msg_test_tfidf = tfidf_transformer.transform(msg_test_bow)
# 5.  Train the classifier using the training TF-IDF representation and labels
spam_detect_model = MultinomialNB().fit(msg_train_tfidf, label_train)
# 6.  Predict the labels for the testing TF-IDF representation
predictions = spam_detect_model.predict(msg_test_tfidf)
# 7.  Evaluate the performance of the classifier using confusion matrix and classification report
print(confusion_matrix(label_test, predictions))                             # Print the confusion matrix to evaluate the performance of the classifier
print(classification_report(label_test, predictions))                        # Print the classification report to evaluate the performance of the classifier
'''


### USING PIPELINES ###
# INSTEAD of repeating the same steps as above, we can use pipelines to streamline the process since this is a common sequence of steps in text classification tasks.
from sklearn.pipeline import Pipeline
pipeline = Pipeline([
    ('bow', CountVectorizer(analyzer=text_process)),                      # Step 1: Bag-of-words transformer
    ('tfidf', TfidfTransformer()),                                        # Step 2: TF-IDF transformer
    ('classifier', MultinomialNB())                                       # Step 3: Classifier
])

pipeline.fit(msg_train, label_train)                                      # Train the pipeline using the training messages and labels. This will automatically perform all the steps in the pipeline.
predictions = pipeline.predict(msg_test)                                  # Predict the labels for the testing messages using the trained pipeline

print(confusion_matrix(label_test, predictions))                          # Print the confusion matrix to evaluate the performance
print(classification_report(label_test, predictions))                     # Print the classification report to evaluate the performance
