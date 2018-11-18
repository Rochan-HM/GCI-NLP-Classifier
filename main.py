import analysis


# quote = 'hello world. This is C++'
# testing = analysis.sentiment(quote)
# print(testing)
quote = input("Please enter string: ")
res = analysis.sentiment(quote)
tipe = res[0]
percent = res[1]
if percent <= 0.8:
    print("Neutral")
elif tipe == 'pos':
    print("Positive")
elif tipe == 'neg':
    print("Negative")