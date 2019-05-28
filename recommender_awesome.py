# 0. import libraries
from sqlalchemy import create_engine
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import process
import pandas as pd

#test
#movies = ['Heat', 'Shrek', 'Titanic']
#ratings = [5, 5, 3]

def get_matrix_from_db():
    '''
    Reads Postgres table and returns movie matrix
    '''
    db_sqlite = create_engine('sqlite:///mydatabase.db')

    df_ratings = pd.read_sql_table('ratings', db_sqlite, columns=['userid', 'movieid', 'rating'])
    df_movies = pd.read_sql_table('movies', db_sqlite, columns=['movieid', 'title'])

    df_ratings = df_ratings.set_index(['movieid', 'userid'])['rating'].unstack(1)
    df = pd.merge(df_movies, df_ratings, how='inner', on='movieid')
    df = df.set_index(['movieid', 'title']).transpose().fillna(0.0)

    return df


def add_new_user_to_matrix(movies, ratings, df):
    '''
    Takes previous df along with user input.
    Cleans input with fuzzywuzzy and returns concatenated
    matrix along with cleaned titles (needed for final function).
    '''
    movie_titles = list(df.columns.get_level_values(1))

    def fuzzy_wuzzy(m):
        movie_title = process.extract(m, movie_titles)[0][0]
        return movie_title

    movies_to_rate = [fuzzy_wuzzy(m) for m in movies]
    movies_rating = dict(zip(movies_to_rate, ratings))

    new_user = [movies_rating[m] if m in movies_rating else 0.0 for m in movie_titles]

    new_user_input = pd.DataFrame(new_user, index=df.columns).transpose()
    df_new = pd.concat([df, new_user_input])

    return df_new, movies_to_rate



def get_recommendations(movies, ratings):
    '''
    Runs previous two functions and applies cosine similarity algorithm.
    Finds most similar user and outputs the most five recommended movies.
    '''
    df = get_matrix_from_db()
    df_new, movies_to_rate = add_new_user_to_matrix(movies, ratings, df)

    df_cosine = pd.DataFrame(cosine_similarity(df_new, Y=None, dense_output=True), index=df_new.index, columns=df_new.index)

    data = df_cosine.loc[0][:-1]
    most_similar_user = pd.DataFrame(data.sort_values(ascending=False)).iloc[0]

    recommendations = df.iloc[most_similar_user.name].sort_values(ascending=False).index.get_level_values(1)[:8]

    recommendated_movies = [movie for movie in recommendations if movie not in movies_to_rate]

    return(recommendated_movies[:5])

#test
#print('ok')
