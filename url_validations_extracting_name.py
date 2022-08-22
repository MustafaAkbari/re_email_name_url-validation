import  re
url = input("what's the url? ").strip().lower()

user_name = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"User_name: {user_name}")