"""Coffee Machine program"""
def Report():
    # print Resource available
    for i in Resource:
        if i =="Water" or i=="Milk":
            print(f"{i}: {Resource[i]}ml")
        elif i=="Coffee":
            print(f"{i}: {Resource[i]}gm")
        else:
             print(f"{i}: {Resource[i]}$")
             
def check_resource(c):
    # To check if there are enough resource to make coffee
    for i in Resource:
        if i!="Money":
            if c[i]>Resource[i]:
                return i

def calculatesum():
    # Calculate sum of Coins entered
    print("Please enter coins.",end="\r")
    quarters=int(input("How many quarters?: "))*0.25
    dimes=int(input("How many dimes?: "))*0.10
    nickles=int(input("How many nickles?: "))*0.05
    pennies=int(input("How many pennies?: "))*0.01
    return quarters+dimes+nickles+pennies

def update_resources(c):
    # To update resouce after making coffee
    for i in c:
        if i!="Money":
            Resource[i]=Resource[i]-c[i]
        else:
            Resource[i]=Resource[i]+c[i]
    
Resource={"Water":300,"Milk":200,"Coffee":100,"Money":0}

Coffee={"espresso":{"Water":50,"Milk":100,"Coffee":18,"Money":1.5},
        "latte":{"Water":200,"Milk":150,"Coffee":24,"Money":2.5},
        "cappuccino":{"Water":250,"Milk":100,"Coffee":24,"Money":3.0}
        }

while True:
    inp=input("What would you like? (espresso/latte/cappuccino): ")
    if inp=="report":
        Report()
    elif inp=="espresso" or inp=="latte" or inp=="cappuccino":
        available=check_resource(Coffee[inp])
        if(available==None):
            sumofcoins=calculatesum()
            refund=float("{:.2f}".format(sumofcoins))
            if sumofcoins<Coffee[inp]["Money"]:
                print(f"Sorry that's not enough Money. {refund}$ refunded")
            elif sumofcoins>Coffee[inp]["Money"]:
                refund=sumofcoins-Coffee[inp]["Money"]
                refund=float("{:.2f}".format(refund))
                update_resources(Coffee[inp])
                print(f"Here is {refund}$ in change.\nHere is your {inp} ☕ Enjoy!")
                
            else:
                update_resources(Coffee[inp])
                print(f"Here is your {inp} ☕ Enjoy!")
        else:
            print(f"Sorry there is not enough {available}")
    elif inp=="off":
        break
    else:
        print("Invalid Choice")
        
        
    

