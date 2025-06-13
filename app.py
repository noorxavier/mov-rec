import streamlit as st
import pickle
import pandas as pd
import requests

#pkl file retrieving from Gdrive
import os
import requests

def download_file(url, output_path):
    response = requests.get(url)
    with open(output_path, 'wb') as f:
        f.write(response.content)

if not os.path.exists("similarity.pkl"):
    url ="https://github.com/noorxavier/mov-rec/releases/tag/v1.0"
    download_file(url, "similarity.pkl")


# Fetch poster using TMDB API
def fetch_poster(movie_id):
    response = requests.get(
        url=f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=827d2c2685fcf72b5e0b75e13b709fdd&language=en-US"
    )
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


# Load data
movies = pickle.load(open('movies.pkl', 'rb'))  # DataFrame with 'title' and 'movie_id'
similarity = pickle.load(open('similarity.pkl', 'rb'))


# Recommend function
def recommend(movie_title):
    movie_index = movies[movies['title'] == movie_title].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id  # Correctly get the TMDB movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_poster


# Streamlit UI
st.title('Movie Recommender System')

movie_titles = movies['title'].values
selected_movie_name = st.selectbox('Select a Movie', movie_titles)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
