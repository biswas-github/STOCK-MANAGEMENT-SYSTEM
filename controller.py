import mysql.connector
def database_connector(host,user,password,database):
        mydb=mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if mydb.is_connected():
            print("db has been connnected")
        else:
            print("NOT CONNECTED")
        return mydb

class stockmanager:
    def __init__(self,host,user,password,database):
        self.host=host
        self.user=user
        self.password=password
        self.database=database
        # connect to database by calling the function
        self.mydb=database_connector(
        self.host,
        self.user,
        self.password,
        self.database)
        self.cursor=self.mydb.cursor()
    # adding to the stock
    def add(self,name,qty,price):
        #  now doing the sql
        sql="insert into items(name,qty,price) values(%s,%s,%s)"
        self.name=name
        self.qty=qty
        self.price=price
        self.cursor.execute(sql,(self.name,self.qty,self.price,))
        print(self.cursor.rowcount,"row(s) affected")
        self.mydb.commit()
        
    # updating the stocks 
    def update(self,name,qty,price):
        self.name=name
        self.qty=qty
        self.price=price
        sql="UPDATE items SET qty=%s,price=%s WHERE name=%s"
        self.cursor.execute(sql,(self.qty,self.price,self.name,))
        self.mydb.commit()
        print(self.cursor.rowcount," row(s) affected")
       
    
    
    # retrive all stocks 
    def retrive_data(self):
        try:
            query = "SELECT name, qty, price FROM items"
            self.cursor.execute(query)
            result = self.cursor.fetchall()  # Fetch all rows from the query result
            return result  # Return the data as a list of tuples
        except Exception as e:
            print(f"Error retrieving data: {e}")
            return []  # Return an empty list if
        
    #delete some data / some stocks 
    def delete(self,item_name):
        sql="DELETE FROM ITEMS WHERE name=%s"
        self.cursor.execute(sql,(item_name,))
        print(f"{self.cursor.rowcount} row(s affected)")
        self.mydb.commit()
    