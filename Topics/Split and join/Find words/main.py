words = input().split(" ")
word_1 = [word for word in words if word.endswith("s")]
print("_".join(word_1))
