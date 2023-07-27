import nltk
from nltk.corpus import gutenberg
from nltk.corpus import stopwords
from collections import Counter

# Load Macbeth text from the Gutenberg corpus
macbeth_words = gutenberg.words('shakespeare-macbeth.txt')

# Get English stopwords
stop_words = set(stopwords.words('english'))

# Filter out stopwords and convert to lowercase
filtered_words = [word.lower() for word in macbeth_words if word.lower() not in stop_words]

# Count the frequencies of the remaining words
word_counts = Counter(filtered_words)

# Print the most common words
print(word_counts.most_common(10))

