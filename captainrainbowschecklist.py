
checklist = []

# CRUD functions
# create, read, update, destroy

def create(item):
    checklist.append(item)
    return "Added {} to checklist".format(item)

def read(index):
    return checklist[index]
    
def update(index, item):
    old = checklist[index]
    checklist[index] = item
    return "Added {} to {}".format(old, item)

def destroy(index):
    removed = checklist[index]
    checklist.pop(index)
    return "Removed {} from checklist".format(removed)

def showList(list):
    items = []
    for i in list:
        print(i)
        items.append(i)
    return items

def checked(index):
    unchecked = checklist[index]
    checklist[index] = "✓ " + unchecked
    return checklist[index]    

def user_input(prompt):
    entry = input(prompt)
    return entry

def userChoice():

    working = True

    while working:
        choice = user_input("what function do you want to use? (CREATE, READ, UPDATE, DESTROY) ")

        if choice == "C" or choice == "c":
            item = user_input("what item do you want to create? ")
            create(item)
            continue

        elif choice == "R" or choice == "r":
            index = user_input("what item do you want to read? ") 
            read(index)
            continue

        elif choice == "U" or choice == "u":
            updateIndex = user_input("what item do you want to update? ")
            newItem = user_input("what is the new item? ")
            update(updateIndex, newItem)
            continue

        elif choice == "D" or choice == "d":
            deleteIndex = user_input("what item do you want to delete? ")
            destroy(deleteIndex)
            continue
        
        else:
            end = user_input("are you done? ")

            if end == "Y" or end == "y":
                print(checklist)
                working = False
            
            else:
                continue
        


# testing
def test():
#    create("purple sox")
#    create("red cloak")

#    print(showList(checklist))

#    print(read(0))
#    print(read(1))

#    update(0, "purple socks")
#    destroy(1)

#    print(read(0))
#    print(showList(checklist))
#    print(checked(0))
#    print(user_input("working? "))
    userChoice()


test()
