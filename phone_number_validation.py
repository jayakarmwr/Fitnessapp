import re
def phone():
    n=input('Enter your phone number:+91 ')
    if not re.match('[7-9]{1}[0-9]{9}', n):
        print("Invalid number.Try again")
        return phone()
    else:
        return n

s=phone()
print(s)
