#Somme
# x=input("Donnez le premier nombre: ")
# y=input("Donnez le deuxieme nombre: ")
# print("La somme de ",x," et ",y,"est ",int(x)+int(y))
#Pair ou impair
# nbr=float(input("Donnez un nombre: "))
# if(nbr%2 == 0 ):
#     print("Le nombre est pair")
# else:
#     print("Le nombre est impair")
#Nombres de 1 a 10
# for i in range(10):
#     print(i+1)
# Longueur d'une phrase
# phrase=input("Donnez une phrase: ")
# print("La longueur de la phrase est: ",len(phrase))
#Table de multiplication
# nbr=int(input("Donner le nombre : "))
# for i in range(10):
#     print(nbr," * ",i,"=",nbr*i)
#Max3
# max=float(input("Donnez nbr1 : "))
# nbr2=float(input("Donnez nbr2 : "))
# nbr3=float(input("Donnez nbr3 : "))
# if (nbr2>max):
#     max=nbr2
# if (nbr3>max):
#     max=nbr3
# print("Le plus grand nombre est ", max)
#Mot de passe aleatoire
# import random
# import string
# mdpLong=int(input("Donnez la longueur du mot de passe : "))
# mdp=''.join(random.choice(string.ascii_letters) for _ in range(mdpLong))
# print("Votre mot de passe : ",mdp)
#Convertisseur de devises
# montant=float(input("Donner le montant en Euro: "))
# taux=float(input("Donnez le taux de change: "))
# valeur=montant*taux
# print("Votre somme devient: ",valeur)
#Calculatrice
# x=float(input("Donnez nombre1: "))
# y=float(input("Donnez nombre2: "))
# operator=str(input("Donnez l'operateur: "))
# evaluation=f"{x}{operator}{y}"
# print(eval(evaluation))
# Comptet les voyelles
phrase=str("Donnez votre phrase: ")
voyelles=["a","o","i","e","y","u","A","O","I","E","Y","U"]
total=sum(phrase.count(i) for i in voyelles)
print("Le nombre de voyelles est: ",total)