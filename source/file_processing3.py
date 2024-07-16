import sys
import os


current_dir = sys.path[1]
config_path = os.path.join(current_dir, "config")

file_path = os.path.join(config_path, 'sample.txt')

f = open(file_path, 'r')
resp = f.read()
f.close()

words = resp.split()
a_words = []
c_words = []
for word in words:
    word = word.lower()
    if word.startswith('a'):
        a_words.append(word)
    elif word.startswith('c'):
        c_words.append(word)

print(f"A- words: {a_words}")
print(f"C- words: {c_words}")

a_word_path = os.path.join(config_path, 'a_words.txt')
c_word_path = os.path.join(config_path, 'c_words.txt')

f = open(a_word_path, 'w')
f.write("\n".join(a_words))
f.close()

f = open(c_word_path, 'w')
f.write("\n".join(c_words))
f.close()
