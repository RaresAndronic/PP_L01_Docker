with open('input.txt', "r") as f:
    text = f.read()
semnePunctuatie = ['"', ';', ':', '.', '?', '!', ',', '\'', '-', '[', ']', '(', ')']
rezultat = ""
for caracter in text:
    if caracter not in semnePunctuatie and not caracter.isdigit():
        rezultat += caracter
