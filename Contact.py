index=0
d={}
def add_contact():
    global index
    name = input("Enter Name")
    phone = input("Enter Phone Number")
    d[index] = {"Name":name,"Phone":phone}
    index=index+1

def del_contact():
    name = input("Enter the name to be deleted")
    idx=0
    for key,value in d.copy().items():
        if name != value['Name']:
            print("No")
        else:
            idx = key
            d.pop(idx)
            print("Delete")


    print("Del")

def search_contact():
    print("Search")

def edit_contact():
    print("edit")

def display():
    for key,value in d.items():
        print("For Key : ",key)
        print('Name ',value['Name'])
        print('Phone ',value['Phone'])

while True:
    print("1.Add Contact")
    print("2.Delete Contact")
    print("3.Search Contact")
    print("4.Edit Contact")
    print("5.Display")
    print("6.Exit")
    choice = int(input("Enter your choice"))
    # match choice :
    #     case 1:
    #         add_contact()
    #     case 2:
    #         del_contact()
    #     case 3:
    #         search_contact()
    #     case 4:
    #         edit_contact()
    #     case 5:
    #         display()
    #     case 6:
    #         break
    if choice == 1:
        add_contact()
    elif choice==2:
        del_contact()
    elif choice == 3:
        search_contact()
    elif choice == 4:
        edit_contact()
    elif choice == 5:
        display()
    else:
        break

