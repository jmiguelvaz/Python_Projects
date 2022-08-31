
def converter(pesos_type, dolar_value):
    pesos =input("how many " + pesos_type + " do you have? : ")
    pesos = float(pesos)
    dolars = pesos/dolar_value
    dolars = round(dolars,2)
    dolars = str(dolars)
    print("You have $" + dolars + " US dolars" )

menu = """
Welcome to the curency converter 💲💲💲

1- Colombian pesos
2- Argentinian pesos
3- Mexican pesos

Choose an option's number: """

opcion = input(menu)

if opcion == "1":
   converter("Colombian pesos", 3875)

elif opcion == "2":
    converter("Argentinian pesos", 65)

elif opcion == "3":
    converter("Mexican pesos", 24)

else:
    print("Please choose an available option")
