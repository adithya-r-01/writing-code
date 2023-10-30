import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

top_10 = ['eng', 'cmn', 'hin', 'spa', 'arb']

# keep rows in df where column 'ISO_1' and 'ISO_2' are in top_10
df = pd.read_table('language_sim.tsv')
df = df[df['ISO_1'].isin(top_10)]

pivot_table = df.pivot(index='LangName_1', columns='LangName_2', values='Similarity')
pivot_table = pivot_table.drop(['Chinese', 'Tok Pisin', 'Wymysorys', 'Saterfriesisch', 'Standard Malay'], axis=1)
col_names = pivot_table.columns.tolist()
np.random.shuffle(col_names)
pivot_table = pivot_table[col_names]

pivot_table = pivot_table.dropna(axis=1, how='any')

fig, ax = plt.subplots()
im = ax.imshow(pivot_table.values)

for i in range(len(pivot_table.index)):
    for j in range(len(pivot_table.columns)):
        text = ax.text(j, i, "{:.2f}".format(pivot_table.values[i, j]), ha='center', va='center', color='w')

ax.set_xticks(range(len(pivot_table.columns)))
ax.set_xticklabels(pivot_table.columns)
ax.set_yticks(range(len(pivot_table.index)))
ax.set_yticklabels(pivot_table.index)
plt.setp(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
cbar = ax.figure.colorbar(im, ax=ax)

# show plot
plt.show()
