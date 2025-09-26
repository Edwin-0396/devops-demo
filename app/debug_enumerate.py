def nth_char(words):
    return ''.join(word[i] for i, word in enumerate(words))

words = ["yoda", "best", "has"]

for i, word in enumerate(words):
    print(f"i={i}, word={word}, word[i]={word[i]}")

print("Result:", nth_char(words))
