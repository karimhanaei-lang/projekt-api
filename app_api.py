import requests 
 
def get_MovieInfo_ByID(movie_id): 
    url = f'https://moviesapi.ir/api/v1/movies/{movie_id}' 
    response = requests.get(url) 
    if response.status_code != 200: 
        return 'ERROR' 
    else: 
        response = response.json() 
        poster = response['poster'] 
        title = response['title'] 
        year = response['year'] 
        dierctor = response['director'] 
        imdb_rating=  response['imdb_rating'] 
        imdb_votes =  response['imdb_votes'] 
        runtime = response['runtime'] 
        actors = response['actors'] 
        return poster, title, year, dierctor, imdb_rating, imdb_votes, runtime, actors 
######################################################### 
def get_MovieInfo_ByName(movie_name, page=1):
    # url = f'https://moviesapi.ir/api/v1/movies?q={movie_name}&page={page}'

    url = 'https://moviesapi.ir/api/v1/movies'
    mydict= {'q':movie_name, 'page':page}
    response = requests.get(url, params=mydict)
    if response.status_code != 200:
        return 'ERROR'
    else:
        response = response.json()
        # return response['data']
        response = response['data'][0]
        poster = response['poster']
        title = response['title']
        year = response['year']
        imdb_rating=  response['imdb_rating']
        return title, poster, year, imdb_rating
######################################################### 
def get_movie_list(page=1): 
    url = f"https://moviesapi.ir/api/v1/movies?page={page}" 
    response = requests.get(url) 
    if response.status_code != 200: 
        return "ERROR" 
    else: 
        output = [] 
        response = response.json() 
        response = response["data"] 
        for item in response: 
            title = item["title"] 
            poster = item["poster"] 
            imdb_rate = item["imdb_rating"] 
            genres = item["genres"] 
            output.append([title, poster, imdb_rate, genres]) 
        return output 

#############################################################################
def get_all_genres():
    url = 'https://moviesapi.ir/api/v1/genres'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data     
    else:
        return []

def get_movies_by_genre(genre_id, page=1):
    url = f'https://moviesapi.ir/api/v1/genres/{genre_id}/movies?page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()    
    else:
        return []
