import pandas as pd
import numpy as np


def trim_popular(ratings:pd.DataFrame):
    temp = ratings.groupby(['movieId'])['rating'].count()
    return ratings[ratings['movieId'].isin( np.where(temp>2)[0] )]

def trim_unpopular(ratings:pd.DataFrame):
    temp = ratings.groupby(['movieId'])['rating'].count()
    return ratings[ratings['movieId'].isin( np.where(temp<=2)[0] )]


def trimm_high_var(ratings:pd.DataFrame):
    movie_rating_vars_great_than_2 = np.where(ratings.groupby(['movieId'])['rating'].var(ddof=0) >=2 )[0]
    movie_count_great_than_5 = np.where(ratings.groupby(['movieId'])['rating'].count() >= 5 ) [0]
    
    return ratings[ratings['movieId'].isin(movie_rating_vars_great_than_2) & ratings['movieId'].isin(movie_count_great_than_5)]