# Anh Vu
# Prof. Wright
# Assignment6
# Notes
# inputString: passing input from user to the function to do morse code translation
# words: the string to be encoded or decoded' 
# '''

MORSE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 
  
# Function to encrypt the string 
# according to the morse code chart 
def translate(words): 
    inputString = '' 
    for letter in words:  
        if letter != ' ': 
  
            # reverse english letter into morse code that's corresponding with the dictionary
            # seperate letter by a space
            inputString += MORSE_DICT[letter] + ' '
        else:
            #Handling space within input, could be more than 1 word
            inputString += ' '
  
    return inputString

words = input()
result = translate(words.upper())
print (result)
