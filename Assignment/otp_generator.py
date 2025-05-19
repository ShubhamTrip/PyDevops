import secrets
import string

def generate_otp(length=6):
    # Digits only OTP (0-9)
    digits = string.digits
    otp = ''.join(secrets.choice(digits) for _ in range(length))
    return otp

if __name__ == "__main__":
    print("Secure OTP Generator")
    otp = generate_otp()
    print(f"Your OTP is: {otp}")
