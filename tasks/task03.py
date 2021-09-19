import re


texts = [
   "Hello, World!",
   "The world is mine",
   "Hello, how are you?"
]


def count_words():
  all_words = []

  for x in texts:
    words = x.lower().split(" ")
    all_words.extend(words)
  return all_words


def collect_words_frequencies(words):
  dictionary = {}

  if words is not None:
    for item in words:
      word = re.sub(r"[^a-zA-Z0-9]", " ", item)

      if word in dictionary:
        dictionary[word] = dictionary[word] + 1
      else:
        dictionary[word] = 1
    return dictionary
  else:
    return None


def find_first_occurrence(word):
  for i in range(len(texts)):
    words = texts[i].split(" ")
    for w in words:
      compare = re.sub(r"[^a-zA-Z0-9]", " ", w)
      if compare.lower() == word:
        return i


word = "word"
count = "count"
first_line = "first line"

print(f"{word:13}{count:7} {first_line:7}")
all_words = count_words()
dictionary = collect_words_frequencies(all_words)
for key, value in dictionary.items():
  number_line = find_first_occurrence(key)
  print(f"{key:7}{value:7} {number_line:7}")