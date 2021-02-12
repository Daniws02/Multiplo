a = float(input("Digite o 1º valor: "))
b = float(input("Digite o 2º valor: "))
def resultado(x):
 if multiplo(x):
  return("é multiplo")
 else:
  return("não é multiplo") 
def multiplo(x):
 return(a%b==0)
print(resultado(a))
