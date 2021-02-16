

#the below code was copied from https://github.com/prof-rossetti/intro-to-python/blob/master/projects/shopping-cart/README.md


products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

#end section of copied setup code
#print(products)


IDlist = []
for x in products:
    IDlist.append(str(x["id"]))

print("Welcome to Gusteau Grocery!")


shopping_cart = []

def shoppingaction():
    stillshopping = True
    firstitem = True

    while stillshopping:
        while firstitem:
            itemid = input("Please enter your product's unique ID: ")
            if itemid not in IDlist:
                print("Please make sure the ID you entered is correct. Please try again.")
            else:
                shopping_cart.append(itemid)
                firstitem = False

        itemid = input("Please enter another unique product ID or enter 'done' to review your cart: ")
        if itemid =='done' or itemid in IDlist:
            if itemid == "done":
                stillshopping = False
            else:
                shopping_cart.append(itemid)
        else:
            print("Please make sure the ID you entered is correct. Please try again.")

shoppingaction()

print('Your cart is displayed below:')

#grouping same products, totaling their instances
#for item in shopping_cart:
#    same_items = [item for item in shopping_cart if shopping_cart[int(item)]==int(item)]
#    print(same_items)


def showcart():
    for i in shopping_cart:
        for k in products:
            if i == str(k["id"]):
                productname = k["name"]
                itemprice = k["price"]

        print(f"+ {productname} ({itemprice})")




changing= True

while changing:
    showcart()
    happy = input("Do you wish to checkout? ('yes'/'no'):")
    if happy =="no":
        nextaction = input("Which change would you like to make? ('add'/'remove'):")
        if nextaction =="add":
            shoppingaction()
        elif nextaction=="remove":
            remid = input("Please enter the unique ID of the item you want to remove from your cart: ")
            if remid in shopping_cart:
                shopping_cart.remove(remid)
            elif remid not in shopping_cart:
                print("Please make sure the ID you entered is correct. Please try again.")
        else:
            print("Please enter either 'add' or 'remove'")

    elif happy =='yes':
        print("Checking out...")
        changing = False

    else:
        print("Please enter either 'yes' or 'no'")
