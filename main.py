from facebook_extract import *
import matplotlib.pyplot as plt
import pandas as pd

#Please replace with your user token - usually lasts for about 1 hour
token = "EAACEdEose0cBAEVE5qWZC4A0NBI3El7qYA9nIxbJUc64RsZADpr3jLZAeXbMDZA20SbSStCk8AshDyZC57QbV84gwogn2yqLqcqVovV9rqFTZAoniSrfZCuUNcYim2b7hhkd6ffoQwnpi9ZBHlI8kZAZBKCyupeJyHjZALZBeWl0lADiQefiWbxiNdNEx6xUGxffOysZD"

#will bring back a json item.
results = req_facebook("me?fields=friends{name,photos{created_time,likes.summary(true)}},photos{likes.summary(true)}", token)

#will clean the json item and put it in a pandas dataframe
data = pd.DataFrame(list(clean_data(results).items()), columns=['time', 'likes'])
#checking the time type
print(type(data['time']))

#will change time type to only HMS
data['time'] = pd.to_datetime(data['time']).dt.time

#index time as the x axis
data.index = data['time']

#delete the duplicate column
del data['time']

print(data)

#plot data using matplotlib libraries
data.plot()

#show plot
plt.show()
