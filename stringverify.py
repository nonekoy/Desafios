

def verify(wordGet,letterGet):
    formatedWord = wordGet.upper()
    formatedLetter = letterGet.upper()
    sum=0
    for i in formatedWord:
        if i== formatedLetter:
            sum+=1
    print("essa letra aparece um total de",sum, "vezes na palavra/frase")

word = str
letter = str
while True:
    try:
        print("entre uma palavra ou frase")
        word = input()
        if not word.replace(" ","").isalpha():
            raise ValueError("Caractere não permitido")
        print("entre uma letra a ser pesquisada")
        letter = input()
        if len(letter)!=1 or not letter.isalpha():
            raise ValueError("Caractere não permitido")
        verify(word,letter)
        break
    except ValueError as e:
        print(e)