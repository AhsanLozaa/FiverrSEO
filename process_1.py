import os
from utils import get_specific_files_from_specific_folder, convert_multiple_csv_files_to_one_dataframe
import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')


def main():
    data_folder_path = "./data"
    csv_files_list = get_specific_files_from_specific_folder(folderPath=data_folder_path, fileType=".csv")
    df = convert_multiple_csv_files_to_one_dataframe(files_list=csv_files_list)
    
    # extract only the iems having ratings_count > 100
    df = df[df["ratings_count"] > 100]
    # Count keyword occurences
    word_counter = Counter(word for text in df['title'] for word in text.lower().split())
    # filtered_counter = {word: count for word, count in word_counter.items() if count >= 10}
    # filter out the stop words
    stop_words = set(stopwords.words('english'))
    filtered_counter = {word: count for word, count in word_counter.items() if count >= 10 and word not in stop_words}
    
    sorted_filtered_counter = dict(sorted(filtered_counter.items(), key=lambda item: item[1], reverse=True))

    # Plotting
    plt.bar(sorted_filtered_counter.keys(), sorted_filtered_counter.values())
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Word Occurrence in Titles')
    plt.xticks(rotation=45)
    plt.show()

    

if __name__ == "__main__":
    main()