import urllib.request, json
from .models import News


# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_source(category):
    get_news_details_url = base_url.format(category)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response['sources']:
            source_library = news_details_response.get['sources']
            news_object = process_sources(source_library)
        else :
            print("noneee")
    return news_object

def process_sources(sources):
    '''
    Function  that processes the news result and transform them to a list of Objects
    '''
    source_results = []
    for source in sources:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        category = source.get("category")

        data_sources = News(id,name,description,url,category)
        source_results.append(data_sources)

    return source_results

