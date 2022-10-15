"""
Add bullet to each line in clipboard.
"""

import pyperclip


BULLET_CHAR = "*"

if __name__ == '__main__':
    text = str(pyperclip.paste())

    print("Original text:")
    print(text)

    lines = text.split('\n')
    bullets = list()
    for line in lines:
        bullet = f"{BULLET_CHAR} {line}"
        bullets.append(bullet)
    bulleted_text = "\n".join(bullets)

    print("Bulleted text:")
    print(bulleted_text)

    pyperclip.copy(bulleted_text)
