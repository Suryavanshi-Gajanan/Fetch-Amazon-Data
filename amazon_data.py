from autoscraper import AutoScraper
amazon_url="https://www.amazon.in/s?k=iphones"
wanted_list=["₹67,999","Apple iPhone 14 (128 GB) - Blue"]
scraper=AutoScraper()
result=scraper.build(amazon_url,wanted_list)
# print(result)

print(scraper.get_result_similar(amazon_url,grouped=True))

# scraper.set_rule_aliases({'rule_0sh6':'Title','rule_61o0':'Price'})
# scraper.keep_rules(['rule_bpu7','rule_61o0'])
scraper.save('amazon-search')