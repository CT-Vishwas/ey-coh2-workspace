from string import punctuation
def password_mutator(base_word):
    for sym in punctuation:
        yield f"{base_word}{sym}"
        yield f"{base_word.capitalize()}{sym}"


for attempt in password_mutator("admin"):
    print(f"Testing: {attempt}")
    