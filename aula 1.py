#print("Hello word")

#nome = input("Digite seu nome: ")
#idade = int(input("Digite sua idade: "))


#print("seu nome é:", nome)
#print("e sua idade é:", idade)

#num1 = int(input("digite o primeiro numero: "))
#num2 = int(input("digite o segundo numero: "))

#soma = num1 + num2
#print(soma)

#num1 = int(input("digite seu mumero: "))


#if num1 % 2 == 0:
#    print("esse numero é par!!")
#else:
#    print("seu numero é impar")

#for i in range(10):
    #print("voce q n consegui")

#contador = 10
#while contador > 0:
#   print("contador: ", contador)
#    contador -= 1
#    if contador == 0:
#        print("fogo!!")

# lista = ["josue","joão","arthur","misael","caio","mateus"]
# for item in lista:
#     print(item.capitalize())

#for i in range(2, 12, +2):
#    print(i)

def main():
    aluno = []
    nome = input("Digite o nome do aluno: ")


    notas = []
    for i in range(3):
        notas.append(float(input("Digite as notas do aluno: ")))

    media = sum(notas) / len(notas)
    aluno.append({"nome": nome,
                  "notas": notas,
                  "media": media
                  })
#    print(media)
    avaliar_aluno(media)

def avaliar_aluno(media):
    if media >= 7:
        print(f"aprovado!!")
    elif media >= 5:
        print("recuperação!!")
    elif media > 5:
        print("reprovado!!")

if __name__ == "__main__":
    main()
    while True:
        op = input("Deseja continuar? [S/N] ").upper()
        if op == "N":
            break
        elif op == "S":
            main()
        else:
            print("opção invalida")
