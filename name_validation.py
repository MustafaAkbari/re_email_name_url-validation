import re
name = input("what's your name? ").strip()
matches = re.search(f"^(.+), *(.+)$", name)
if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"Hello, {name}")
