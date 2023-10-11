
#Exercício 1: Escreva um programa que verifique se a palavra "python" está presente na string "Estou aprendendo Python".
 
frase  = "Estou aprendendo Python"
if "python" in frase:
   palavra = "Python"
   print(f"{palavra} está presente!") 
    



# exercício 2: Escreva um programa que peça ao usuário para digitar seu nome e verifique se o nome começa com a letra "A" (maiúscula ou minúscula).

name  =  input("Digite o seu nome")
if name.startswith("a") or name.startswith("A"):
     print(f'Existe a ou A em  {name}')


# Exercício 3: Escreva um programa que peça ao usuário para digitar uma senha e verifique se a senha contém pelo menos 8 caracteres.

senha = input("Digite uma senha -> ")
senha2 = len(senha)
if senha2 == 8  :
    print("Excelente, digitou uma boa quantidade de caractres")
 
else: 
     print("Coloque mais carcateres")

# # Exercício 4: Escreva um programa que peça ao usuário para digitar um número e verifique se o número é uma representação numérica (não contém letras ou símbolos).
n = input("123")
print(n.isnumeric())


# Exercício 5: Escreva um programa que peça ao usuário para digitar uma frase e conte quantas vezes a letra "a" (maiúscula ou minúscula) aparece na frase.

frase = input("Digite uma frase: ")
contador = frase.count("a")
print(f"A letra 'a' aparece {contador} vezes na frase.")



#Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
print("-"*30)

for x in str(input("Digite seu nome: ")):
   print(x)
for x in input("Digite seu nome: "):
   print(x)