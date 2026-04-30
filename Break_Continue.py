# #BREAK
# contador = 1
# while contador <= 10:
#     if contador == 5:
#         break
#     print(contador)
#     contador += 1
# #-------------------------
# #BREAK EXEMPLO SENHA
# senha = ""
# while True:
#     senha = input("Digite a senha: ")
#     if senha == "1234":
#         print("Senha correta!")
#         break
#     else:
#         print("Senha incorreta. Tente novamente.")

# #-------------------------
# #CONTINUE PULAR NUMERO 2
# numero = 1
# while numero <= 5:
#     if numero == 2:
#         numero += 1
#         continue
#     print(numero)
#     numero += 1
# #-------------------------
#     #CONTINUE
# contador = 0
# while contador < 10:
#     contador += 1
#     if contador % 2 == 0:
#         continue
#     print(contador)
# #-------------------------
#     EXEMPLO PARA AULA
# numero = 0
# while numero < 10:  
#         numero += 1  
#         if numero == 3:  
#             continue  
#         if numero == 10:  
#             break
#         print (numero) 
#-------------------------
#ATIVIDADES BREAK_CONTINUE 29/04##

#ATIVIDADE 1 - BREAK
numero = 1
while numero <= 10:
    if numero == 7:
        break
    print(numero)
    numero += 1
#--------------------------
    #ATIVIDADE 2 - CONTINUE
numero = 1
while numero <= 10:
    if numero == 5:
        numero += 1
        continue 

    print(numero)
    numero +=1

#----------------------------
#ATIVIDADE 3 - pulando pares
numero = 1
while numero <= 20:
    if numero == 17:
      break
    if numero % 2 == 0:
        numero += 1
        continue    
    print(numero)
    numero += 1
    
#-----------------------------------------
#ATIVIDADE 4 - CADASTRO DE PRODUTOS
while True:
    produto = input("Digite o nome do produto: ou Fim para finalizar:")
    if produto.lower() == "Fim".lower():
        print("Cadastro Finalizado.")
        break

#------------------------------------------
#ATIVIDADE 5 -SOMA ATE 20
soma = 0
while True:
    numero = int(input("Digite um número: "))
    soma += numero
    if soma > 20:
        print("A soma ultrapassou 20. Programa encerrado.")
        break

#-------------------------------------------
 #ATIVIDADE 6
soma = 0
while True:
    numero = int(input("Digite um número: "))
    soma += numero
    if soma >50:
        print("A soma ultrapassou 50. Programa encerrado.")
        break

#-------------------------------------------
#ATIVIDADE 7 SISTEMA DE SENHA
senha = ""
while True:
    senha = input("Digite a senha: ")
    if senha.lower() == "teste".lower():
        print("ACESSO LIBERADO!")
        break
    else:
        print("Senha incorreta. Tente novamente.")

