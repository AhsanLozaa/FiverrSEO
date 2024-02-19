import pandas as pd
import os
import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

def analyze_title():
    print("Analyzing Title")
    
    df = pd.read_csv("/Users/ahsanilyas/Documents/FiverrSEO/Data/gigs.csv")
    title_list = df["title"].tolist()
    print(title_list)
    # Count keyword occurences
    word_counter = Counter(word for text in title_list for word in text.lower().split())
    stop_words = set(stopwords.words('english'))
    filtered_counter = {word: count for word, count in word_counter.items() if count >= 5 and word not in stop_words}
    sorted_filtered_counter = dict(sorted(filtered_counter.items(), key=lambda item: item[1], reverse=True))
    
    # Plotting
    plt.bar(sorted_filtered_counter.keys(), sorted_filtered_counter.values())
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Word Occurrence in Titles')
    plt.xticks(rotation=45)
    plt.show()
    print(filtered_counter)
    
analyze_title()

