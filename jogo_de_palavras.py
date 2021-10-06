'''
criando um joguinho de palavras
-- v.beta
'''
from rich import print

palavra_secreta = "coragem"
digitado = []
vida = 3

while True:
    if vida <= 0:
        print("Você perdeu")
        break

    usuario = input("Digite uma letra: ")
    if len(usuario) > 1:
        print("[bold red]Digite apenas uma letra[/]")
        continue
    digitado.append(usuario)

    if usuario in palavra_secreta:
        print(f"A letra '{usuario}' existe na palavra secreta")

    elif usuario not in palavra_secreta:
        print(f"A letra '{usuario}' não existe na palavra secreta")
        digitado.pop()
        vida += - 1
        print(f"Você ainda tem '{vida}' vidas")

    palavra_secreta_criptografada = ''
    for uma_variavel in palavra_secreta:
        if uma_variavel in digitado:
            palavra_secreta_criptografada = palavra_secreta_criptografada + uma_variavel
        else:
            palavra_secreta_criptografada = palavra_secreta_criptografada + "*"
    print(palavra_secreta_criptografada)
    if palavra_secreta_criptografada == palavra_secreta:
        print('você venceu!')
        break
