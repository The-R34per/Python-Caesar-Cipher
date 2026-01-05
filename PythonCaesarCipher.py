def caesar_encrypt(text: str, shift: int) -> str:
    result = []
    for ch in text:
        if 'A' <= ch <= 'Z':
            base = ord('A')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        elif 'a' <= ch <= 'z':
            base = ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return "".join(result)

def caesar_decrypt(text: str, shift: int) -> str:
    return caesar_encrypt(text, -shift)


if __name__ == "__main__":
    while True:
        print("\n" + "="*30)
        print("CAESAR CIPHER TOOL")
        print("1. Encrypt message")
        print("2. Decrypt message") 
        print("3. Quit")
        print("="*30)
        
        choice = input("Choose option (1/2/3): ").strip()
        
        if choice == '3':
            print("\nThanks for using Caesar Cipher!")
            break
        
        message = input("Enter your message: ").strip()
        
        if choice in ['1', '2']:
            try:
                shift = int(input("Enter shift amount (1-25): ").strip())
                if 1 <= shift <= 25:
                    if choice == '1':
                        result = caesar_encrypt(message, shift)
                        print(f"Encrypted: {result}")
                    else:
                        result = caesar_decrypt(message, shift)
                        print(f"Decrypted: {result}")
                else:
                    print("Shift must be 1-25!")
            except ValueError:
                print("Enter a valid number for shift!")
        else:
            print("Invalid choice! Pick 1, 2, or 3.")
        
        print("-" * 40)
