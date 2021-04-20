import urllib.request, json

from flask import render_template

from .models import News
from newsapi import NewsApiClient



# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_source(category):
    get_news_details_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)
        print(news_details_response)

        news_object = None
        if news_details_response['sources']:
            source_library = news_details_response['sources']
            news_object = process_sources(source_library)
    return news_object
#     name = []
#     news_api = NewsApiClient(api_key='33fc8330b71f4cb684fa492fd9074cc3')
#     sources = news_api.get_sources()
#     for i in range(len(sources)):
#         my_profile = sources[i]
#         name.append(my_profile['name'])
#     mylist = zip(name)
#
#     return  render_template('index.html', context=mylist)
#
# if __name__ == "__main__":
#     app.run(debug=True)
#

def process_sources(source_library):
    '''
    Function  that processes the news result and transform them to a list of Objects
    '''
    source_results = []
    for source in source_library:
        id = source.get("id")
        name = source.get("name")
        description = source.get('description')
        url = source.get('url')
        category = source.get("category")

        data_sources = News(id,name,description,url,category)
        source_results.append(data_sources)

    return source_results

