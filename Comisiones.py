name=input("please type your name: ")
sale=int(input("how much did you sell this month?:$"))
comision=round(sale*0.13,2)
print("Hello, {} your sales comission for this month is: ${} thank your for your hard work".format(name,comision))