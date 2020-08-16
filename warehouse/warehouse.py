""""
     Program: warehouse management system
     Author Christian Mercado Astarita
     Description: Warehouse Project
     
     Tasks:
     1. Register new item
        id (auto generated)
        title(str)
        category (str)
        price (float)
        stock(int)
        
    2. Display Catalog
    3. upstate stock
    4. Remove item from catalog
    5. Print total stock value
    6. Report- Out of stock
    
    """

# imports
from menu import clear, print_menu, print_header, print_item
from item import Item
import pickle

# global vars
catalog = []
data_file = 'warehouse.data'
last_id = 1
# fn


def serialize_catalog():
    global data_file
    writer = open(data_file, 'wb')
    pickle.dump(catalog, writer)
    writer.close()  # close stream, release the file
    print("** Data serialized")


def deserialize_catalog():
    try:
        global data_file
        reader = open(data_file, 'rb')  # open file to Read Binary
        temp_list = pickle.load(reader)

        for item in temp_list:
            catalog.append(item)

        last_item = catalog[-1]
        last_id = last_item.id + 1
        print("** Deserialized " + str(len(catalog)) + " items")
    except:
        print("Error, could not load data")


def register_item():
    global last_id
    try:
        print_header("Register New Item")
        title = input("Please provide Title: ")
        cat = input("Please provide Category: ")
        price = float(input("Please provide Price: "))
        stock = int(input("Please provide Stock: "))

        id = last_id
        last_id += 1
        item = Item(id, title,  cat, price, stock)
        catalog.append(item)

        how_many = len(catalog)
        print("You now have : " + str(how_many) + "item(s) in the catalog ")

    except ValueError:
        print("Error, Please verify data input!")
    # except:
       # print(" Error, something went wrong")


def display_catalog():
    print_header("Your Current Catalog")
    for item in catalog:
        print_item(item)


def display_out_of_stock():
    print_header("Items currently out of stock")
    for item in catalog:
        if (item.stock == 0):
            print_item(item)


def remove_item():
    try:
        print_header("Remove Stock Item")
        display_catalog()
        id = input("Please provide ID to continue...")
        found = False
        for item in catalog:
            if(str(item.id) == id):
                found = True
                val = input("Select item for deletion ")
            delete(item)

        if(not found):
            print("**Error: Invalid ID, verify and try again")

    except ValueError:
        print("Error, Please verify data input!")
    except:
        print(" Error, something went wrong")


def total_stock_value():
    total = 0.0
    for item in catalog:
        total += item.price * item.stock

        print("Total value:  " + str(total))
        # for i in range(0, 20):


def update_stock():
    try:
        print_header("Update stock value")
        display_catalog()
        id = input("Please provide ID to continue...")
        found = False
        for item in catalog:
            if(str(item.id) == id):
                found = True
                val = input("Please provide new stock value(s) ")
                item.stock = int(val)
                print("Stock value updated")

        if(not found):
            print("**Error: Invalid ID, verify and try again")

    except ValueError:
        print("Error, Please verify data input!")
    except:
        print(" Error, something went wrong")


def update_price():
    try:
        print_header("Update Price")
        display_catalog()
        id = input("Please provide ID to continue...")
        found = False
        for item in catalog:
            if(str(item.id) == id):
                found = True
                val = input("Please provide new Price value(s) ")
                item.price = int(val)
                print("Price updated")

        if(not found):
            print("**Error: Invalid ID, verify and try again")

    except ValueError:
        print("Error, Please verify data input!")
    except:
        print(" Error, something went wrong")


def list_of_categories():
    print_header("Items duplication removed")
    for item in catalog:
        do_not_duplicate(item)


# instuctions


deserialize_catalog()
input("Press Enter to continue...")

opc = ''
while(opc != 'x'):
    clear()
    print_menu()

    opc = input('Please choose an option:  ')

    if(opc == '1'):
        register_item()
        serialize_catalog()
    elif (opc == '2'):
        display_catalog()
    elif (opc == '3'):
        update_stock()
        serialize_catalog()
    elif (opc == '4'):
        remove_item()
    elif (opc == '5'):
        update_price()
    elif (opc == '6'):
        display_out_of_stock()
    elif (opc == '7'):
        total_stock_value()
        serialize_catalog()
    elif (opc == '8'):
        list_of_categories()

    input("Press enter to continue...")
