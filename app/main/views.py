from flask import render_template
from ..request import get_source
from .import main
from ..models import News

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''



    general = get_source('general')


    return render_template('index.html', general = general)


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
