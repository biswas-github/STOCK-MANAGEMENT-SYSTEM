#this is a stock management software 
from controller import stockmanager
host="localhost"
user="root"
password=""
database="stocks"
# taking the database as stocks and table as items
print("...........................................................")
print(".................STOCK MANAGEMENT SYSTEM...................")
print("...........................................................")
print(". \n"*3)

choice="""
1. Add to stock
2. update the stock
3. retrive the stocks
4. delete the stocks
5. EXIT """
stock_obj=stockmanager(host,user,password,database)
while True:
    print(f"{choice}")
    select=int(input("Enter the choice : "))
    match select:
        case 1:
            # adding the items to the stocks 
            name=input("Enter the name of product")
            qty=input("Enter the name of quantity")
            price=input("Enter the name of Price")
            stock_obj.add(name,qty,price)


        case 2:
            # update the stocks 
            name=str(input("Enter the item to be updated :"))
            qty=int(input("Enter the quantity to be updated :"))
            price=int(input("Enter the price to be updated :"))
            stock_obj.update(name,qty,price)
           
        case 3:
            # retrive the stocks
            print(".......retriving all the data in table format.....")
            stock_obj.retrive_data()
        case 4:
            # delete  data from the stocks 
            name=input("Enter the name of the item to be deleted :")
            stock_obj.delete(name)
        case 5:
            print("Exiting ..........")
            break
        case __:
            print("...........INVALID INPUT ........")