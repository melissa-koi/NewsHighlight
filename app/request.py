import urllib.request, json

from flask import render_template

from app.models import News, Articles
from newsapi import NewsApiClient
from instance import config


# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_APIKEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_source(category):
    get_news_details_url =base_url.format(category, api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response['sources']:
            source_library = news_details_response['sources']
            news_object = process_sources(source_library)
    return news_object

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

def get_articles(source):

    article_news = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=33fc8330b71f4cb684fa492fd9074cc3'.format(source)

    with urllib.request.urlopen(article_news) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)

        article_object = None
        if article_details_response['articles']:
            article_library = article_details_response['articles']
            article_object = process_articles(article_library)
    return article_object

def process_articles(article_news):
    article_results = []
    for article in article_news:
        id = article.get("id")
        name = article.get("name")
        title = article.get("title")
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get("publishedAt")

        data_articles = Articles(id,name,title,description,url,urlToImage,publishedAt)
        article_results.append(data_articles)

    return article_results