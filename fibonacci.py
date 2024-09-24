

num = int()
def fibonacci(num): #essa função cria e verifica ao mesmo tempo se o numero seguinte é igual ao número digitado
    a,b = 0,1 #a é o primeiro número e b é o próximo da sequencia
    i=0
    while (num>b):
        a,b = b, a+b # a = b e b = a+b
    if (num==b):
        print("Esse número pertence a sequência de fibonacci")
    else:
        print("Esse número não pertence a sequência de fibonacci")

#laço principal com tratamento de exceções
while True:
    try:
        print("insira um numero:")
        num= int(input())
        if (num==0):
            print("Esse número pertence a sequência de fibonacci")
        fibonacci(num)
        break
    except ValueError:
        print("Caractere não permitido.")