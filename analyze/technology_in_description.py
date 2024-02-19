from collections import Counter
import pandas as pd
import ast

df = pd.read_csv("/Users/ahsanilyas/Documents/FiverrSEO/Data/gigs.csv")
df = df[df["reviews_count"] > 200]
df['technology'] = df['technology'].apply(ast.literal_eval)



def func1(row: pd.Series):
    try:
        reviews_count = row["reviews_count"]
        description = row["description"].lower()
        technology = row["technology"]
        technology = [item.lower() for item in technology]
        
        counts = Counter(tech.lower() for tech in technology if tech.lower() in description)
        # technology = list(map(lambda x: x.lower(), technology))
        
        print("\n")
        print(technology)
        print(counts)
        print(reviews_count)
    except Exception as e:
        pass



df['result'] = df.apply(func1, axis=1)