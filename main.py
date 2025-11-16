text = "python"
text_terbalik = ""

i = len(text) - 1
while i >= 0:
    text_terbalik += text[i]
    i -= 1

print(text_terbalik)