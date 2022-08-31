
def run():
    LIMIT = 1000000

    counter = 0
    power_2 = 2**counter
    while power_2< LIMIT:
        print("2 to the power of " + str(counter) + " equals: " + str(power_2))
        counter = counter + 1
        power_2 = 2**counter


if __name__== "__main__":
    run()
