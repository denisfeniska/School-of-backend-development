def high(x):
  max_sum = 0
  res_word = x.split()[0]
  for word in x.split():
    cur_sum = 0
    for letter in word:
      cur_sum += ord(letter) - 96
    if cur_sum > max_sum:
      max_sum = cur_sum
      res_word = word
  return res_word
  

print(high('man i need a taxi up to ubud'))
