from scraper.search_suggestion_keywords import Keyword


def main():
    k1 = Keyword(start="web", custom_web_driver=None, keywords=["a", "b", "c"])
    k2 = Keyword(start="web", custom_web_driver=None, keywords=k1.keywords)
    
    print(k1.keywords)
    k1.clear_keywords()
    print(k1.keywords)
    
    print(k2.keywords)
    
    

if __name__ == "__main__":
    main()