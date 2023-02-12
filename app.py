import streamlit as st
import pickle
import numpy as np
import pandas as pd


movies_data = pickle.load(open('./books/movies.pkl','rb'))
similarities = pickle.load(open('./books/movie_similarities.pkl','rb'))
movies_df = pd.DataFrame(movies_data)
movies_title = movies_df['title'].values


def recommend(movie):
    movie = movie.lower()
    movie_id = movies_df[movies_df['lower_title'] == movie].index
    best5 = np.argsort(similarities[movie_id])[0,-6:-1]
    return movies_df['title'].values[best5]


# print(recommend('Avatar'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Choose a movie',
    movies_title
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for m in recommendations: # type: ignore
        st.write(m)
