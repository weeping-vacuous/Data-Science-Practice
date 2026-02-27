from matplotlib import pyplot as plt
import csv
from collections import Counter
import pandas as pd

plt.style.use("fivethirtyeight")

# with open('dataVisualization\\data.csv') as csv_file:
#     csv_reader=csv.DictReader(csv_file)

data = pd.read_csv('dataVisualization\\data.csv')
ids = data['Responder_id']
language_responses = data['LanguagesWorkedWith']

language_counter= Counter()

for response in language_responses:
    language_counter.update(response.split(';'))

languages = []
popularity = []
for item in language_counter.most_common(15):
     languages.append(item[0])
     popularity.append(item[1])

languages.reverse(),popularity.reverse()

plt.barh(languages,popularity,color="#008fd5",height=0.6)

plt.title('Most Popular Languages')
plt.xlabel('Popularity')


plt.tight_layout()
plt.show()



        
