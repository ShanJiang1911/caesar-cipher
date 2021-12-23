import re

def encrypt(plain, key):
    encrypted_text = ""

    for i in range(len(plain)):
        char = plain[i]
        matchObj = re.search('[a-zA-Z]', char)
        if not matchObj:
            encrypted_text += char
        elif(char.isupper()):
            encrypted_text += chr((ord(char) + key - 65)%26 + 65)
        else:
            encrypted_text += chr((ord(char) + key - 97)%26 + 97)
            
    return encrypted_text

def decrypt(encoded, key):
    return encrypt(encoded, -key)


if __name__ == "__main__":
    words = [
        "zzz",
        "Hi there!",
        "abcd",
        "SUN",
        "moon",
        "It was the best of times, it was the worst of times.",

    ]

    for word in words:
        key = 27
        print("plain word:", word)
        encrypted_word = encrypt(word, key)
        print("encrypted_word:", encrypted_word)
        decrypted_word = decrypt(encrypted_word, key)
        print("decrypted_word:", decrypted_word)