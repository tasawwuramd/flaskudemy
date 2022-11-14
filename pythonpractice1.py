# replace vowels from string with x

def code_replace(mystring):
    outstring = list(mystring)
    print(outstring)
    for index,letter in enumerate(mystring):
        for vowels in 'aeiou':
            if letter.lower() == vowels:
                outstring[index]='x'
    print(''.join(outstring))
        

code_replace("This is a text string")