#Calculatrice
x=float(input("Donnez nombre1: "))
y=float(input("Donnez nombre2: "))
operator=str(input("Donnez l'operateur: "))
evaluation=f"{x}{operator}{y}"
print(eval(evaluation))