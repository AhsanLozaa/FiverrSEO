import pandas as pd
from collections import Counter
import ast

from nltk.tokenize import word_tokenize


def check_cosine_similarity(row):
    try:
        description = row['description'].lower()
        title = row["title"].lower().replace("i will do ", "")
        title = title.split(" ")
        # print(title)
        # technologies = [tech.lower() for tech in row['title']]
        description_tokens = word_tokenize(description)
        similarities = {}
        for tech in title:
            tech_tokens = word_tokenize(tech.lower())
            description_counter = Counter(description_tokens)
            tech_counter = Counter(tech_tokens)
            intersection = set(description_counter.keys()) & set(tech_counter.keys())
            union = set(description_counter.keys()) | set(tech_counter.keys())
            similarity = len(intersection) / len(union)
            similarities[tech] = similarity

        # # counts = Counter(tech.lower() for tech in technologies if tech.lower() in description)
        print(similarities)
        # return similarities
    except Exception as e:
        return {}
    
def check_occurance(row):
    try:
        description = row['description'].lower()
        # technologies = [tech.lower() for tech in row['technology']]
        title = row["title"].lower()
        # .replace("i will do ", "")
        title_list = title.split(" ")
        counts = Counter(tech.lower() for tech in title_list if tech.lower() in description)
        
        # tokens = set(word_tokenize(desc))
        # matched_words = sum(1 for word in tokens if word in counter)
        total_words = sum(counts.values())
        matched_words = sum(counts[word] for word in title_list if word in counts)
        percantage = (matched_words/total_words) * 100
        
        print(title)
        print(counts, "     |     ", str(row["reviews_count"]))
        print(percantage)
        print("\n")
        
        
        return counts
    except Exception as e:
        return {}

def check_exact_title_math(row):
    try:
        description = row['description'].lower()
        title = row["title"].lower().replace("i will do ", "")
        if (title in description):
            print(title, "     |     ", str(row["reviews_count"]))
        # else:
        #     print(False)
    except Exception as e:
        return {}
    
def analyze_title_description(gigs_data_frame: pd.DataFrame):
    # gigs_data_frame['technology'] = gigs_data_frame['technology'].apply(ast.literal_eval)
    gigs_data_frame['technology_found'] = gigs_data_frame.apply(check_occurance, axis=1)
