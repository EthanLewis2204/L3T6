
#========The beginning of the class==========

#creating the class
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    
    #printing the cost of the shoe
    def get_cost(self):
        
        print("The cost of the shoe is R", self.cost)

    #printing the quantity of the show
    def get_quantity(self):
       
        print("There are ", self.quantity, "amount of shoes in stock")

    #printing the shoes as an object
    def __str__(self):
        
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''

#creating an empty list for the shoes
shoe_list = []
#==========Functions outside the class==============

#opening the external file and creating objects for the shoes and adding the shoes to the list
def read_shoes_data():
    
    '''
    Entering code to open the file inventory.txt
    The code will then read the data from this file, then create a shoes object with this data
    and append this object into the shoes list.
    '''
    file = open("inventory.txt", "r+")
    info = file.readline().split(",")
    info = file.readline().split(",")

    for x in info:
        country = info[0]
        code = info[1]
        product = info[2]
        cost = info[3]
        quantity = info[4]
        shoes = Shoe(country, code, product, cost, quantity)
        shoe_list.append(shoes)

    file.close()


#creating a function to add new shoes to the database
def capture_shoes():
    
    '''
    Entering code to allow the user to add a new shoe adn create a new shoe object. 
    This shoe will then be created as a new object
    '''
    file = open("inventory.txt", "a")

    country = input("Country: ")
    code = input("Code: ")
    product = input("Product: ")
    cost = input("Cost: ")
    quantity = input("Quantity: ")
    new_shoe = Shoe(country ,code ,product ,cost ,quantity)
    shoe_list.append(new_shoe)

    file.write(new_shoe)

#creating a function to view all the shoes
def view_all():
    
    '''
    Entering code to run through the shoe list and print the details returned from the __str__ function
    '''
    read_shoes_data()
    for x in shoe_list:
        print(x)

#creating a function to view the shoe with the lowest stock and giving the option of restocking the shoes
def re_stock():
    
    '''
    Entering code to find the shoe with the lowest quantity and asking the user if they would like to update the 
    quantity
    '''
    file = open("inventory.txt", "r")
    info = file.readline().split(",")
    info = file.readline().split(",")

    quantity = info[4]
    
    Lowest_quantity = quantity.find(quantity)
    print(info[Lowest_quantity])
    update = input("Would you like to update the quantity of the shoe? ").lower()

    if update == "yes":
        how_much = input("What would you like to change the quantity to? ")
    
    info[Lowest_quantity] = how_much
    
    
#creating a function to search for a specific shoe
def seach_shoe():
    
    '''
    Entering code to search for a shoe using the shoe code and then printing that object
    '''
    file = open("inventory.txt", "r+")
    info = file.readline().split(",")
    info = file.readline().split(",")

    shoe_code = input("please enter the code for the shoe you are looking for: ")
    required_shoe = shoe_list.find(shoe_code)
    return required_shoe

#creating a function to get the value per shoe
def value_per_item():
    
    '''
    Entering the code to determine the value of each shoe and then print that specific value
    '''
    file = open("inventory.txt", "r+")
    info = file.readline().split(",")
    info = file.readline().split(",")

    for x in info:
        cost = info[3]
        quantity = info[4]
        value = cost * quantity
        print("The value for your shoe is ",value)


#function to get the shoe with the highest quantity
def highest_qty():
    
    '''
    Entering the code to determine the shoe with the highest quantity
    '''
    file = open("inventory.txt", "r+")
    info = file.readline().split(",")
    info = file.readline().split(",")

    quantity = info[4]

    high_qty = max(quantity)
    return high_qty

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
#Entering the code for the menu
while True:
    menu = input('''Welcome to the menu!
    
    c = capture a new shoe
    v = view all shoes
    r = restock shoes
    s = search for a shoe
    vi = view the value per item
    h = view the shoe with the highest quantity
    
    Please select the option of what you would like to do: ''')

    if menu == "c":
        capture_shoes()

    elif menu == "v":
        view_all()
    
    elif menu == "r":
        re_stock()
    
    elif menu == "s":
        seach_shoe()
    
    elif menu == "vi":
        view_all()
    
    elif menu == "h":
        highest_qty()
    
    else:
        print("You have entered an invalid option, please try again!")
