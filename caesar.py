def caesar(text, shift, decrypt=False):
    """Encrypt or decrypt text with a Caesar cipher."""
    if decrypt:
        shift = -shift
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)  # keep spaces, digits, punctuation
    return "".join(result)


def get_shift():
    while True:
        try:
            return int(input("Enter shift value (key): "))
        except ValueError:
            print("Please enter a whole number.")


def main():
    print("=== Caesar Cipher Encryption Tool ===")
    while True:
        print("\n1. Encrypt\n2. Decrypt\n3. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "3":
            print("Goodbye!")
            break
        if choice not in ("1", "2"):
            print("Invalid choice.")
            continue

        text = input("Enter your text: ")
        shift = get_shift()

        if choice == "1":
            encrypted = caesar(text, shift)
            print(f"\nOriginal : {text}")
            print(f"Encrypted: {encrypted}")
        else:
            decrypted = caesar(text, shift, decrypt=True)
            print(f"\nEncrypted: {text}")
            print(f"Decrypted: {decrypted}")


if __name__ == "__main__":
    main()