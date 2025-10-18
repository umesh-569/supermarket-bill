from datetime import datetime

name = input("Enter your name: ")

# List of available items
items_list = '''
Rice             : 20 Rs/kg
Sugar            : 30 Rs/kg
Salt             : 20 Rs/kg
Oil              : 110 Rs/liter
Milk             : 70 Rs/liter
Groundnuts       : 70 Rs/kg
Wheat flour      : 55 Rs/kg
Dish wash liquid : 140 Rs/liter
Detergent        : 110 Rs/kg
Tea powder       : 480 Rs/kg
'''

# Dictionary of items and their prices
items = {
    'rice': 20,
    'sugar': 30,
    'salt': 20,
    'oil': 110,
    'milk': 70,
    'groundnuts': 70,
    'wheat flour': 55,
    'dish wash liquid': 140,
    'detergent': 110,
    'tea powder': 480
}

# Variable initialization
price_list = []
Total_price = 0

# Show list of items
option = int(input("For list of items press 1: "))
if option == 1:
    print(items_list)

# Buying process
while True:
    inp1 = int(input("\nPress 1 to buy items or 2 for bill: "))
    if inp1 == 2:
        break
    elif inp1 == 1:
        # Take multiple items in one input
        items_input = input("Enter item names (comma separated): ").lower().split(',')
        for item in items_input:
            item = item.strip()  # Remove extra spaces
            if item in items:
                quantity = int(input(f"Enter quantity for {item}: "))
                price = quantity * items[item]
                price_list.append((item, quantity, price))
                Total_price += price
            else:
                print(f"❌ {item} is not available.")
    else:
        print("⚠️ Invalid input!")

# Billing section
if Total_price > 0:
    gst = (Total_price * 5) / 100
    Final_price = Total_price + gst

    print("\n" + "=" * 25 + " Umesh Super Market " + "=" * 25)
    print(" " * 28 + "Wanaparthy")
    print("Name:", name, " " * 20, "Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("-" * 75)
    print("{:<10}{:<20}{:<15}{:<10}".format("S.No", "Item", "Quantity", "Price (Rs)"))
    print("-" * 75)

    for i, (item, qty, price) in enumerate(price_list, start=1):
        print("{:<10}{:<20}{:<15}{:<10}".format(i, item.title(), qty, price))

    print("-" * 75)
    print(f"{'Total Amount:':>60} Rs {Total_price}")
    print(f"{'GST (5%):':>60} Rs {gst}")
    print(f"{'Final Amount:':>60} Rs {Final_price}")
    print("-" * 75)
    print(" " * 25 + "Thanks for visiting!")
    print("-" * 75)
else:
    print("No items were purchased.")


            



    


