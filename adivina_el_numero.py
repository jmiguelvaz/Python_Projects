import random

def run():
    vidas= 5
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input("elIge un numero: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            vidas -= 1
            print("Elige un numero mas alto")
        if numero_elegido > numero_aleatorio:
            print("Busca un numero mas bajo")
            vidas -= 1
        if vidas == 0:
            print("GAME OVER")
            break

        print("Tienes " + str(vidas) + " vidas")
        numero_elegido = int(input("Elige otro numero: "))
        
    if numero_elegido == numero_aleatorio:
        print("GANASTE!")
    

if __name__=="__main__":
    run()