from flask import render_template,request,redirect,url_for
from ..request import get_source
from .import main
from ..models import News

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Welcome'
    general = get_source('general')

    return render_template('index.html', general = general)


