# A variable called 'Inventory' with a dictionary containing items and their quantities.
inventory = {"Apples": 50, "Bananas": 5, "Cherries": 0, "Dates": 20, "Eggplant": 8}

# a 'for loop' is used to iterate through each item and its quantity in the 'inventory' dictionary.
for item, qty in inventory.items():
    # If the quantity of an item is less than or equal to 0, it prints that the item is out of stock. 
    if qty <= 0:
        print(f"{item} is out of stock")
        #If the quantity is less than 10, it prints that the item is low in stock along with the remaining quantity.
        #an 'elif' statement is used to handle multiple conditions. 
    elif qty < 10:
        print(f"{item} is low in stock ({qty} left)")
    #If the quantity is 10 or more, it does nothing (passes).
    else:
        pass

#script to run: python inventory-audit.py  
