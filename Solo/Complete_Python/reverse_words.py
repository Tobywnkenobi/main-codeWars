'''

'''

def reverse_words(s: str) -> str:
    return ' '.join(word[::-1] for word in s.split(' '))

print(reverse_words("This is an example!")) 
print(reverse_words("double  spaces"))  