import itemDatabase
# Creating "Item" Class
class Item:
    # The __init__ function creates an instance of the created class.
    def __init__(self, name, barcode, category, brand, quantity, price, sellingPrice, description):
        # To create a Class Parameter we use 'self' and then assign it to the passed value from the Function.
        self.name = name
        self.barcode = barcode
        self.category = category
        self.description = description
        self.brand = brand
        self.quantity = quantity
        self.price = price
        self.sellingPrice = sellingPrice

        # Here We Are using the Create Item From The Database file,
        # So that every time an object is created it is automatically added to the database
        itemDatabase.addItem (self)

# Defining setters and getters.
# A Setter Sets a value of a certain class object.
# A Getter Gets a value of a certain class object.
# Note That Since We have a DataBase Running We don't really need any of these functions.
# But its a Good practice To Always write setters and getters

    def getName(self):                          # Function That returns the name of an item object.
        return self.name

    def setName(self, name):                    # Function That sets or changes the Name of an item Project
        self.name = name

    def getBarcode(self):                       # Function That returns the Barcode of an Item Object
        return self.barcode

    def setBarcode(self, barcode):              # Function That sets or changes the Barcode of an item Project
        self.barcode = barcode

    def getCategory(self):                      # Function That returns the Category of an Item Object
        return self.category

    def setCategory(self, Category):            # Function That sets or changes the Category of an item Project
        self.category = Category

    def getDescription(self):                   # Function That returns the Description of an Item Object
        return self.description

    def setDescription(self, description):      # Function That sets or changes the Description of an item Project
        self.description = description

    def getBrand(self):                         # Function That returns the Brand of an Item Object
        return self.brand

    def setBrand(self, brand):                  # Function That sets or changes the Brand of an item Project
        self.brand = brand

    def getQuantity(self):                      # Function That returns the Quantity of an Item Object
        return self.quantity

    def setQuantity(self, quantity):            # Function That sets or changes the Quantity of an item Project
        self.quantity = quantity

    def getPrice(self):                         # Function That returns the Price of an Item Object
        return self.price

    def setPrice(self, price):                  # Function That sets or changes the Price of an item Project
        self.price = price

    def getSellingPrice(self):                  # Function That returns the Selling Price of an Item Object
        return self.sellingPrice

    def setSellingPrice(self, sellingPrice):    # Function That sets or changes the Selling Price of an item Project
        self.sellingPrice = sellingPrice
