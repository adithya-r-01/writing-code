import matplotlib.pyplot as plt

lang_codes = ['English', 'Chinese', 'Spanish', 'French', 'Greek', 'Portuguese', 'German', 'Italian']
lang_count = [56813, 444, 824, 3572, 220, 624, 2136, 939]

# build visualization with exponential axis
fig, ax = plt.subplots()
ax.bar(lang_codes, lang_count)
ax.set_title('Number of Books in Top 8 Languages')
ax.set_xlabel('Language')
ax.set_ylabel('Number of Books')
plt.yscale('log')
plt.show()
