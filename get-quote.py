import random

def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  # Original usage
  # last = len(quotes) - 1
  # rnd = random.randint(0, last)
  # print(quotes[rnd], end="")

  lines = 2
  quotes_sq = random.choices(quotes, k=lines)
  # print(*quotes_sq, sep='\n')
  print(*quotes_sq, end="")

if __name__== "__main__":
  primary()
