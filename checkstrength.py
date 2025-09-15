import re
import getpass

def password_strength(password: str) -> tuple:
    score = 0
    feedback = []
    if len(password) >= 12:
        score += 30
    elif len(password) >= 8:
        score += 20
    else:
        feedback.append("Password to short (<8)")
    if re.search(r'[A-Z]', password):
        score += 10
    else:
        feedback.append("= add uppercase letter")
    if re.search(r'[a-z]', password):
        score += 10
    else:
        feedback.append("add lowercase letter")
    
    if re.search(r'\d', password):
        score += 10
    else:
        feedback.append("add number")
    
    if re.search(r'\W', password):
        score += 20
    else:
        feedback.append("add special character")
    weak_patterns = ["123456", "password", "qwerty"]
    if any(p in password.lower() for p in weak_patterns):
        score -= 20
        feedback.append("Hindari pola umum seperti 123456")

    # Level
    if score >= 70:
        level = "STRONG"
    elif score >= 40:
        level = "MEDIUM"
    else:
        level = "WEAK"
    
    return score, level, feedback

def main():
    password = getpass.getpass("Input password: ")
    score, level, feedback = password_strength(password)

    print(f"\n[+] score strength: {score}/100")
    print(f"[+] Level: {level}")
    if feedback:
        print("[!] feedback:")
        for f in feedback:
            print(f" - {f}")
    else:
        print("[!] Password very strong !")

if __name__ == "__main__":
    main()
