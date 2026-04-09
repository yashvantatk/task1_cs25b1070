def decode_morse(morse_message):


   #Assumes letters are separated by 1 space, and words by 3 spaces.


   # The Morse Code
   morse_to_english = {
       '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
       '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
       '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
       '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
       '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
       '--..': 'Z', '.----': '1', '..---': '2', '...--': '3',
       '....-': '4', '.....': '5', '-....': '6', '--...': '7',
       '---..': '8', '----.': '9', '-----': '0',


       '.-.-.-': '.', '--..--': ',', '..--..': '?'
   }


   morse_message = morse_message.strip()


   # Split the message into words (separated by 3 spaces)
   morse_words = morse_message.split('   ')


   decoded_message = []


   for word in morse_words:
       decoded_word = ""
       # Split the word into individual Morse characters (1 space)
       morse_chars = word.split(' ')


       # Translate each character
       for char in morse_chars:
           #If it's invalid insert a '?'
           english_char = morse_to_english.get(char, '?')
           decoded_word += english_char


       # Add the translated word
       decoded_message.append(decoded_word)


   return decoded_message


if __name__ == "__main__":
   incoming_signal = str(input("Enter a message: "))
   print("Decoded Text:", decode_morse(incoming_signal))