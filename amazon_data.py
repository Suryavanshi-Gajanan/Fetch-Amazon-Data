from autoscraper import AutoScraper
amazon_url="https://www.amazon.in/s?k=iphones"
search_list=["₹67,999","Apple iPhone 14 (128 GB) - Blue"]
scraper=AutoScraper()
result_data=scraper.build(amazon_url,search_list)
scraper.get_result_similar(amazon_url,grouped=True)
scraper.save('search-data')