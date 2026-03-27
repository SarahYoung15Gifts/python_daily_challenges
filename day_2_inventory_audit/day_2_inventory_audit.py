# A variable called 'Inventory' with a dictionary containing items and their quantities.
inventory = {"Apples": 50, "Bananas": 5, "Cherries": 0, "Dates": 20, "Eggplant": 8}

def get_inventory_alerts(items):
    alerts = []
    for item, qty in items.items():
        if qty <= 0:
            alerts.append(f"{item} is out of stock")
        elif qty < 10:
            alerts.append(f"{item} is low in stock ({qty} left)")
    return alerts


def main():
    for alert in get_inventory_alerts(inventory):
        print(alert)


if __name__ == "__main__":
    main()

#script to run: python inventory-audit.py  
