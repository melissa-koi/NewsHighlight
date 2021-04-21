from flask import render_template,request,redirect,url_for
from ..request import get_source
from .import main
from ..models import News
from newsapi import NewsApiClient
from instance import config

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    general = get_source('general')

    return render_template('index.html', general = general)

@main.route('/articles/<int:id>')
def articles():
    newsapi = NewsApiClient(config.NEWS_API_KEY)
    all_articles = newsapi.get_everything(sources='bbc-news')