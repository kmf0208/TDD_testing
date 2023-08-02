def estimate_reading_time(word):
    if word == "":
        raise Exception("sorry it is an empty string")
    text = word.split()
    return len(text) / 200