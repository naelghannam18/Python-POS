from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import itemDatabase
from Item import Item
from datetime import datetime

# This is The Code For The Main GUI.
# The screen is made of 3 screens: Main Screen, Sales Screen and Inventory Screen.
# The Inventory and Sales Screens are Coded as classes Because many functions are required within each screen.
# The Main Screen Is Simple And does not require any complex Coding so we didn't create it as a class.
# Notice That we have imported our previously coded classes alongside the tkinter module and datetime to use in the Screens.

# For The sake of not explaining each recurring tkinter widget, here's an explanation of each widget used:

"""
First of all, Every tkinter screen is an tk() instance which is like the main application window.
Every Window in The application is Divided into Frames. Frames are containers that belong to a main window.
Every Frame is positioned into the main window. And in it, is positioned other widgets.

tkinter provides 2 positioning methods:

- pack() : Packs widgets either horizontally or vertically without the ability to freely manipulate in designs.
           Pack is Used When we don't have a lot of widgets. For example: Placing Frames in a window.
- grid() : The griding system, divides the window into rows and columns and gives much more flexibility with the design.

In this project we used pack() to pack Frames in a Window and used grid() to place different widgets inside Frames.

The Used Widgets are: 

- tkinter.Label : A label is a Container used to create Titles or outputting certain results.
                  It Also offers a lot of functionalities to manipulate text and fonts and label stats such as bg and fg.

- tkinter.Entry : As The Name suggests, an Entry is used to get User Input. We use the get() function to get its contents.  

- tkinter.ttk.ComboBox: A ComboBox is an entry that has a drop down list. we can also use get() method.

- tkinter.Listbox : A ListBox is a text Container That outputs Data as a list and can be assigned an onClick method that is 
                    activated when a user clicks on a certain Entry in the listbox.

- tkinter.Text : A text is like Entry but can be used also to display formatted Text. (in The project we used it to output a receipt)

- tkinter.button: A button basically that is assigned a command. (function)
                 In every class we created functions and assigned them as commands for the buttons.

For every widget, we should pass a parent. (To which window belongs this widget)
For Example, The parent of the frames will be the main app window.
             The parent of Each widget will be the Frame That it belongs to.

Also Every widget Offers variety of configuration options.
we can either pass them directly: for Example:

thisLabel = Label(parentFrame, text="Hello World", State="disabled")

or create the Label and then use the Configure Button:

thisLabel = Label(parentFrame)
thisLabel.configure(text="hello World")

"""


class InventoryScreen:
    def __init__(self):
        self.appWindow = Tk ()  # Creating Main app Window
        self.appWindow.geometry ("1920x1080")  # Configuring Window Size.
        self.appWindow.title ("Inventory")  # Configuring window Title (The small text that appears on the top Left)

        # Creating the Frames
        editingFrame = Frame (self.appWindow, highlightbackground="Black", highlightthickness=1)
        viewFrame = Frame (self.appWindow, highlightbackground="Black", highlightthickness=1)
        viewFrameForEditing = Frame (self.appWindow, highlightbackground="Black", highlightthickness=1)
        headerFrame = Frame (self.appWindow, highlightbackground="Black", highlightthickness=1)

        # Configuring the Header frame
        self.label_header = Label (master=headerFrame,
                                   text="INVENTORY",
                                   font=("Arial Black", 32),
                                   bg="#34ebd8",
                                   fg="#FFFFFF").pack(fill=X)

        self.label_barcode = Label (editingFrame, text="Barcode:", font=("Calibri Bold Italic", 10))
        self.label_barcode.grid (column=0, row=0, pady=10, padx=10)
        self.entry_Barcode = Entry (editingFrame)
        self.entry_Barcode.grid (column=1, row=0, padx=10)

        self.label_Name = Label (editingFrame, text="Name:", font=("Calibri Bold Italic", 10))
        self.label_Name.grid (column=0, row=1, pady=10, padx=10)
        self.entry_Name = Entry (editingFrame)
        self.entry_Name.grid (column=1, row=1, padx=10)

        self.categories = ("", "INPUT DEVICE", "OUTPUT DEVICE", "STORAGE DEVICE", "PROCESSING DEVICE")

        self.label_Category = Label (editingFrame, text="Category: ", font=("Calibri Bold Italic", 10))
        self.label_Category.grid (column=0, row=3, pady=10, padx=10)
        self.comboBox_Category = ttk.Combobox (editingFrame, values=self.categories)
        self.comboBox_Category.grid (column=1, row=3, padx=12)

        self.label_Brand = Label (editingFrame, text="Brand:", font=("Calibri Bold Italic", 10))
        self.label_Brand.grid (column=0, row=2, pady=10)
        self.entry_Brand = Entry (editingFrame)
        self.entry_Brand.grid (column=1, row=2)

        self.label_Quantity = Label (editingFrame, text="Quantity:", font=("Calibri Bold Italic", 10))
        self.label_Quantity.grid (column=2, row=0, pady=10)
        self.entry_Quantity = Entry (editingFrame)
        self.entry_Quantity.grid (column=3, row=0)

        self.label_price = Label (editingFrame, text="Price:", font=("Calibri Bold Italic", 10))
        self.label_price.grid (column=2, row=1, pady=10)
        self.entry_Price = Entry (editingFrame)
        self.entry_Price.grid (column=3, row=1, padx=10)

        self.label_sellingPrice = Label (editingFrame, text="Selling Price:", font=("Calibri Bold Italic", 10))
        self.label_sellingPrice.grid (column=2, row=2, pady=10)
        self.entry_sellingPrice = Entry (editingFrame)
        self.entry_sellingPrice.grid (column=3, row=2, padx=10)

        self.label_Description = Label (editingFrame, text="Description:", font=("Calibri Bold Italic", 10))
        self.label_Description.grid (column=0, row=4, pady=10)
        self.text_Description = Text (editingFrame, height=10, width=50)
        self.text_Description.grid (column=1, row=4, pady=10, padx=10, rowspan=2, columnspan=4)

        self.addButton = Button (editingFrame, text="ADD ITEM", width=10, command=self.addItem)
        self.addButton.grid (row=6, column=0, columnspan=1, padx=10)
        self.ClearButton = Button (editingFrame, text="CLEAR", width=10, command=self.clearButton)
        self.ClearButton.grid (row=6, column=1, columnspan=1)
        self.updateButton = Button (editingFrame, text="UPDATE ITEM", state="disabled", width=10,
                                    command=self.updateButton)
        self.updateButton.grid (row=6, column=2, columnspan=1)
        self.deleteButton = Button (editingFrame, text="DELETE ITEM", width=10, command=self.deleteItem)
        self.deleteButton.grid (row=6, column=3, columnspan=1)

        self.closeButton = Button (editingFrame, width=10, text="CLOSE", command=self.closeInventory)
        self.closeButton.grid (row=7, column=0, pady=10)

        self.listBox = Listbox (viewFrame, width=100)
        self.listBoxEditingLabel = Label (viewFrameForEditing, text="Select Barcode For Editing:", width=25, height=2)
        self.listBoxEditingLabel.pack (side=TOP, fill=BOTH)
        self.listBoxEditing = Listbox (viewFrameForEditing)
        self.listBoxEditing.pack (side=LEFT, fill=BOTH, expand="true")
        self.labelListBox = Label (viewFrame, width=75, height=2, text="INVENTORY")
        self.labelListBox.pack (side=TOP, fill=X)
        self.listBox.pack (side=LEFT, fill=BOTH)
        self.scrollbar = Scrollbar (viewFrame)
        self.scrollbar.pack (side=RIGHT, fill=BOTH)

        items = itemDatabase.getItems ()

        for item in items:
            description = item[3] + " " + item[1]
            barcode = item[0]
            self.listBox.insert (END, f"Barcode: {barcode}   {description}")

        barcodes = itemDatabase.getBarcodes ()

        for barcode in barcodes:
            self.listBoxEditing.insert (END, barcode)

        self.listBoxEditing.bind ("<<ListboxSelect>>", self.onItemClick)

        self.listBox.config (yscrollcommand=self.scrollbar.set)
        self.scrollbar.config (command=self.listBox.yview)

        # Packing the Frames in the main window
        headerFrame.pack (side=TOP, fill=BOTH)
        editingFrame.pack (side=LEFT, fill=BOTH, expand=False)
        viewFrame.pack (side=RIGHT, fill=BOTH, expand=False)
        viewFrameForEditing.pack (side=TOP, fill=BOTH, expand=True)

        # The mainloop() is basically a infinite loop that keeps a window running (looping) until a user closes it manually.
        self.appWindow.mainloop ()

    # Function to Add an Item Once a User has Entered All the Needed Info.
    # Every If-statement is a Validation Over User Input.
    # The Validation is Outputted using pop-up message boxes from the messageBox class in tkinter
    def addItem(self):
        # Validating if any of the Entries are Empty
        if (self.entry_Barcode.get () == ""
                or self.entry_Name.get () == ""
                or self.comboBox_Category.get () == ""
                or self.entry_Brand.get () == ""
                or self.entry_Quantity == ""
                or self.entry_sellingPrice == ""
                or self.text_Description == ""):

            messagebox.showerror ("Error", "Please Fill All The Data!")

        # Validating if the barcode Is of invalid value (alphabet or alphanumerical) or if The barcode is already used.
        elif not str (self.entry_Barcode.get ()).isdigit () or itemDatabase.isBarcodeUsed (self.entry_Barcode.get ()):

            messagebox.showerror ("Error", "Duplicate Barcode!")
            self.entry_Barcode.delete (0, END)

        # Here we're basically validating for VALUE_ERROR the quantity entry.
        elif not str (self.entry_Quantity.get ()).isdigit ():

            messagebox.showerror ("Error", "Invalid Quantity!")
            self.entry_Quantity.delete(0, END)

        # Validating the category.
        elif self.comboBox_Category.get () not in self.categories:

            messagebox.showerror ("Error", "Invalid Category!")

        # Validating For Value ERROR
        elif not str(self.entry_Price.get()).isdigit() or not str(self.entry_sellingPrice.get()).isdigit():
            messagebox.showerror("ERROR", "INVALID PRICES!")

        # Here, logically speaking, the selling price cannot be less than the buying price or the buisness will be at a loss.
        # So we are also validating the selling price.
        elif self.entry_sellingPrice.get () < self.entry_Price.get ():
            messagebox.showerror ("Error", "Selling Price Cannot be Less Than Actual Price")
            self.entry_Price.delete (0, END)
            self.entry_sellingPrice.delete (0, END)

        # If all Validations succeed, then the user has Entered Correct Values and the program can proceed to add the item to the database.
        else:
            # Creating the Variables to pass to the __init__ function for the Item Class.
            name = str (self.entry_Name.get ()).upper ()
            barcode = self.entry_Barcode.get ()
            category = self.comboBox_Category.get ()
            brand = str (self.entry_Brand.get ()).upper ()
            quantity = self.entry_Quantity.get ()
            price = self.entry_Price.get ()
            sellingPrice = self.entry_sellingPrice.get ()
            description = str (self.text_Description.get ("1.0", END))

            # Creating a New Item that has the values Entered by a user.
            # Notice That whenever we create an item object. It automatically gets added into the Database because we included the createItem() in the __init__ function.
            newItem = Item (name.upper (),
                            barcode,
                            category,
                            brand.upper (),
                            quantity,
                            price,
                            sellingPrice,
                            description.upper ())

            # Inserting the entry to the inventory listbox.
            self.listBox.insert (END, "Barcode:  " + str (self.entry_Barcode.get ()) + "         "
                                 + str (self.entry_Brand.get ()).upper () + " " + str (self.entry_Name.get ()).upper ())
            # Inserting The Entry's barcode into the editing Listbox.
            self.listBoxEditing.insert (END, self.entry_Barcode.get ())

            # Calcutating The amount to pay and add to the cashier table in the database.
            amount = float (newItem.getPrice ()) * float (newItem.getQuantity ())
            itemDatabase.pay (amount)

            # Clearing all the entries after adding.
            self.clearButton ()

            # Outputting an informative message Box.
            messagebox.showinfo("INFO", "ITEM ADDED SUCCESSFULLY!")

    # Function to clear All Entry Widgets.
    def clearButton(self):
        self.updateButton.configure (state='disabled')      # Setting the update button to disabled
        self.entry_Barcode.delete (0, END)
        self.entry_Name.delete (0, END)
        self.comboBox_Category.current (0)
        self.entry_Brand.delete (0, END)
        self.entry_Quantity.delete (0, END)
        self.entry_Price.delete (0, END)
        self.entry_sellingPrice.delete (0, END)
        self.text_Description.delete ("1.0", END)

    # OnClick function for the editing listbox.
    # We Expect this method to fill the Entries with the info pertaining to the barcode that the user clicked on.
    def onItemClick(self, event):
        selection = event.widget.curselection ()                   # returns a tuple containing the index of the Item clicked on.
        if selection:
            index = selection[0]                                   # Creating a variable holding the Index
            data = event.widget.get (index)                        # Getting The Barcode from the clicked Item
            curentItem = itemDatabase.getItem (data)               # Getting the Item that has the barcode

            self.clearButton ()                                    # Clearing everything before configuring the Entries

            # CurrentItem is A tuple Containing another tuple holding the Values of the item called by the preceding function.
            # Therefor, first we call currentItem[0] which is the tuple containing the info, then we choose the second index to point to the needed value.
            self.updateButton.configure (state="active")
            self.entry_Barcode.insert (END, curentItem[0][0])           # Assigning barcode
            self.entry_Name.insert (END, curentItem[0][1])              # Assigning Name
            self.comboBox_Category.insert (END, curentItem[0][2])       # Assigning ComboBox
            self.entry_Brand.insert (END, curentItem[0][3])             # Assigning Brand
            self.entry_Quantity.insert (END, curentItem[0][4])          # Assigning quantity
            self.entry_Price.insert (END, curentItem[0][5])             # Assigning Price
            self.entry_sellingPrice.insert (END, curentItem[0][6])      # Assigning Selling Price
            self.text_Description.insert (END, curentItem[0][7])        # Assigning Description

    # Function That Updates The Values for a an Item holding a certain barcode.
    def updateButton(self):
        # Same Entry validations
        if (self.entry_Barcode.get () == ""
                or self.entry_Name.get () == ""
                or self.comboBox_Category.get () == ""
                or self.entry_Brand.get () == ""
                or self.entry_Quantity == ""
                or self.entry_sellingPrice == ""
                or self.text_Description == ""):

            messagebox.showerror ("Error", "Please Fill All The Data!")

        elif not str (self.entry_Quantity.get ()).isdigit ():

            messagebox.showerror ("Error", "Invalid Quantity!")
            self.entry_Quantity.delete(0, END)

        elif self.comboBox_Category.get () not in self.categories:

            messagebox.showerror ("Error", "Invalid Category!")
            self.comboBox_Category.set(0)

        elif not str(self.entry_Price.get()).isdigit() or not str(self.entry_sellingPrice.get()).isdigit():
            messagebox.showerror("ERROR", "INVALID PRICES!")

        elif self.entry_sellingPrice.get () < self.entry_Price.get ():
            messagebox.showerror ("Error", "Selling Price Cannot be Less Than Actual Price")
            self.entry_Price.delete (0, END)
            self.entry_sellingPrice.delete (0, END)

        else:
            # Using the Database Update Function
            itemDatabase.updateItem (self.entry_Barcode.get (),
                                     self.entry_Name.get (),
                                     self.comboBox_Category.get (),
                                     self.entry_Brand.get (),
                                     self.entry_Quantity.get (),
                                     self.entry_Price.get (),
                                     self.entry_sellingPrice.get (),
                                     self.text_Description.get ("1.0", END))

            # Clearing the list boxes to refill them with updated Data
            self.listBoxEditing.delete (0, END)
            self.listBox.delete (0, END)

            # Refilling the List Boxes with the new Items
            items = itemDatabase.getItems ()
            for item in items:
                self.listBox.insert (END, "Barcode: " + str (item[0]) + "          " + item[3] + " " + item[1])

            barcodes = itemDatabase.getBarcodes ()

            for barcode in barcodes:
                self.listBoxEditing.insert (END, barcode)

            # Clearing The Screen After updating
            self.clearButton ()

    # Function To Delete an item from the inventory.
    def deleteItem(self):

        # we only need a barcode for this so we only validate the barcode.
        if len (self.entry_Barcode.get ()) == 0:
            messagebox.showerror ("ERROR", "Invalid Barcode!")
        else:
            # logically, when deleting an item from the inventory, it means also returning the paid money.
            # so We also need to calculate the paid money to return it to the register.

            barcode = self.entry_Barcode.get ()
            tempItem = itemDatabase.getItem (barcode)
            currentItemQuantity = tempItem[0][4]
            itemPrice = tempItem[0][5]
            paidAmountForItem = (float (currentItemQuantity) * float (itemPrice))

            itemDatabase.returnItemToSupplier(barcode, paidAmountForItem)  # using the returnItemToSupplier() from the database.
            itemDatabase.deleteItem (barcode)                              # Deleting from the database

            self.listBoxEditing.delete (0, END)
            self.listBox.delete (0, END)

            items = itemDatabase.getItems ()
            for item in items:
                self.listBox.insert (END, "Barcode: " + str (item[0]) + "          " + item[3] + " " + item[1])

            barcodes = itemDatabase.getBarcodes ()

            for barcode in barcodes:
                self.listBoxEditing.insert (END, barcode)

            messagebox.showinfo("INFO", "ITEM DELETED SUCCESSFULLY!")
            self.clearButton ()

    # Function to close The Inventory Screen and reopen the main Screen.
    def closeInventory(self):
        self.appWindow.destroy ()
        main ()

# Same Applies to the Sales Screen Class
class SalesScreen:
    def __init__(self):
        # Defining main App Window
        self.appWindow = Tk ()
        # Defining window size
        self.appWindow.geometry ("1920x1080")
        # Setting a Title
        self.appWindow.title ("Sales")
        # In the Sales Window, we created 2 lists to hold the objects that the customer Chose and their Quantity.
        # Every time we add an Item, It is appended to the itemList. And its quantity is appended to the Other List.
        # So Basically The 2 lists will have the Same Length and every Index will match the Item to its corresponding Quantity.
        self.itemList = []
        self.itemQuantities = []

        # Creating The Frames and assigning them to the main window
        self.headerFrame = Frame (self.appWindow, highlightbackground="Black", highlightthickness=1)

        self.label_header = Label (self.headerFrame,
                                   text="SALES",
                                   font=("Arial Black", 32),
                                   bg="#34ebd8",
                                   fg="#FFFFFF",
                                   justify='center').pack (fill=X)
        self.headerFrame.pack (side=TOP, fill=X)

        self.cartFrame = Frame (self.appWindow, highlightbackground="Black", highlightthickness=1)
        self.receiptFrame = Frame (self.appWindow)

        self.labelEntrybarcode = Label (self.cartFrame, text="Enter Barcode: ")
        self.labelEntrybarcode.grid (column=0, row=0, pady=10)

        self.entrybarcode = Entry (self.cartFrame)
        self.entrybarcode.grid (column=1, row=0, padx=10, pady=10)

        self.labelEntryQuantity = Label (self.cartFrame, text="Enter Quantity: ")
        self.labelEntryQuantity.grid (column=2, row=0, padx=10, pady=10)

        self.entryQuantity = Entry (self.cartFrame)
        self.entryQuantity.grid (column=3, row=0, padx=10, pady=10)

        self.listBoxCart = Listbox (self.cartFrame, width=100, height=20)
        self.listBoxCart.grid (row=1, column=0, padx=10, columnspan=10)
        self.listBoxCart.bind ("<<ListboxSelect>>", self.onItemClick)
        self.selectedItemIndex = -1
        self.selectedItemQuantity = 0

        self.btnAddToCart = Button (self.cartFrame, text='Add To Cart', command=self.addToCart)
        self.btnAddToCart.grid (column=0, row=2, padx=10, pady=10)

        self.btnRemoveFromCart = Button (self.cartFrame, text='Remove From Cart', state='disabled',
                                         command=self.removeFromCart)
        self.btnRemoveFromCart.grid (column=1, row=2, padx=10, pady=10)

        self.btnCancelSale = Button (self.cartFrame, text="Cancel Purchase", command=self.cancelPurchase)
        self.btnCancelSale.grid (column=2, row=2, padx=10, pady=10)

        self.btnBuy = Button (self.cartFrame, text='Done', command=self.makePurchase)
        self.btnBuy.grid (column=3, row=2, padx=10, pady=10)

        self.closeButton = Button (self.cartFrame, text="CLOSE", command=self.closeSales)
        self.closeButton.grid (column=4, row=2, padx=10, pady=10)

        self.labelTotalText = Label (self.cartFrame, text="TOTAL: ")
        self.labelTotalText.grid (column=0, row=3, padx=10, pady=10)

        self.total = 0
        self.labelTotal = Label (self.cartFrame, text=str (self.total), bg='white', relief="sunken")
        self.labelTotal.config (font=("Courier", 44))
        self.labelTotal.grid (column=1, row=3, padx=10, pady=10)

        self.receiptText = Text (self.receiptFrame, relief='sunken', bg='white', state='disabled', width=40)
        self.receiptText.pack (fill=Y, pady=20)

        self.cartFrame.pack (side=LEFT, anchor='nw', fill=BOTH, expand=True)
        self.receiptFrame.pack (side=RIGHT, anchor='se', fill=Y, expand=False, padx=50)

        self.appWindow.mainloop ()

    # Function to Add an Item To The Cart.
    def addToCart(self):
        # we Want the remove button to always stay disabled until a user clicks on an item in the cart.
        self.btnRemoveFromCart.configure (state="disabled")
        # Creating a temp Item Object to Validate if The entered quantity succeeds the Stock
        itemTemp = itemDatabase.getItem (self.entrybarcode.get ())

        # Validating if any of the widgets is left empty
        if len (str (self.entrybarcode.get ())) == 0 or len (str (self.entryQuantity.get ())) == 0:
            messagebox.showerror ("Error", "Please Enter All The Values!")
        # Validating if the Barcode Entered exists in the Database
        elif not itemDatabase.isBarcodeUsed (self.entrybarcode.get ()):
            messagebox.showerror ("Error", "Barcode Does Not Exist!")
        # Validating the Quantity, it shouldn't be negative or zero
        elif int (self.entryQuantity.get ()) <= 0:
            messagebox.showerror ("Error", "Invalid Quantity!")
        # Validating if the Entered Quantity succeeds the stock
        elif int (self.entryQuantity.get ()) > itemTemp[0][4]:
            messagebox.showerror ("Error", "The Quantity Entered Exceeds The Stock!")
        else:

            # If all Validations Succeed, we want to add the Item and its Quantity to our shopping cart.
            # That means adding the Item to the ItemList and adding its Quantity into the Quantity List.
            # Also we want to add the Item Into The list box.
            barcode = self.entrybarcode.get ()
            quantity = self.entryQuantity.get ()
            item = itemDatabase.getItem (barcode)[0]  # returns a tuple holding Info about the Item added.
            self.itemList.append (item)               # Appending The item to the item list
            self.itemQuantities.append (quantity)     # Appending the Quantity to the Item List.
            # Creating The String and inserting it to the shopping Cart Listbox
            description = str (item[3]) + " " + str (item[1])
            self.listBoxCart.insert (END, " " + str (quantity) + "                    " + description + "                 " + str (item[6]))
            # Calculating the Total And Configuring the Label to show it.
            self.total = self.total + item[6] * float (quantity)
            self.labelTotal.configure (text=str (self.total))
            # Clearing The Entry widgets
            self.entrybarcode.delete (0, END)
            self.entryQuantity.delete (0, END)

    # The OnClick function for the ListBox.
    # When a User Clicks on a listBox Entry, The Remove button becomes Active.
    # Two Variables are Created:
    # The Index of the entry in the list Box which logically matches the indexes in the ItemList and Quantity List.
    # And The Quantity of the Item Selected so we can decrease the quantity when removing an item
    def onItemClick(self, event):
        selection = event.widget.curselection ()
        if selection:
            # getting the index of our selection. It will match the indexes in our lists.
            index = selection[0]
            # Getting the Data of our selection. We're gonna use the String at index 0 which is the quantity of the item.
            data = event.widget.get (index)
            # getting the Tuple holding the Info of the selected item to get its price.
            currentItem = self.itemList[index]

            # Enabling the Remove Button,
            self.btnRemoveFromCart.configure (state="active")
            # Clearing The Widgets
            self.entrybarcode.delete (0, END)
            self.entryQuantity.delete (0, END)
            # Inserting the Values to the Widgets
            self.entrybarcode.insert (END, currentItem[0])
            self.entryQuantity.insert (END, data[1])
            # Creating the Variables.
            self.selectedItemIndex = index
            self.selectedItemQuantity = data[1]

    # Function to remove An Item From the shopping cart ( From the Listbox and Lists and decreasing the total).
    def removeFromCart(self):
        # Deleting The selected entry from the ListBox
        self.listBoxCart.delete (ANCHOR)
        # Getting the Item Info in a tuple
        currentItem = self.itemList[self.selectedItemIndex]
        # Calculating the amount to decrease from total and setting it into the label.
        amountToDecrease = currentItem[6] * float (self.selectedItemQuantity)
        self.total = self.total - amountToDecrease
        self.labelTotal.configure (text=self.total)
        # Deleting the values From the Lists
        self.itemList.pop (self.selectedItemIndex)
        self.itemQuantities.pop (self.selectedItemIndex)
        # Clearing the Widgets
        self.entrybarcode.delete (0, END)
        self.entryQuantity.delete (0, END)

    # Function to Cancel the whole Purchase.
    # All the widgets and lists are Cleared
    def cancelPurchase(self):
        self.itemList.clear ()
        self.itemQuantities.clear ()
        self.entrybarcode.delete (0, END)
        self.entryQuantity.delete (0, END)
        self.listBoxCart.delete (0, END)
        self.selectedItemIndex = -1
        self.selectedItemQuantity = -1
        self.btnRemoveFromCart.configure (state='disabled')
        self.total = 0.0
        self.labelTotal.configure (text=self.total)
        self.receiptText.configure (state='normal')
        self.receiptText.delete ('1.0', END)
        self.receiptText.configure (state='disabled')

    # Function to print A receipt
    def printReceipt(self):
        # A text widget is usually editable by users. So we have to modify the States to be able to insert text.
        self.receiptText.configure (state='normal')
        # Clearing the Text.
        self.receiptText.delete ('1.0', END)
        # Creating the Lines and formatting them.
        nowTime = datetime.now ()      # Current time
        todayTime = datetime.today ()  # Current Date
        today = "\tDATE: " + todayTime.strftime ("%B %d, %Y")
        now = "\t    TIME: " + nowTime.strftime ("%H:%M:%S")
        title = "\t  PYTHON POS V1.00"
        location = " AMERICAN UNIVERSITY OF SCIENCES AND TECHNOLOGY"
        region = "\t\tBEIRUT"
        separator = "----------------------------------------"
        quantifiers = "Q.    Description\t       \t\tPrice"
        self.receiptText.insert ('end', title + "\n")
        self.receiptText.insert ('end', location + "\n")
        self.receiptText.insert ('end', region + '\n')
        self.receiptText.insert ('end', str (today) + '\n')
        self.receiptText.insert ('end', str (now) + '\n')
        self.receiptText.insert ('end', separator + '\n')
        self.receiptText.insert ('end', quantifiers + '\n')

        # Formatting The lines.
        self.receiptText.tag_add ('title', '1.0', '1.end')
        self.receiptText.tag_config ('title', font='arial 12 bold')

        self.receiptText.tag_add ('location', '2.0', '2.end')
        self.receiptText.tag_config ('location', font='arial 8 italic')

        self.receiptText.tag_add ('quantifiers', '7.0', '7.end')
        self.receiptText.tag_config ('quantifiers', font='arial 8 bold ')

        # Filling the Body Text from the Lists Created.
        bodytext = ""

        for index in range (len (self.itemList)):
            description = str (self.itemList[index][3]) + " " + str (self.itemList[index][1])
            quantity = str (self.itemQuantities[index])
            price = float (self.itemQuantities[index]) * float (self.itemList[index][6])
            neededSpaces = " " * (30 - len (description))

            bodytext = quantity + "  " + description + neededSpaces + str (price)
            self.receiptText.insert ('end', bodytext + '\n')

        self.receiptText.insert ('end', separator + '\n')
        totalUSD = "\tTOTAL USD:" + " " * (25 - len ("\tTOTAL USD:")) + str (self.total)
        self.receiptText.insert ('end', totalUSD + '\n')
        self.receiptText.insert ('end', "\n\n\tTHANK YOU! COME AGAIN.\n")

        self.receiptText.configure (state='disabled')

    # Finally This Function applies The Purchase by:
    # decrementing the item quantity
    # Modifying the register and making the Transaction
    # Printing the Receipt
    def makePurchase(self):
        # Printing the receipt
        self.printReceipt ()
        # Creating the amount Variable that will hold the amount to be added to the register.
        amount = 0.0

        for index in range (len (self.itemList)):
            itemBarcode = self.itemList[index][0]
            itemQuantity = self.itemQuantities[index]
            itemSellingPrice = self.itemList[index][6]
            amount += float (itemSellingPrice) * float (itemQuantity)

            itemDatabase.decrementQuantity (itemBarcode, itemQuantity)

        itemDatabase.purchase (amount)

    # Closing the Sales Screen
    def closeSales(self):
        self.appWindow.destroy ()
        main ()

# Function to open the Inventory Screen
def openInventoryScreen():
    myInventory = InventoryScreen ()

# Function to open the Sales Screen
def openSalesScreen():
    mySalesScreen = SalesScreen ()

# Main Function That will hold the Main Screen.
def main():
    # Creating the Database And register (if The database does not exist)
    itemDatabase.createDatabase ()
    appWindow = Tk ()
    appWindow.geometry ("1000x500")
    appWindow.title ("Python POS")
    header = Label (master=appWindow,
                    text="PYTHON POS V1.00",
                    font=("Arial Black", 32),
                    bg="#34ebd8",
                    fg="#FFFFFF").pack (fill=X)

    salesButton = Button (appWindow, text="Sales", font=("Calibri Bold Italic", 24),
                          command=lambda: [appWindow.destroy (), openSalesScreen ()]).pack (ipady=10, ipadx=100)
    inventoryButton = Button (appWindow, text="Inventory", font=("Calibri Bold Italic", 24),
                              command=lambda: [appWindow.destroy (), openInventoryScreen ()]).pack (ipadx=100)
    credits = Label (appWindow, text="Created by:\nNael Ghannam",
                     font=("Calibri Bold Italic", 10)).pack (side=BOTTOM)

    appWindow.mainloop ()


main ()
