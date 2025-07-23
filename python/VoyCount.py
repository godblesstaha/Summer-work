# Compter les voyelles
phrase=str("Donnez votre phrase: ")
voyelles=["a","o","i","e","y","u","A","O","I","E","Y","U"]
total=sum(phrase.count(i) for i in voyelles)
print("Le nombre de voyelles est: ",total)