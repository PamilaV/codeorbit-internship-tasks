SPECIAL_CHARS = "!@#$%^&*()-_=+[]{};:'\",.<>/?\\|`~"


def check_password(password):
    """Return a list of problems with the password (empty list = strong)."""
    problems = []

    if len(password) < 8:
        problems.append("Use at least 8 characters.")
    if not any(c.islower() for c in password):
        problems.append("Add a lowercase letter.")
    if not any(c.isupper() for c in password):
        problems.append("Add an uppercase letter.")
    if not any(c.isdigit() for c in password):
        problems.append("Add a number.")
    if not any(c in SPECIAL_CHARS for c in password):
        problems.append("Add a special character (e.g. !@#$%).")

    return problems


def main():
    password = input("Enter a password to check: ")
    problems = check_password(password)

    if not problems:
        print("Strong password! 💪")
    else:
        print("Weak password. To improve it:")
        for tip in problems:
            print(f"  - {tip}")


if __name__ == "__main__":
    main()