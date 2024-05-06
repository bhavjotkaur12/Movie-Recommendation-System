import pandas as pd

links_df = pd.read_csv('archive/links.csv')
movies_df = pd.read_csv('archive/movies.csv')
ratings_df = pd.read_csv('archive/ratings.csv')
tags_df = pd.read_csv('archive/tags.csv')

print(movies_df.head())
print(ratings_df.head())
print(tags_df.head())
print(links_df.head())