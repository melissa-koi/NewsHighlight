import urllib.request,json
from .models import News
import urllib.request, json

# Getting api key
api_key = None
# Getting the movie base url
base_url = None


def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_source():
    get_news_details_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            id = news_details_response.get('id')
            name = news_details_response.get('name')
            description = news_details_response.get('description')

            movie_object = News(id, name, description)

    return news_object


# def get_movies(category):
#     '''
#     Function that gets the json response to our url request
#     '''
#     get_movies_url = base_url.format(category,api_key)
#
#     with urllib.request.urlopen(get_movies_url) as url:
#         get_movies_data = url.read()
#         get_movies_response = json.loads(get_movies_data)
#
#         movie_results = None
#
#         if get_movies_response['results']:
#             movie_results_list = get_movies_response['results']
#             movie_results = process_results(movie_results_list)
#
#
#     return movie_results
#
def process_results(news_object):
    # '''
    # Function  that processes the newsresult and transform them to a list of Objects
    #
    # Args:
    #     movie_list: A list of dictionaries that contain movie details
    #
    # Returns :
    #     movie_results: A list of movie objects
    # '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        if name:
            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)
            news_results.append(movie_object)

    return news_results

