

#the below code was copied from https://github.com/prof-rossetti/intro-to-python/blob/master/projects/shopping-cart/README.md

from datetime import datetime
thisday = datetime.now()
receiptdate = thisday.strftime("%m/%d/%Y %H:%M")


products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50, "price_per":"item"},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99, "price_per":"item"},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49, "price_per":"item"},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99, "price_per":"item"},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99, "price_per":"item"},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99, "price_per":"item"},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50, "price_per":"item"},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25, "price_per":"item"},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50, "price_per":"item"},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99, "price_per":"item"},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99, "price_per":"item"},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50, "price_per":"item"},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00, "price_per":"item"},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99, "price_per":"item"},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50, "price_per":"item"},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50, "price_per":"item"},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99, "price_per":"item"},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50, "price_per":"item"},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99, "price_per":"item"},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25, "price_per":"item"},
    {"id":21, "name": "Organic Bananas", "department":"snacks", "aisle":"produce", "price":0.79,"price_per":"pound"}
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

print("---------------------------------")
print("Welcome to Gusteau's Grocery!")
print("---------------------------------")
print(" ")


shopping_cart = ["b"]

#def shoppingaction():
stillshopping = True


while stillshopping:
    if shopping_cart[0] == "b":
        itemid = input("Please enter your product's unique ID: ")
        if itemid not in IDlist:
            print("Please make sure the ID you entered is correct. Please try again.")
        else:
            shopping_cart[0] = itemid
            for item in products:
                if item["price_per"]=="pound":
                    namename = item["name"]
                    countpounds = True
                    while countpounds:
                        try:
                            numpounds = float(input(f"Please enter the number of pounds of {namename}: "))
                            countpounds = False
                            newpoundprice = float(item["price"])*numpounds
                            item["price"] = newpoundprice
                        except:
                            print("Please enter a number obove zero [ex. 4, 8.2].")




    else:
        itemid = input("Please enter another unique product ID or enter 'done' to review your cart: ")
        if itemid =='done' or itemid in IDlist:
            if itemid == "done":
                stillshopping = False
            else:
                shopping_cart.append(itemid)
                for item in products:
                    if item["price_per"]=="pound":
                        namename = item["name"]
                        countpounds = True
                        while countpounds:
                            try:
                                numpounds = float(input(f"Please enter the number of pounds of {namename}: "))
                                countpounds = False
                                newpoundprice = float(item["price"])*numpounds
                                item["price"] = newpoundprice
                            except:
                                print("Please enter a number obove zero [ex. 4, 8.2].")
        else:
            print("Please make sure the ID you entered is correct. Please try again.")

#shoppingaction()

print("---------------------------------")
print('Your cart is displayed below:')

#grouping same products, totaling their instances
#for item in shopping_cart:
#    same_items = [item for item in shopping_cart if shopping_cart[int(item)]==int(item)]
#    print(same_items)


#def showcart():
#    carttotal = 0
#    for i in shopping_cart:
#        for k in products:
#            if i == str(k["id"]):
#                productname = k["name"]
#                itemprice = k["price"]
#                carttotal = carttotal + float(itemprice)

#        print(f"+ {productname} ({itemprice})")





changing= True

while changing:
    carttotal = 0
    for i in shopping_cart:
        for k in products:
            if i == str(k["id"]):
                productname = k["name"]
                itemprice = k["price"]
                carttotal = carttotal + float(itemprice)
                itemprice = to_usd(itemprice)


        print(f"+ {productname} ({itemprice})")
    print(" ")
    happy = input("Do you wish to checkout? ('yes'/'no'):")
    if happy =="no":
        nextaction = input("Which change would you like to make? ('add'/'remove'):")
        if nextaction =="add":
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
                        for item in products:
                            if item["price_per"]=="pound":
                                namename = item["name"]
                                countpounds = True
                                while countpounds:
                                    try:
                                        numpounds = float(input(f"Please enter the number of pounds of {namename}: "))
                                        countpounds = False
                                        newpoundprice = float(item["price"])*numpounds
                                        item["price"] = newpoundprice
                                    except:
                                        print("Please enter a number obove zero [ex. 4, 8.2].")

                itemid = input("Please enter another unique product ID or enter 'done' to review your cart: ")
                if itemid =='done' or itemid in IDlist:
                    if itemid == "done":
                        stillshopping = False
                    else:
                        shopping_cart.append(itemid)
                        for item in products:
                            if item["price_per"]=="pound":
                                namename = item["name"]
                                countpounds = True
                                while countpounds:
                                    try:
                                        numpounds = float(input(f"Please enter the number of pounds of {namename}: "))
                                        countpounds = False
                                        newpoundprice = float(item["price"])*numpounds
                                        item["price"] = newpoundprice
                                    except:
                                        print("Please enter a number obove zero [ex. 4, 8.2].")
                else:
                    print("Please make sure the ID you entered is correct. Please try again.")
        elif nextaction=="remove":
            remid = input("Please enter the unique ID of the item you want to remove from your cart: ")
            if remid in shopping_cart:
                shopping_cart.remove(remid)
            elif remid not in shopping_cart:
                print("Please make sure the ID you entered is correct. Please try again.")
        else:
            print(" ")
            print("Please enter either 'add' or 'remove'")

    elif happy =='yes':
        print(" ")
        print("~ Checking out ~")
        print(" ")
        changing = False

    else:
        print(" ")
        print("Please enter either 'yes' or 'no'")

print("---------------------------------")
print("Gusteau's Grocery")
print("www.gusteausgrocery.com")
print("1999 Rue Ratatouille")
print("75002 Paris, France")
print("---------------------------------")
print(f"Checkout at: {receiptdate}")
print("---------------------------------")
print("Shopping cart:")
for i in shopping_cart:
    for k in products:
        if i == str(k["id"]):
            productname = k["name"]
            itemprice = to_usd(k["price"])


    print(f"+ {productname} ({itemprice})")
print("---------------------------------")
subtotal = to_usd(carttotal)
print(f"Subtotal: {subtotal}")
dcsalestax = .06
displaydcsales = "{:.0%}".format(dcsalestax)
carttax = carttotal*dcsalestax
displaytax = to_usd(carttax)
print(f"Sales tax ({displaydcsales}): {displaytax}")
carttotal = to_usd(carttax+carttotal)
print(f"Total: {carttotal}")
print("---------------------------------")
print("Merci, come back soon!")
print("---------------------------------")
