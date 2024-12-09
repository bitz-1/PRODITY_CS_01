def ceasar_cipher(text , shift , mode= "encrpyt"):
    
    if mode =="decrypt":
        shift = - shift 
    
    processed_text = ""
    for char in text :
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            processed_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else :
             processed_text += char 
    return processed_text

if __name__ == "__main__":
    text = input ("Enter your message :")
    shift = int (input ("Enter the shift value (integer):"))
    mode = input ("would you like to 'encrypt' or 'decrypt' the message ? ").strip().lower()
    
    if mode not in ["encrypt", "decrypt"]:
        print ("Invalid Choice ! please choose 'encrypt' or 'decrypt' ")
    else :
        result = ceasar_cipher(text,shift ,mode)
        print (f"Result : {result}")