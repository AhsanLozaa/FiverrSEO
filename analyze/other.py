



# inputs -> dataframe
# output -> comparison between two columns

import pandas as pd
from collections import Counter
import ast

from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



df = pd.read_csv("/Users/ahsanilyas/Documents/FiverrSEO/Data/gigs.csv")
df = df[df["reviews_count"] > 300]
df['technology'] = df['technology'].apply(ast.literal_eval)
# def check_technologies(row):
#     try:
#         description = row['description'].lower()
#         technologies = [tech.lower() for tech in row['technology']]
#         counts = Counter(tech.lower() for tech in technologies if tech.lower() in description)
#         return counts
#     except Exception as e:
#         return False

# # Add a new column to the DataFrame to indicate if any technology is in the description
# df['technology_found'] = df.apply(check_technologies, axis=1)


# print(df['technology_found'])


def check_cosine_similarity(row):
    try:
        description = row['description'].lower()
        technologies = [tech.lower() for tech in row['technology']]
        description_tokens = word_tokenize(description)
        similarities = {}
        for tech in technologies:
            tech_tokens = word_tokenize(tech.lower())
            description_counter = Counter(description_tokens)
            tech_counter = Counter(tech_tokens)
            intersection = set(description_counter.keys()) & set(tech_counter.keys())
            union = set(description_counter.keys()) | set(tech_counter.keys())
            similarity = len(intersection) / len(union)
            similarities[tech] = similarity

        # counts = Counter(tech.lower() for tech in technologies if tech.lower() in description)
        print(similarities)
        return similarities
    except Exception as e:
        return {}
    
def check_occurance(row):
    try:
        description = row['description'].lower()
        technologies = [tech.lower() for tech in row['technology']]
        counts = Counter(tech.lower() for tech in technologies if tech.lower() in description)
        print(counts, "     |     ", str(row["reviews_count"]))
        return counts
    except Exception as e:
        return {}


# Add a new column to the DataFrame to indicate if any technology is in the description
# df['technology_found'] = df.apply(check_cosine_similarity, axis=1)
df['technology_found'] = df.apply(check_occurance, axis=1)


# similarities = {}
# for tech in technologies:
#     tech_tokens = word_tokenize(tech.lower())
#     description_counter = Counter(description_tokens)
#     tech_counter = Counter(tech_tokens)
#     intersection = set(description_counter.keys()) & set(tech_counter.keys())
#     union = set(description_counter.keys()) | set(tech_counter.keys())
#     similarity = len(intersection) / len(union)
#     similarities[tech] = similarity

# # Print similarities
# for tech, similarity in similarities.items():
#     print(f"{tech}: {similarity}")


# for index, row in df.iterrows():