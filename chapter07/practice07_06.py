import re


if __name__ == "__main__":
    text = [
        "Batman",
        "Batwoman",
        "Batmobil",
        "Batwowoman",
    ]
    bat_regex = re.compile(r"Bat(wo)+man")
    for word in text:
        mo = bat_regex.search(word)
        if mo:
            print(mo.group())
