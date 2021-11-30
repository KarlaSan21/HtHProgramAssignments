
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

def showList():
    for i in len(checklist):
        print(checklist[i] + " at index " + i + " ")
        


# testing
def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    showList()



    print(read(0))

test()
