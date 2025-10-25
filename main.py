# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----', ',': '--..--',
    '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-'
}

# Reverse dictionary for decoding
MORSE_CODE_DICT_REVERSE = {v: k for k, v in MORSE_CODE_DICT.items()}

# Function to encode a message into Morse code
def encrypt(message):
    cipher = []
    for letter in message.upper():
        if letter != ' ':
            cipher.append(MORSE_CODE_DICT.get(letter, ''))
        else:
            cipher.append('')  # Empty string to separate words
    return ' '.join(cipher)

# Function to decode a Morse code message
def decrypt(message):
    words = message.strip().split('  ')  # Two spaces separate words
    decipher = []

    for word in words:
        letters = word.split()
        decoded_word = ''.join(MORSE_CODE_DICT_REVERSE.get(letter, '') for letter in letters)
        decipher.append(decoded_word)

    return ' '.join(decipher)

# Main function with user input
def main():
    choice = input("Do you want to encode (E) or decode (D)? ").strip().upper()

    if choice == 'E':
        text = input("Enter the text to encode: ")
        encoded = encrypt(text)
        print("Encoded:", encoded)

    elif choice == 'D':
        morse = input("Enter the Morse code to decode (use 2 spaces between words): ")
        decoded = decrypt(morse)
        print("Decoded:", decoded)

    else:
        print("Invalid choice. Use 'E' to encode or 'D' to decode.")

if __name__ == '__main__':
    main()
