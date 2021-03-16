# the entire file has been made by Karolina Szwedo
import pandas as pd
import numpy as np
import re
import datetime
import matplotlib.pyplot as plt

df = pd.read_csv('imdb/imdb/spiders/movies.csv')

# cleaning data
df['time'] = df['time'].replace("min",'', regex=True)
df['when'] = df['when'].replace("\([^\)]*\)",'', regex=True)
df['when'] = df['when'].replace("Video",'', regex=True)
# change "when" to date type
df['when'] = pd.to_datetime(df['when'])

# get month from the date
df['month'] = pd.DatetimeIndex(df['when']).month
df['month'] = df['month'].map({1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'})

# function which classify "time"
def flag_df(df):
    if pd.notna(df['time']) == True:
        try:
            if (int(df['time']) < 100):
                return '< 100 min'
            elif (int(df['time']) > 100 and int(df['time']) <= 120):
                return '(100 min, 120 min)'
            elif (int(df['time']) > 120):
                return '>120 min'
        except:
            return np.nan

df['time_group'] = df.apply(flag_df, axis = 1)

# create dataframe only with "coming soon" movies
today = datetime.datetime.now()
df_filter = df.loc[df['when'] > today.strftime("%Y-%m-%d")]

# variable analisis for all movies:

# STARS (FOR ALL MOVIES)
# split to get data from lists
stars_split = df.stars.str.split(",",expand=True)
list1 = stars_split[0].to_list()
list2 = stars_split[1].to_list()
list3 = stars_split[2].to_list()
stars = list1 + list2 + list3
# create dataframe to count values
stars_df = pd.DataFrame(data = stars, columns = ['star'])
print('Stars all movies:')
print(stars_df.star.value_counts()[:26])

# DIRECTOR (FOR ALL MOVIES)
# split to get data from lists
directors_split = df.director.str.split(",",expand=True)
list1 = directors_split[0].to_list()
list2 = directors_split[1].to_list()
directors = list1 + list2
# create dataframe to count values
directors_df = pd.DataFrame(data = directors, columns = ['directors'])
print('\nDirectors all movies:')
print(directors_df.directors.value_counts()[:10])

# WRITER (FOR ALL MOVIES)
# split to get data from lists
writer_split = df.writer.str.split(",",expand=True)
list1 = writer_split[0].to_list()
list2 = writer_split[1].to_list()
writer = list1 + list2
# create dataframe to count values
writer_df = pd.DataFrame(data = writer, columns = ['writer'])
print('\nWriters all movies:')
print(writer_df.writer.value_counts()[:20])

# WHEN (FOR ALL MOVIES)
df.month.value_counts()
# chart
fig, ax1 = plt.subplots(1, 1, figsize=(6,4))

ax1 = df.month.value_counts().plot(kind='bar', color='magenta')
y1 = df.month.value_counts()
# delete eges
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
# write a value for each column
for i, p in enumerate(ax1.patches):
    ax1.annotate(y1[i], (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', rotation=0, xytext=(0, 10), textcoords='offset points')

plt.title("Release month")
plt.tight_layout()
plt.savefig('charts/when.png')

# TIME (FOR ALL MOVIES)
df.time_group.value_counts()
# chart
fig, ax2 = plt.subplots(1, 1, figsize=(6,4))

ax2 = df.time_group.value_counts().plot(kind='bar', color='magenta')
y2 = df.time_group.value_counts()
# delete eges
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
# write a value for each column
for i, p in enumerate(ax2.patches):
    ax2.annotate(y2[i], (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', rotation=0, xytext=(0, 10), textcoords='offset points')

plt.title("Duration")
plt.tight_layout()
plt.savefig('charts/time.png')

# COUNTRY (FOR ALL MOVIES)
# split to get data from lists
country_split = df.country.str.split(",",expand=True)
list1 = country_split[0].tolist()
list2 = country_split[1].tolist()
list3 = country_split[2].tolist()
list4 = country_split[3].tolist()
list5 = country_split[4].tolist()

country = list1 + list2 + list3 + list4 + list5

# create dataframe to count values
country_df = pd.DataFrame(data = country, columns = ['country'])
country_df.country.value_counts()

# chart
fig, ax3 = plt.subplots(1, 1, figsize=(6,4))

ax3 = country_df.country.value_counts().plot(kind='bar', color='magenta')
y3 = country_df.country.value_counts()
# delete eges
ax3.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)
# write a value for each column
for i, p in enumerate(ax3.patches):
    ax3.annotate(y3[i], (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', rotation=0, xytext=(0, 10), textcoords='offset points')

plt.title("Country of origin")
plt.tight_layout()
plt.savefig('charts/countries.png')

# GENRES (FOR ALL MOVIES)
# split to get data from lists
genres_split = df.genres.str.split(",",expand=True)
list1 = genres_split[0].tolist()
list2 = genres_split[1].tolist()
list3 = genres_split[2].tolist()
genres = list1 + list2 + list3

# create dataframe to count values
genres_df = pd.DataFrame(data = genres, columns = ['genres'])
genres_df.genres.value_counts()

# chart
fig, ax4 = plt.subplots(1, 1, figsize=(6,4))

ax4 = genres_df.genres.value_counts().plot(kind='bar', color='magenta')
y4 = genres_df.genres.value_counts()
# delete eges
ax4.spines['right'].set_visible(False)
ax4.spines['top'].set_visible(False)
# write a value for each column
for i, p in enumerate(ax4.patches):
    ax4.annotate(y4[i], (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', rotation=0, xytext=(0, 10), textcoords='offset points')

plt.title("Genres")
plt.tight_layout()
plt.savefig('charts/genres.png')

# LANGUAGE (FOR ALL MOVIES)
# split to get data from lists
language_split = df.language.str.split(",",expand=True)
list1 = language_split[0].tolist()
list2 = language_split[1].tolist()
language = list1 + list2

# create dataframe to count values
language_df = pd.DataFrame(data = language, columns = ['language'])
language_df.language.value_counts()

# chart
fig, ax5 = plt.subplots(1, 1, figsize=(6,4))

ax5 = language_df.language.value_counts().plot(kind='bar', color='magenta')
y5 = language_df.language.value_counts()
# delete eges
ax5.spines['right'].set_visible(False)
ax5.spines['top'].set_visible(False)
# write a value for each column
for i, p in enumerate(ax5.patches):
    ax5.annotate(y5[i], (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', rotation=0, xytext=(0, 10), textcoords='offset points')

plt.title("Language")
plt.tight_layout()
plt.savefig('charts/languages.png')

# variable analisis for "coming soon" movies:

# STARS (COMING SOON MOVIES)
# split to get data from lists
stars_split = df_filter.stars.str.split(",",expand=True)
list1 = stars_split[0].to_list()
list2 = stars_split[1].to_list()
list3 = stars_split[2].to_list()
stars = list1 + list2 + list3
# create dataframe to count values
stars_df = pd.DataFrame(data = stars, columns = ['star'])
print('\nStars coming soon movies:')
print(stars_df.star.value_counts()[:16])

# DIRECTOR (COMING SOON MOVIES)
# split to get data from lists
directors_split = df_filter.director.str.split(",",expand=True)
list1 = directors_split[0].to_list()
list2 = directors_split[1].to_list()
directors = list1 + list2
# create dataframe to count values
directors_df = pd.DataFrame(data = directors, columns = ['directors'])
print('\nDirectors coming soon movies:')
print(directors_df.directors.value_counts()[:2])

# WRITER (COMING SOON MOVIES)
# split to get data from lists
writer_split = df_filter.writer.str.split(",",expand=True)
list1 = writer_split[0].to_list()
list2 = writer_split[1].to_list()
writer = list1 + list2
# create dataframe to count values
writer_df = pd.DataFrame(data = writer, columns = ['writer'])
print('\nWriters coming soon movies:')
print(writer_df.writer.value_counts()[:6])

# WHEN (COMING SOON MOVIES)
df_filter.month.value_counts()

# chart
fig, ax6 = plt.subplots(1, 1, figsize=(6,4))

ax6 = df_filter.month.value_counts().plot(kind='bar', color='magenta')
y6 = df_filter.month.value_counts()
# delete eges
ax6.spines['right'].set_visible(False)
ax6.spines['top'].set_visible(False)
# write a value for each column
for i, p in enumerate(ax6.patches):
    ax6.annotate(y6[i], (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', rotation=0, xytext=(0, 10), textcoords='offset points')

plt.title("Release month")
plt.tight_layout()
plt.savefig('charts/when_coming_soon.png')

# TIME (COMING SOON MOVIES)
df_filter.time_group.value_counts()
# chart
fig, ax7 = plt.subplots(1, 1, figsize=(6,4))

ax7 = df_filter.time_group.value_counts().plot(kind='bar', color='magenta')
y7 = df_filter.time_group.value_counts()
# delete eges
ax7.spines['right'].set_visible(False)
ax7.spines['top'].set_visible(False)
# write a value for each column
for i, p in enumerate(ax7.patches):
    ax7.annotate(y7[i], (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', rotation=0, xytext=(0, 10), textcoords='offset points')

plt.title("Duration")
plt.tight_layout()
plt.savefig('charts/time_coming_soon.png')

# COUNTRY (COMING SOON MOVIES)
# split to get data from lists
country_split = df_filter.country.str.split(",",expand=True)
list1 = country_split[0].tolist()
list2 = country_split[1].tolist()
list3 = country_split[2].tolist()
list4 = country_split[3].tolist()
list5 = country_split[4].tolist()
country = list1 + list2 + list3 + list4 + list5
# create dataframe to count values
country_df = pd.DataFrame(data = country, columns = ['country'])
country_df.country.value_counts()

# chart
fig, ax8 = plt.subplots(1, 1, figsize=(6,4))

ax8 = country_df.country.value_counts().plot(kind='bar', color='magenta')
y8 = country_df.country.value_counts()
# delete eges
ax8.spines['right'].set_visible(False)
ax8.spines['top'].set_visible(False)
# write a value for each column
for i, p in enumerate(ax8.patches):
    ax8.annotate(y8[i], (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', rotation=0, xytext=(0, 10), textcoords='offset points')

plt.title("Country of origin")
plt.tight_layout()
plt.savefig('charts/countries_coming_soon.png')

# GENRES (COMING SOON MOVIES)
# split to get data from lists
genres_split = df_filter.genres.str.split(",",expand=True)
list1 = genres_split[0].tolist()
list2 = genres_split[1].tolist()
list3 = genres_split[2].tolist()
genres = list1 + list2 + list3
# create dataframe to count values
genres_df = pd.DataFrame(data = genres, columns = ['genres'])
genres_df.genres.value_counts()

# chart
fig, ax9 = plt.subplots(1, 1, figsize=(6,4))

ax9 = genres_df.genres.value_counts().plot(kind='bar', color='magenta')
y9 = genres_df.genres.value_counts()
# delete eges
ax9.spines['right'].set_visible(False)
ax9.spines['top'].set_visible(False)
# write a value for each column
for i, p in enumerate(ax9.patches):
    ax9.annotate(y9[i], (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', rotation=0, xytext=(0, 10), textcoords='offset points')

plt.title("Genres")
plt.tight_layout()
plt.savefig('charts/genres_coming_soon.png')

# LANGUAGE (COMING SOON MOVIES)
# split to get data from lists
language_split = df_filter.language.str.split(",",expand=True)
list1 = language_split[0].tolist()
list2 = language_split[1].tolist()
language = list1 + list2
# create dataframe to count values
language_df = pd.DataFrame(data = language, columns = ['language'])
language_df.language.value_counts()

# chart
fig, ax10 = plt.subplots(1, 1, figsize=(6,4))

ax10 = language_df.language.value_counts().plot(kind='bar', color='magenta')
y10 = language_df.language.value_counts()
# delete eges
ax10.spines['right'].set_visible(False)
ax10.spines['top'].set_visible(False)
# write a value for each column
for i, p in enumerate(ax10.patches):
    ax10.annotate(y10[i], (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', rotation=0, xytext=(0, 10), textcoords='offset points')

plt.title("Language")
plt.tight_layout()
plt.savefig('charts/languages_coming_soon.png')
