def prime_number(number):
    counter = 0

    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue
        if number % i ==0:
            counter += 1
    if counter == 0:
        return True
    else:
        return False        



def run():
    number = int(input("please type a number: "))
    if prime_number(number):
        print("it is a prime number")
    else:
        print("it is  not a prime number)")





if __name__=="__main__":
    run()