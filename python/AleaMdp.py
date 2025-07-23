#Mot de passe aleatoire
import random
import string
mdpLong=int(input("Donnez la longueur du mot de passe : "))
mdp=''.join(random.choice(string.ascii_letters) for _ in range(mdpLong))
print("Votre mot de passe : ",mdp)