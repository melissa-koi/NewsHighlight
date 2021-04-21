from flask import render_template
from ..request import get_source, get_articles
from .import main

@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    general = get_source('general')
    return render_template('index.html', general = general)

@main.route('/articles/<source>')
def articles(source):
    """
    View articles after clicking on id
    """
    article = get_articles(source)
    return render_template('news.html', articles=article, source = source)