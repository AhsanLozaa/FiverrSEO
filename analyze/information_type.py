import pandas as pd
import os
import ast
import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

def analyze_information_types():
    print("Analyzing Title")
    
    df = pd.read_csv("/Users/ahsanilyas/Documents/FiverrSEO/Data/gigs.csv")
    df['information_type'] = df['information_type'].apply(ast.literal_eval)
    df = df[df["reviews_count"] > 300]

    information_type_list = df['information_type'].explode().tolist()
    filtered_information_type_list = [item for item in information_type_list if pd.notnull(item) and item]
    item_counter = Counter(item.lower() for item in filtered_information_type_list)
    unique_items = list(set(filtered_information_type_list))
    sorted_filtered_counter = dict(sorted(item_counter.items(), key=lambda item: item[1], reverse=True))
    sorted_filtered_counter = dict(sorted(item_counter.items(), key=lambda item: item[1], reverse=True))
    
    # Plotting
    plt.bar(sorted_filtered_counter.keys(), sorted_filtered_counter.values())
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Word Occurrence in Titles')
    plt.xticks(rotation=45)
    plt.show()
    
analyze_information_types()

