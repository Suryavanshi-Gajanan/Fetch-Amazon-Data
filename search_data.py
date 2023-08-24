from autoscraper import AutoScraper
from flask import Flask, request

amazon_scraper = AutoScraper()
amazon_scraper.load('search-data')
app = Flask(__name__)


def get_amazon_data(search_query):
    url = 'https://www.amazon.in/s?k=%s' % search_query
    result_data = amazon_scraper.get_result_similar(url, group_by_alias=True)
    return aggregate_result(result_data)


def aggregate_result(result):
    final_output = []
    print(list(result.values())[0])
    for i in range(len(list(result.values())[0])):
        try:

            final_output.append({alias: result[alias][i] for alias in result})
        except:
            pass
    return final_output


@app.route('/', methods=['GET'])
def search_api():
    query = request.args.get('q')
    print(query)
    return dict(result=get_amazon_data(query))


if __name__ == '__main__':
    app.run(debug=False)



