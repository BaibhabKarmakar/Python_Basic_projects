# User Inputs : 
u1 = input("Enter the input of user 1 : (snake , water or gun) : ")
u2 = input("Enter the input of user 2 : (snake , water or gun) : ")

# Defining the logic : 
def snake_water_gun(u1 , u2):
    u1 = u1.lower()
    u2 = u2.lower()

    if u1 == u2:
        return "Draw!"
    

    rules = {
        "snake" : "water",
        "water" : "gun",
        "gun" : "snake"
    }

    if rules[u1] == u2:
        return "user 1 wins!"
    else:
        return "user 2 wins!"

result = snake_water_gun(u1 , u2)
print(result)


      