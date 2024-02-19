import pandas as pd
from collections import Counter
import ast
from bs4 import BeautifulSoup


from nltk.tokenize import word_tokenize



df = pd.read_csv("/Users/ahsanilyas/Documents/FiverrSEO/Data/gigs.csv")
df = df[df["reviews_count"] > 100]

def func1(row: pd.Series):
    try:
        title = row["title"]
        reviews_count = row["reviews_count"]
        description_html = row["description_html"]
        soup = BeautifulSoup(description_html, 'html.parser')
        extracted_items = {}
        items_to_extract = ['strong', 'u', 'li']
        # items_to_extract = ['u']

        for tag in items_to_extract:
            element = soup.find(tag)
            if element:
                extracted_items[tag] = element.text

        print("\n")
        print(title)
        # print(extracted_items)
        for key in extracted_items:
            print(f"{key}: {extracted_items[key]}")
        print(reviews_count)
    except Exception as e:
        pass
    # breakpoint()


df['result'] = df.apply(func1, axis=1)
