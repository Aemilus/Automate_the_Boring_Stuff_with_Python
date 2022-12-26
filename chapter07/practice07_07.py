import re


if __name__ == "__main__":
    text = [
        "Batman",
        "Batwoman",
        "Batmobil",
        "Batwowoman",
    ]
    bat_regex = re.compile(r"Bat(wo){2}man")
    # bat_regex = re.compile(r"Bat(wo){1,2}man")
    # bat_regex = re.compile(r"Bat(wo){0,2}man")
    for word in text:
        mo = bat_regex.search(word)
        if mo:
            print(mo.group())
