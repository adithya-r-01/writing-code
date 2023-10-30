import csv
import pandas as pd
import altair as alt
from datetime import datetime as dt
import regex as re

curr_year = 1900
data_obj = []

world_pop = {
    1900: 1654000000,
    1910: 1750000000,
    1920: 1860000000,
    1930: 2070000000,
    1940: 2300000000,
    1950: 2516000000,
    1960: 2516000000,
    1970: 3712000000,
    1980: 4451000000,
    1990: 5288000000,
    2000: 6067000000,
    2010: 6858000000,
    2020: 7812000000
}

# with open('languages_3.csv', 'r') as f:
#     next(f)
#     reader = csv.reader(f)
#     for line in reader:
#       if line[0] in ['English', 'Chinese Mandarin']:
#         speakers = re.sub(r'[^\d\.]', '', line[1])
#         if line[2]:
#           curr_year = int(line[2])
#         data_obj.append({'language': line[0], 'Speakers': (int(speakers) * world_pop[curr_year]) / 100, 'year': curr_year})

# df = pd.DataFrame(data_obj)

# print(df)

# chart = alt.Chart(df).mark_line(interpolate='basis').encode(
#     x=alt.X('year:Q', axis=alt.Axis(title='Year', format='d')),
#     y=alt.Y('Speakers:Q', axis=alt.Axis(title='Total Speakers', labels=True)),
#     color='language'
# ).interactive()

# # Show the chart
# chart.save("Languages_Chinese_English.html")

second_languages = {
  'Spanish': 24,
  'French': 30,
  'German': 36,
  'Hindi': 44,
  'Arabic': 88
}

df = pd.DataFrame(second_languages.items(), columns=['Language', 'Weeks To Learn']).sort_values(by=['Weeks To Learn'])

chart = alt.Chart(df).mark_bar().encode(
    x=alt.X('Language', axis=alt.Axis(title='Language', labelAngle=0)),
    y=alt.Y('Weeks To Learn', axis=alt.Axis(ticks=False, labels=True)),
    text=alt.Text('Weeks To Learn', format='.10f')
).properties(
    width=800,
    height=400
).configure_axis(
    grid=False
)



chart.save("Languages_Second_Languages.html")
