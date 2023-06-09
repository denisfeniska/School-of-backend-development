def pig_it(text):
  new_text = ""
  for word in text.split():
    new_word = word[1:] + word[0] + "ay"
    if word.isalpha():
      new_text += new_word + " "
    else:
      new_text += word + " "
  return new_text.strip()


print(pig_it('Hello world !'))
