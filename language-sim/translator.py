# from essential_generators import DocumentGenerator
# from translate import Translator

# src = 'en'
targs = ['zh', 'de', 'it', 'fr', 'es', 'ru']
# scores = [0, 0, 0, 0, 0, 0]

# for targ in targs:
#     for _ in range(10):
#       gen = DocumentGenerator()
#       actual = gen.sentence()
#       translator = Translator(to_lang=targ, from_lang=src)
#       translation = translator.translate(actual)
#       translator = Translator(to_lang=src, from_lang=targ)
#       predict = translator.translate(translation)
#       if actual == predict:
#           scores[targs.index(targ)] += 1
#       # show program progess in console as progress bar
#       print(f'{targs.index(targ) + 1}/{len(targs)}', end='\r')

# print(targs)
# print(scores)

# plot results
scores = [0, 2, 2, 1, 1, 0]
scores = [score / 10 for score in scores]
import matplotlib.pyplot as plt
plt.bar(targs, scores)
plt.show()
