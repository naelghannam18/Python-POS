import Item
import sqlite3
import os

# Creating our Database.
# Note That not all the methods are used in the main Activity.
# They are just written for demonstration purposes.

# Creating a Variable Holding The name of the Database to prevent miss-typing the database name.
DATABASE = 'items.db'
# First of all we Created a Function To Create a Database called items.db if it doesn't exist.
# This function will Create the database at First run or if the database is deleted.
# If The database already exists, the function will do nothing (pass)

def createDatabase():
    if os.path.isfile('items.db'):                      # Checks If the database File Exists or not.
        pass                                            # Do Nothing if the Database Already Exists.
    else:                                               # If The database doesn't exist we will Create a new one.
        # Creating a Connection to Our Database
        connection = sqlite3.connect('Items.db')
        # Creating a Cursor
        # The sqlite3. Cursor class is an instance using which you can invoke methods that execute SQLite statements.
        c = connection.cursor()

        # To Execute SQLite Queries we use the cursor's execute() Function.

        # The following is a Query That Creates a Table Called 'items' That will hold info about our created Items.
        # After The Line 'CREATE TABLE items', we are Creating the Columns that match the values of the parameters for items.

        # We made the Barcode a Primary Key because Primary Keys cannot have duplicates value, The same applies for item barcodes.
        # Every Primary key is unique Value Assigned to To Each row of the Database.

        c.execute("""CREATE TABLE items (
                     BARCODE INTEGER PRIMARY KEY,   
                     NAME TEXT,
                     CATEGORY TEXT,
                     BRAND TEXT,
                     QUANTITY INTEGER,
                     PRICE REAL,
                     SELLING_PRICE REAL,
                     DESCRIPTION TEXT
                     )""")

        # Next We Created another Table Called Cashier That will Store Basic Data Concerning the Incomes and outcomes and profits.
        # This Table Holds the values of the current balance as well as the expenses and profits.
        # For The sake of this project we will use one row representing one register.
        c.execute ("""CREATE TABLE cashier (
                             ID INTEGER PRIMARY KEY,
                             BALANCE REAL,
                             PAID REAL,
                             INCOME REAL,
                             PROFIT REAL
                             )""")

        connection.commit()     # Commiting The connection applies The Changes Done.
        connection.close()      # Connection should always be closed because one connection to a Table Can be done at a time.
        createCashRegister()    # This is a method that creates one cash register instance when the whole Database is Created.

# Function That Adds An Item to The 'items' table.
def addItem(item):
    try:
        # We always start by creating a connection to out database and Creating a cursor.
        connection = sqlite3.connect(DATABASE)
        c = connection.cursor()
        # Query That adds values To Each Column of the row.
        # Note that we don't use the f'' to format our Entries because this will make our function vulnerable for SQL Injection

        c.execute("INSERT INTO items VALUES (?,?,?,?,?,?,?,?)", (item.getBarcode(),         # Index 0
                                                                 item.getName(),            # Index 1
                                                                 item.getCategory(),        # Index 2
                                                                 item.getBrand(),           # Index 3
                                                                 item.getQuantity(),        # Index 4
                                                                 item.getPrice(),           # Index 5
                                                                 item.getSellingPrice(),    # Index 6
                                                                 item.getDescription()      # Index 7
                                                                 ))
        # We Always Commit and Close our connection to apply Changes and Close the connection.
        connection.commit()
        connection.close()
    # Notice That we Put Our code In Try/Except to listen for IntegrityError.
    # An IntegrityError Appears When We are Trying to add a duplicate value to an existing primary key which is the barcode.
    # This alleviates the Need for A Method That checks for Duplicate Barcodes.
    # But for The sake Of the Projects we also Created A method that checks for duplicate primary keys (barcodes)
    # If we are trying to add a barcode that already exists, the program will output a certain phrase instead of crashing.
    except sqlite3.IntegrityError:
        print("Barcode Already Exists!")

# This is the method we used in the createDatabase() function to create a register to hold the transaction information.
def createCashRegister():
    connection = sqlite3.connect(DATABASE)
    c = connection.cursor()
    # Creating one register with ID of 1 and zeros to all the other values.
    c.execute("INSERT INTO cashier VALUES (?,?,?,?,?)", (1, 0.0, 0.0, 0.0, 0.0))
    connection.commit()
    connection.close()

# This is a method related to the register.
# It is used everytime we add an item to our inventory (we Pay from the register)
def pay(amount):
    connection = sqlite3.connect(DATABASE)
    c = connection.cursor()

    # The 'UPDATE' Keyword updates an existing value in a certain row.
    # Note That we only Created one register with the ID of 1 so we are using the ID to locate our register in the database.

    # In other terms: Here we are telling SQLite That we want to update The "PAID" columns in the "cashier" table where the ID of the row is = 1.
    # Mathematically, PAID = PAID + Amount
    #                 BALANCE = BALANCE - amount
    #                 PROFIT = INCOME - PAID
    # These are illustrated in the Queries below.
    c.execute("UPDATE cashier SET PAID = PAID + ? WHERE ID = 1", (amount,))
    c.execute("UPDATE cashier SET BALANCE = BALANCE - ? WHERE ID = 1", (amount,))
    c.execute("UPDATE cashier SET PROFIT = INCOME - PAID WHERE ID = 1")

    connection.commit()
    connection.close()

# This is the same as the previous method but were getting an income instead of paying.
def purchase(amount):
    connection = sqlite3.connect (DATABASE)
    c = connection.cursor ()

    c.execute("UPDATE cashier SET INCOME = INCOME + ? WHERE ID = 1", (amount,))
    c.execute("UPDATE cashier SET BALANCE = BALANCE + ? WHERE ID = 1", (amount,))
    c.execute("UPDATE cashier SET PROFIT = INCOME - PAID WHERE ID = 1")

    connection.commit ()
    connection.close ()

# This function deletes an the item from the database and returns the money paid to the balance.
def returnItemToSupplier(barcode, amount):
    connection = sqlite3.connect (DATABASE)
    c = connection.cursor ()
    # Here we are telling SQLite to Delete The row From the Table items, where BARCODE = [barcode provided]
    c.execute ("DELETE FROM items WHERE BARCODE = ?", (barcode,))
    c.execute ("UPDATE cashier SET PAID = PAID - ? WHERE ID = 1", (amount,))
    c.execute ("UPDATE cashier SET BALANCE = BALANCE + ? WHERE ID = 1", (amount,))
    c.execute ("UPDATE cashier SET PROFIT = INCOME - PAID WHERE ID = 1")
    connection.commit ()
    connection.close ()

# Method to delete a Certain row from a Database.
# We are using the barcode as a search criteria Since it is unique to every item.
def deleteItem(barcode):
    connection = sqlite3.connect(DATABASE)
    c = connection.cursor()
    # Here we are telling SQLite to Delete The row From the Table items, where BARCODE = [barcode provided]
    c.execute("DELETE FROM items WHERE BARCODE = ?", (barcode,))
    connection.commit()
    connection.close()

# Method to Update a Certain Row in the DataBase
# This methods takes as parameters the new updated values and updates each column.
# This method works if we only want to modify one or two parameters.
def updateItem(barcode, name, category, brand, quantity, price, selling_Price, description):
    connection = sqlite3.connect(DATABASE)
    c = connection.cursor()

    c.execute("UPDATE items SET NAME = ? WHERE BARCODE = ?", (name, barcode))
    c.execute("UPDATE items SET CATEGORY = ? WHERE BARCODE = ?", (category, barcode))
    c.execute("UPDATE items SET BRAND = ? WHERE BARCODE = ?", (brand, barcode))
    c.execute("UPDATE items SET QUANTITY = ? WHERE BARCODE = ?", (quantity, barcode))
    c.execute("UPDATE items SET PRICE = ? WHERE BARCODE = ?", (price, barcode))
    c.execute("UPDATE items SET SELLING_PRICE = ? WHERE BARCODE = ?", (selling_Price, barcode))
    c.execute("UPDATE items SET DESCRIPTION = ? WHERE BARCODE = ?", (description, barcode))

    connection.commit()
    connection.close()

# Function that returns a tuple of tuples containing the info of each row.
def getItems():
    connect = sqlite3.connect (DATABASE)
    c = connect.cursor ()
    c.execute ("SELECT * FROM items")  # Selecting everything from the Table.
    items = c.fetchall ()              # Fetching everything from our selection and put them in a variable called items.
    # Notice here That we don't have to commit out connection since we did not change anything in the Database
    connect.close()
    return items

# Same as The preceding Function, but here we are getting a tuple containing one tuple of the item we are seeking per barcode.

def getItem(barcode):

    connect = sqlite3.connect (DATABASE)
    c = connect.cursor ()
    c.execute ("SELECT * FROM items WHERE BARCODE = ?", (str(barcode),))  # Selecting everything from the row that matches the barcode provided.

    item = c.fetchall()
    # We don't need to commit our connection here either.
    connect.close()
    return item

# Function That returns a list of all the barcodes present.
def getBarcodes():
    connect = sqlite3.connect (DATABASE)
    c = connect.cursor ()
    c.execute ("SELECT BARCODE FROM items")       # Selecting all the barcodes from the items table.

    items = c.fetchall ()                         # Fetching our selection
    connect.close()

    list_barcodes = [item[0] for item in items]   # Creating a List of the barcodes.

    return list_barcodes

# Function That returns if the provided barcode is used or not.
def isBarcodeUsed(barcode):
    connection = sqlite3.connect(DATABASE)
    c = connection.cursor()
    c.execute('SELECT 1 FROM items WHERE BARCODE = ? LIMIT 1', (barcode,))
    # If a match is found, then out query will return a non-empty String.
    # Else, It will return an empty String.
    tempBarcode = c.fetchall()
    # If The String is empty, then the barcode provided is not used and the function will return False.
    # If The String is not Empty, Then the barcode is used and the function will return True.
    return len(tempBarcode) != 0

# The following two Functions Increment and decrement the quantities of a certain Item when a customer buys or returns an item.
# Notice That the Queries are written with the f'' for formatting.
# This Type of query is vulnerable for SQLite Injection.
def incrementQuantity(barcode, quantity):
    connection = sqlite3.connect(DATABASE)
    c = connection.cursor()
    # THIS TYPE OF QUERY IS VULNERABLE TO SQL INJECTION
    c.execute(f"SELECT * FROM items WHERE BARCODE = {barcode} ")
    # TO AVOID SQL INJECTION THIS QUERY SHOULD BE WRITTEN IN THE FOLLOWING METHOD:
    # c.execute(f"SELECT * FROM items WHERE BARCODE = ? ", (barcode,))
    items = c.fetchall()
    # items will be equal to : ( (.....), ) A tuple Containing one tuple holding the info of the item returned by the query.
    # The first index [0] indicates the first tuple in the main tuple.
    # The Index [4] indicates the fifth item in the first tuple of the main tuple which contains the quantity of a certain item.
    currentQuantity = items[0][4]
    # Adding the Quantity to our new Quantity.
    newQuantity = int(currentQuantity) + int(quantity)
    # Updating The Quantity in the Database into our new Quantity.
    c.execute(f"UPDATE items SET QUANTITY = {newQuantity} WHERE BARCODE = {barcode}")
    # The right way to write the query would be:
    # c.execute("UPDATE items SET QUANTITY = ? WHERE BARCODE = ?", (newQuantity, barcode))
    connection.commit()
    connection.close()

def decrementQuantity(barcode, quantity):
    connection = sqlite3.connect(DATABASE)
    c = connection.cursor()
    c.execute(f"SELECT * FROM items WHERE BARCODE = {barcode} ")
    items = c.fetchall()
    currentQuantity = items[0][4]
    newQuantity = int(currentQuantity) - int(quantity)
    c.execute(f"UPDATE items SET QUANTITY = {newQuantity} WHERE BARCODE = {barcode}")
    connection.commit()
    connection.close()