prices={"batata":10, "tamata": 20, "kela": 5}

print("Price of batata is 10 Rs./Kg")
print("Price of tamata is 20 Rs./Kg")
print("Price of kela is 5 Rs./Kg")

a=int(input("How many batata you want to buy: "))
b=int(input("How many tamata you want to buy: "))
c=int(input("How many kela you want to buy: "))

bill={}

total=a*prices["batata"]+b*prices["tamata"]+c*prices["kela"]

print("You have to pay", total, "Rs.")
