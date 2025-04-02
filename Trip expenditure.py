def hotelcost(nights):
    return 140*nights
def planeridecost(city):
    if city == "Mexico":
        return 185
    elif city=="London":
        return 224
    elif city=="Hawaii":
        return 533
    elif city=="Vegas":
        return 480
    else:
        return "invalid option!"

def rentalcarcost(days):
    if days>=7:
        return 40*days-50
    elif days>=3:
        return 40*days-20
    else:
        return 40*days
    

def tripcost(city, days, spendingmoney):
    return rentalcarcost(days)+ hotelcost(days) + planeridecost(city)+ spendingmoney

print("Total cost of car rental: ",rentalcarcost(6))

print("The total cost of the plane ride: ",planeridecost("Hawaii"))

print("Cost hotel room: ",hotelcost(4))

print("cost of the trip: ",tripcost("Hawaii",7,500))