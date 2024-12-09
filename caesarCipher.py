def display_banner():
    """
    Displays a banner for the Caesar Cipher tool.
    """
    print("=" * 50)
    print(" " * 15 + "🔐 Caesar Cipher Tool 🔐")
    print("=" * 50)
    print("""
Welcome to the Caesar Cipher Tool!
This tool allows you to:
- Encrypt messages by shifting characters.
- Decrypt encrypted messages back to their original form.

👉 Supported Characters:
   - Letters (A-Z, a-z)
   - Non-alphabetic characters are not affected.
   - Developed by Apurv N (bitz)

Enjoy secure communication! 😊
    """)
    print("=" * 50)

def ceasar_cipher(text, shift, mode="encrypt"):
    """
    Encrypts or decrypts the text using the Caesar Cipher algorithm.
    :param text: Input text to process.
    :param shift: Number of positions to shift characters.
    :param mode: 'encrypt' or 'decrypt'.
    :return: Processed text.
    """
    if mode == "decrypt":
        shift = -shift

    processed_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            processed_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            processed_text += char
    return processed_text

if __name__ == "__main__":
    display_banner()

    text = input("Enter your message: ")
    shift = int(input("Enter the shift value (integer): "))
    mode = input("Would you like to 'encrypt' or 'decrypt' the message? ").strip().lower()

    if mode not in ["encrypt", "decrypt"]:
        print("❌ Invalid Choice! Please choose 'encrypt' or 'decrypt'.")
    else:
        result = ceasar_cipher(text, shift, mode)
        print("\n✨ Process Completed! ✨")
        print(f"{'🔒 Encrypted' if mode == 'encrypt' else '🔓 Decrypted'} Text: {result}")
