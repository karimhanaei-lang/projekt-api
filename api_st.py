import streamlit as st 
 
import app_api

import json 
 
st.title('API STREAMLIT') 
 
option = st.sidebar.selectbox('Select Your Option: ',  
                              ("CALL API BY ID", 'CALL API BY NAME', "CALL API BY PAGE" 
                               , "CALL API BY GENRE ID")) 
if option == 'CALL API BY ID': 
    movie_id = st.number_input('enter movie id: ', min_value=1, max_value=250) 
    if st.button('Display Info: '): 
        result = app_api.get_MovieInfo_ByID(movie_id) 
        if result !='ERROR': 
            st.success('DATA DISPLAY BELOW') 
            st.image(result[0]) 
            st.write(result[1:]) 
        else: 
            st.error('DATA NOT FOUND')

elif option == 'CALL API BY NAME':
    movie_name = st.text_input('enter movie name: ')

    if st.button('Display Info: '):
        result = app_api.get_MovieInfo_ByName(movie_name)
        if result !='ERROR':
            st.success('DATA DISPLAY BELOW')
            st.write(result)
        else:
            st.error('DATA NOT FOUND')

elif option == "CALL API BY PAGE": 
    page = st.number_input('enter page: ', min_value=1, max_value=25) 
    if st.button("Display info: "): 
        result = app_api.get_movie_list(page) 
        if result != "ERROR": 
            st.success("DATA DISPLAY BELOW") 
            st.write(result) 
        else: 
            st.error("DATA NOT FOUND")

elif option == "CALL API BY GENRE ID":
    st.subheader("🎬 MOVIES & GENRE ")
    genres = app_api.get_all_genres()
    if genres:
        genre_names = [g['name'] for g in genres]
        selected_genre_name = st.selectbox("ENTER GENRE:", genre_names)
        selected_genre_id = next(g['id'] for g in genres if g['name'] == selected_genre_name)
        page = st.number_input("ROW PAGE :", min_value=1, value=1)

        if st.button("show filme "):
            response = app_api.get_movies_by_genre(selected_genre_id, page)
            movies = response.get('data', [])
            
            if movies:
                st.success(f"film genre {selected_genre_name}  :")
                
                for movie in movies:
                    col1, col2 = st.columns([1, 3])
                    
                    with col1:
                        
                        poster = movie.get('poster')
                        if poster:
                            st.image(poster)
                    
                    with col2:
                        st.subheader(movie.get('title', 'NOT TITLE '))
                        st.write(f"⭐ RATING: {movie.get('imdb_rating', '---')}")
                        st.write(f"📅 YERS: {movie.get('year', '---')}")
                    
                    st.divider() 
            else:
                st.error("NOT FILME")
