#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
movie = pd.read_csv('movies.csv')
movie.head()


# In[5]:


print(movie.shape)


# In[6]:


ratings = pd.read_csv('ratings.csv')
ratings.head()


# In[7]:


print(ratings.shape)


# In[10]:


unique_users = ratings.userId.unique()


# In[11]:


print(len(unique_users))


# In[12]:


ratings.movieId.value_counts()


# In[18]:


print(movie[movie['movieId'] == 356])


# In[20]:


tags = pd.read_csv('tags.csv')
tags.head()


# In[21]:


# movie id of Matrix, The (1999)
print(movie[movie['title'] == 'Matrix, The (1999)'])


# In[22]:


# movieId of Matrix, The (1999) = 2571
new_df = pd.DataFrame(tags[tags['movieId']==2571])


# In[23]:


# tags for Matrix 
new_df


# In[24]:


# movieId for Terminator 2: Judgment Day (1991)
print(movie[movie['title']=='Terminator 2: Judgment Day (1991)'])


# In[25]:


# movieId for Terminator 2 is 589
# rating table with movieId = 589
# What is the average user rating for movie named "Terminator 2: Judgment Day (1991)"?
a = pd.DataFrame(ratings[ratings['movieId']==589])
print(a)


# In[34]:


import statistics
x = sum(a['rating'])
print(x)
# rows = 224
avg = x/224
print(avg)
print(statistics.mean(a['rating']))


# In[35]:


#How does the data distribution of user ratings for "Fight Club (1999)" movie looks like?
# 1. movieId of Fight Club

print(movie[movie['title']=='Fight Club (1999)'])


# In[36]:


#movieId = 2959

fcdf = pd.DataFrame(ratings[ratings['movieId']==2959])
print(fcdf)


# In[37]:


import matplotlib.pyplot as plt
fcdf['rating'].hist()
plt.show()
#left skewed histogram


# In[38]:


# Which movie is the most popular based on  average user ratings? *
#Godfather, The (1972)
#Shawshank Redemption, The (1994)
#Jumanji (1995)
#Wolf of Wall Street, The (2013)


# In[ ]:


1. Group the user ratings based on movieId and apply aggregation operations like count and mean on ratings. 
2. Apply inner join on dataframe created from movies.csv and the grouped df from step 1.
3. Filter only those movies which have more than 50 user ratings (i.e. > 50).


# In[99]:


# 1
modified_ratings = pd.DataFrame()
modified_ratings['movieId'] = ratings.movieId.unique()
modified_ratings


# In[88]:


lst = ratings[ratings['movieId']==1]


# In[103]:


rating_list = list(lst['rating'])
print(len(rating_list))
print(statistics.mean(rating_list))


# In[100]:


count = 0
for i in modified_ratings['movieId']:
    r = ratings[ratings['movieId']==i]
    r_l = list(r['rating'])
    modified_ratings.at[count,'ratings_count']=len(r_l) 
    modified_ratings.at[count,'ratings_mean']=statistics.mean(r_l)
    count+=1
    


# In[101]:


modified_ratings.head()


# In[104]:


new_mds = mds.copy()


# In[108]:


new_mds=new_mds.merge(modified_ratings, on='movieId')


# In[109]:


new_mds


# In[110]:


count_fifty = pd.DataFrame(new_mds[new_mds['ratings_count']>50])


# In[111]:


count_fifty


# In[113]:


sorted_cf=count_fifty.sort_values(by='ratings_mean', ascending=False)


# In[118]:


sorted_cf.head(10)


# In[115]:


no_sort = count_fifty.sort_values(by='ratings_count', ascending=False)


# In[117]:


no_sort.head(20)


# In[120]:


pip install BeautifulSoup4


# In[ ]:




