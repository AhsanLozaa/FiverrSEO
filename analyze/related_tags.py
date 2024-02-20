import pandas as pd
import os
import ast
import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords
import nltk
import itertools
nltk.download('stopwords')

def analyze_related_tags():
    # df = pd.read_csv("/Users/ahsanilyas/Documents/FiverrSEO/Data/gigs.csv")
    # df = df[df["reviews_count"] > 500]
    # for _, row in df.iterrows():
    #     print(len(row["title"].lower().replace("i will ", "")))
    # return
    print("Analyzing Related Tags")
    for i in range(1, 2):
        df = pd.read_csv("/Users/ahsanilyas/Documents/FiverrSEO/Data/gigs.csv")
        df.dropna(subset=['related_tags'], inplace=True)
        df['related_tags'] = df['related_tags'].apply(ast.literal_eval)
        df = df[df["reviews_count"] > 100]
        realted_tags_list = df['related_tags'].explode().tolist()
        filtered_realted_tags_list = [item for item in realted_tags_list if pd.notnull(item) and item]
        item_counter = Counter(item.lower() for item in filtered_realted_tags_list)
        unique_items = list(set(filtered_realted_tags_list))
        sorted_filtered_counter = dict(sorted(item_counter.items(), key=lambda item: item[1], reverse=True))
        sorted_filtered_counter = dict(sorted(item_counter.items(), key=lambda item: item[1], reverse=True))
        
        for key, value in itertools.islice(sorted_filtered_counter.items(), 40):
            # print("key: ", key, ",  value: ", str(value), " | ", end="")
            print(key)
        
        # print()

        
        # # Plotting
        # plt.bar(sorted_filtered_counter.keys(), sorted_filtered_counter.values())
        # plt.xlabel('Words')
        # plt.ylabel('Frequency')
        # plt.title('Word Occurrence in Titles')
        # plt.xticks(rotation=45)
        # plt.show()
    
analyze_related_tags()



