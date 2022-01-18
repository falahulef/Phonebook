
from tabulate import tabulate
from termcolor import colored


class Node:
    # Node for singly Linkedlist
    def __init__(self, data, data2):
        self.data = data
        self.data2 = data2
        self.next = None


class singly_linked_list:
    def __init__(self):
        # create empty list
        self.head = None
        self.tail = None
        self.count = 0

    def iterate_item(self):
        # Iterate the list.
        current_item = self.head
        while current_item:
            val = current_item.data
            val2 = current_item.data2
            current_item = current_item.next
            yield val, val2

    def search_item(self, key):
        # search item in list
        print("🔍 Your Contact With Name : ", colored(key, "yellow"))
        print("{:<20} {:<9}".format("Nama", "Phone Number"))
        for node in self.iterate_item():
            if key in node:
                name, phone = node[0], node[1]
                print("{:<20} {:<9}".format(name, phone))
 
    def update_matches(self, key):
        for node in self.iterate_item():
            if key in node:
                return node[0]
              
# Prefix Search (Contains Word)
    def prefix_search(self, val):
        print("🔍 Your Contact Contains : '",
              colored(val, "yellow"), "' Character.")
        print("{:<20} {:<9}".format("Nama", "Phone Number"))
        for prefix in self.iterate_item():
            if str(val).lower() in str(prefix).lower():
                name, phone = prefix[0], prefix[1]
                print("{:<20} {:<9}".format(name, phone))

# Print All Node
    def print_all_item(self):
        print("👥 Your Phonebook Contact : ")
        print("{:<20} {:<9}".format("Nama", "Phone Number"))
        for val in self.iterate_item():
            name, phone = val[0], val[1]
            print("{:<20} {:<9}".format(name, phone))
            
# Insert Data to Node LinkedList
    def append_item(self, data, data2):
        # menambahkan item pada list
        node = Node(data, data2)
        if self.tail:
            self.tail.next = node
            self.tail.next2 = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.count += 1
        
# Remove Node from LinkedList
    def RemoveNode(self, Removekey):
        HeadVal = self.head

        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return
        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return "Note : Failed Updated Data, Data Not Found!"

        prev.next = HeadVal.next
    HeadVal = None


PhoneBooks = singly_linked_list()

# Display Menu's
def InsertPhonebook():
    print("\n1. Input Phone Contact Menu")
    name = input("Enter Name : ")
    phone = input("Enter Phone Number : ")
    PhoneBooks.append_item(name, phone)


def PhonebookContact():
    print("")
    PhoneBooks.print_all_item()


def UpdatePhonebook():
    oldcontact = input(
        "\n2. Update Data Phone Contact Menu\nSteps 1 (Case Sensitive!):\nEnter the Old Contact Name: ")
    if oldcontact == PhoneBooks.update_matches(oldcontact):
        name = input(
            "Steps 2 :\nEnter the New Contact Name: ")
        phone = input(
            "Steps 3 :\nEnter the New Phone Number: ")

        PhoneBooks.append_item(name, phone)
        PhoneBooks.RemoveNode(oldcontact)
        print(colored("Note : Contact Name Updated!", "green"))
    else:
        print(colored("Note : The Old Contact Name Not Found!", "red"))


def SearchPhonebook():
    menu = input(
        "\n3. Search Data Phonebook Menu\nSelect type Search!\n1. Search (With True Word)\n2. Prefix Searh\n\nEnter Key (1/2): ")
    if menu == "1":
        search = input("Enter Contact Name (Case Sensitive!): ")
        PhoneBooks.search_item(search)
    elif menu == "2":
        prefix = input("Enter Character/Contact Name: ")
        PhoneBooks.prefix_search(prefix)
    else:
        print(colored("Invalid Key!.", "red"))


def Menus():
    key = input("Enter Key (1/2/3/4): ")
    if key == "1":
        InsertPhonebook()
        Menus()
    elif key == "2":
        UpdatePhonebook()
        Menus()
    elif key == "3":
        SearchPhonebook()
        Menus()
    elif key == "4":
        PhonebookContact()
        Menus()
    else:
        print(colored("Invalid Key!.", "red"))


print("☎  SIMPLE PHONEBOOK : MGH+ \n─────────────────────────\n1. Input Data Phonebook\n2. Update Data Phonebook\n3. Search Data Phonebook\n4. List Data Phonebook")
Menus()
