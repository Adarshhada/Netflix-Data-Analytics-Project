import pandas as pd
import matplotlib.pyplot as plt

# Load the Data
df = pd.read_csv(r'C:\Users\aadar\Downloads\netflix_titles.csv.zip')


# Clean Data
df = df.dropna(subset=['type','release_year','rating','country','duration'])

# Count types (Movies vs Tv shows)
type_counts = df['type'].value_counts()

# Plot
plt.figure(figsize=(6,4))
plt.bar(type_counts.index, type_counts.values, color = ['skyblue','orange'])
plt.title('Number of Movies VS Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.show()




rating_counts = df['rating'].value_counts()
plt.figure(figsize = (8,6))
plt.pie(rating_counts, labels = rating_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Percentage of Content Rating')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.show()




movie_df = df[df['type'] == 'Movie'].copy()
movie_df['duration_int'] = movie_df['duration'].str.replace('min', '').astype(int)
plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'], bins = 30, color = 'purple' , edgecolor='black')
plt.title('Distribution of Movie Duration')
plt.xlabel('Duration (min)')
plt.ylabel('Number of Movies')
plt.show()




release_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_counts.index, release_counts.values, color = 'red')
plt.title('Release Year VS Number of Shows')
plt.xlabel('Release Year')
plt.ylabel('Number of Shows')
plt.tight_layout()
plt.show()





country_counts = df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_counts.index, country_counts.values, color='teal')
plt.title('Top 10 Country by Number of Shows')
plt.xlabel('Number of Shows')
plt.ylabel('Country')
plt.tight_layout()
plt.show()


content_by_year = df.groupby(['release_year', 'type']).size().unstack().fillna(0)
fig, ax = plt.subplots(1,2, figsize=(12,5))

#first subplot = movie
ax[0].plot(content_by_year.index, content_by_year['Movie'], color='blue')
ax[0].set_title('Movies Release Per Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')


# Second subplot = tv shows
ax[0].plot(content_by_year.index, content_by_year['TV Show'], color='orange')
ax[0].set_title('TV Show Release Per Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of TV Show')
fig.suptitle('Comparision of Movies and TV Shows Released Over Years')
plt.tight_layout()
plt.show()



