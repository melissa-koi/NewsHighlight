from flask import render_template,request,redirect,url_for
from ..request import get_source
# from .forms import ReviewForm
from ..models import News
from .import main

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    # news_id = get_source('id')
    # news_name = get_source('name')
    # news_description = get_source('description')

    # title = 'Home - Welcome to The best Movie Review Website Online'

    render_template('request.html' )

# @main.route('/movie/<int:id>')
# def movie(id):
#
#     '''
#     View movie page function that returns the movie details page and its data
#     '''
#
#     movie = get_movie(id)
#     title = f'{movie.title}'
#     reviews = Review.get_reviews(movie.id)
#
#     return render_template('movie.html',title = title,movie = movie,reviews = reviews)
