def contains_digits(word):
  for character in word:
    if character.isnumeric():
      return True
  return False

def contains_letters(word):
  for character in word:
    if character.isalpha():
      return True
  return False

def validate_password(password):
  if not contains_letters(password) or not contains_digits(password):
    return False
  else:
    return True

password = input("Enter your password here: ")
if validate_password(password) == True:
  print("Password correct")
else:
  print("Incorrect password")
