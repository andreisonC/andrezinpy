# CADASTRO #
from re import S 

print(' ')
print(' ')                                                 #INTRODUÇÂO#
print("Bem vindo ao site de estudos do Igor Torres")
print(' ')
print("Para começar faça o seu Cadastro ou login")
print("Caso já tenha não tenha cadastro, ensira as informações abaixo")
                                              #PEDINDO OS DADOS#
name = input("Insira seu nome: ")
serie = input("Sua série: ")
scool = input("Seu colégio: ")
ID = input("Sua matricula:(ex:123-123) ")
                                    #CONFERINDO A QUANTIDADE DE CARACTERES#
b = len(ID)
if  b == 6:
    print("Confira se os seus dados estão corretos!")
else:
    print("Reescreva sua matricula corretamente")
    ID = input("Sua matricula:(ex:123-123) ")
    b = len(ID)
    if  b == 6:
        print("Confira se os seus dados estão corretos!")
    else:
        print("Reescreva sua matricula corretamente")
        ID = input("Sua matricula:(ex:123-123) ")
        b = len(ID)
        if  b == 6:
            print("Confira se os seus dados estão corretos!")
        else:
            print("Reescreva sua matricula corretamente")
            
                                            #CONFERINDO OS DADOS#

print(name)
print(serie)
print(scool)
print(ID)
print("")
                                           #CONFIRMAÇÃO DOS DADOS#
a = input('Se seus dados estiverem corretos digite "S", caso não digite "N" ')
if  a == 's' :
    print("Seja bem vindo(a) ao site de estudos Igor QUI! ")
else:
    print("Por favor, refaça seus dados!")
                                            #REFAZEDO OS DADOS#
    name = input("nsira seu nome: ")
    serie = input("Sua série: ")
    scool = input("Seu colégio: ")
    ID = input("Sua matricula:(ex:123-123) ")
    print("Confira se os seus dados estão corretos!")
    print(name)
    print(serie)
    print(scool)
    print(ID)
    print("")  
    a = input('Se seus dados estiverem corretos digite "S", caso não digite "N" ')
    if  a == 's' :
        print("Seja bem vindo(a) ao site de estudos Igor QUI! ")
    else:
        print("Por favor, refaça seus dados!")
        print("Bem vindo ao site de estudos do Igor Torres")
        print("Para começar faça o seu Cadastro ou login")
        print("Caso já tenha não tenha cadastro, ensira as informações abaixo")
                                              #PEDINDO OS DADOS PARA LOGIN#
print(" ")
print(" ")
print("Login:")
print(" ")
print(" ")

l = input("Insira seu nome: ")
FR = input("Insira novamente sua matricula ex:(123-123) ")
if l == name:
    print
else:
  print('Usuario não encontrado, por favor, faça um cadastro.')
        #CRIANDO UMA CONTA#
  
  AQ = input("Insira seu nome: ")
  SW = input("Sua série: ")
  DE = input("Seu colégio: ")
  FR = input("Sua matricula:(ex:123-123) ")
#CONFERINDO NOVAMENTE OS DADOS#

  print(AQ)
  print(SW)
  print(DE)
  print(FR)
  print("")

if FR == ID:
    print("Seja bem vindo de volta %s " %name )

#CABOU :D#
