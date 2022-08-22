import re
email = input("what is your email: ").strip()

# if re.search(r"^[a-zA-Z0-9\.]+@\w+\.(com|org|net|edu)$", email, re.IGNORECASE):
# if re.search(r"^\w+@\w+\.(com|org|net|edu)$", email, re.IGNORECASE):
# if re.search(r"^\w+@(\w+\.)?\w+\.(com|org|net|edu)$", email, re.IGNORECASE) # allowing dot in email right side
if re.search(r"^(\w+\.)?\w+@(\w+\.)?\w+\.(com|org|net|edu)$", email, re.IGNORECASE):  # allowing dot in email both side
    print("Valid")
else:
    print("Invalid")


