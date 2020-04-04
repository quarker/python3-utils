import string

# translate punctuations to spaces, and uppercase to lowercase
translation_table = str.maketrans(string.punctuation + string.ascii_uppercase, ' ' * len(string.punctuation) +
                                  string.ascii_lowercase)

text = 'Hello World, My name is: Dao Nguyen.'
res = text.translate(translation_table)

words = res.split()
print(words)