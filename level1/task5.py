def palid_check(text):
    string = text
    if len(text) <= 1:
        return f"Is it palindrom ."
    elif text[0] == text[-1]:
        return palid_check(text[1:-1])
    else:
        return f"Is it not palindrom ."

print(palid_check(input("enter any word,phrase or sequence..")))
