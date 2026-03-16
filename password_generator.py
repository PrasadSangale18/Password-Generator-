import random
import string


def generate_password(length: int = 12, use_upper: bool = True,
                      use_digits: bool = True, use_symbols: bool = True) -> str:
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    return "".join(random.choice(chars) for _ in range(length))


def check_strength(password: str) -> str:
    score = 0
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1
    if len(password) >= 12: score += 1

    if score <= 2: return "Weak 🔴"
    if score == 3: return "Medium 🟡"
    if score == 4: return "Strong 🟢"
    return "Very Strong 💪"


def main():
    print("=" * 40)
    print("       🔐 Password Generator")
    print("=" * 40)

    try:
        length = int(input("Password length (default 12): ") or 12)
        upper   = input("Include uppercase? (y/n, default y): ").lower() != "n"
        digits  = input("Include digits?   (y/n, default y): ").lower() != "n"
        symbols = input("Include symbols?  (y/n, default y): ").lower() != "n"
        count   = int(input("How many passwords? (default 5): ") or 5)
    except ValueError:
        print("Invalid input. Using defaults.")
        length, upper, digits, symbols, count = 12, True, True, True, 5

    print("\n" + "=" * 40)
    print(f"  Generated {count} Password(s):")
    print("=" * 40)

    for i in range(1, count + 1):
        pwd = generate_password(length, upper, digits, symbols)
        strength = check_strength(pwd)
        print(f"  {i}. {pwd}  [{strength}]")

    print("=" * 40)


if __name__ == "__main__":
    main()
