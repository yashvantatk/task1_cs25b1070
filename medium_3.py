def decode_mars_message(encoded_message):
   """
   Decodes a progressively shifted string.
   The i-th letter is shifted backwards by i positions in the alphabet.
   """
   # Convert all characters to uppercase
   encoded_message = encoded_message.upper()
   decoded_message = ""


   # enumerate() gives us the index (0, 1, 2...) and the character itself
   for index, char in enumerate(encoded_message):
       # The shift amount is 1-based (1, 2, 3...), so we add 1 to the 0-based index
       shift = index + 1


       # get the ASCII number of the letter using ord
       # We subtract 65 to normalize it to 0-25, subtract the shift,
       # use % 26 to manage if it goes below 0, and add 65 back.
       decoded_ascii = (ord(char) - 65 - shift) % 26 + 65


       # Convert the ASCII number back to a character and add to string
       decoded_message += chr(decoded_ascii)


   return decoded_message


if __name__ == "__main__":
   message = str(input("Enter a message: "))
   print(f"Encoded: '{message}' -> Decoded: '{decode_mars_message(message)}'")