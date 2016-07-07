import os

letters = "abcdefghijklmnopqrstuvwxyz"
reverse = {l: i for i, l in enumerate(letters)}

THIS_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

d = set()
with open(os.path.join(THIS_DIRECTORY, "words")) as f:
  for line in f:
    d.add(line.strip().lower())


def rot(word, i):
  w = ""
  word = word.lower()
  for l in word:
    current_i = reverse[l]
    current_i = (current_i + i) % len(letters)
    w += letters[current_i]
  return w


def solve(words):
  words = words.split(" ")
  solved = []
  for i in xrange(26):
    solved.append([])
    for word in words:
      solved[-1].append(rot(word, i))
    solved[-1] = tuple(solved[-1])

  suspected = set()
  for i, words in enumerate(solved):
    for w in words:
      if w in d:
        suspected.add(words)

  return solved, suspected
