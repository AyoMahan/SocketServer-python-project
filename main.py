file = open("data.txt", "r")
read = file.readlines()  # read contains the info of text file including /n returns list with new line being a list item

modified = []  # create new list
for line in read:
    modified.append(line.strip())  # remove the /n
def Convert(string):
    li = list(string.split("|"))#converting list fo strings in to a list of a list
    return li
track=[]
for element in modified:
    track.append(Convert(element))#putting all the lists of strings together into a list of lists


for i in range(len(track)):
    for j in range(len(track[i])):
        print(track[i][j], end=" ")
    print()#printing database so far



def find_customer(searched_name=input()):
    for i in range(len(track)):#getting full info of person Find customer
        for j in range(len(track[i])):
            if(track[i][j]==searched_name):
             print(track[i], end=" ")
        print()



#to add an entry
def addentry(name, age, address, phone):
    entry = [name, age, address, phone]
    track.append(entry)
    print(track)


#to remove an entry
def removeEntry(name):
    for i in range(len(track)):  # clearing the info of a desired customer
        for j in range(len(track[i])):
            if (track[i][j] == name):
                track[i].clear()
                break

def updateAge(name, age):
    for i in range(len(track)):  # clearing the info of a desired customer
        for j in range(len(track[i])):
            if (track[i][j] == name):
                track[i][1]=age
                break

def updateAddress(name, newAddress):
    for i in range(len(track)):  # clearing the info of a desired customer
        for j in range(len(track[i])):
            if (track[i][j] == name):
                track[i][2]=newAddress
                break

def updatePhone(name, newNumber):
    for i in range(len(track)):  # clearing the info of a desired customer
        for j in range(len(track[i])):
            if (track[i][j] == name):
                track[i][3]=newNumber
                break

def printReport():
    for i in range(len(track)):
        for j in range(len(track[i])):
            print(track[i][j], end=" ")
        print()

print("welcome to the python DB menu")
print("\n")

key=False
while key==False:
    print("1.find customer\n2.add customer\n3.delete customer\n4.update customer age\n5.update customer address\n6.update customer phone\n7.print report\n8.exit")
    selection = input("enter selection:")
    if selection=="1":
        x = input('Enter name of customer:')
        find_customer(x)
    elif selection == "2":
        x = input("enter the name of the person to be added")
        y=input("Enter the age of the customer")
        z=input("Enter the address of teh customer")
        a=input("enter the telephone number of the customer")
        addentry(x, y, z, a)
    elif selection == "3":
        x = input("enter the name of the customer to be deleted")
        removeEntry(x)
    elif selection == "4":
        x = input("enter the name of the user to be updated")
        y = input("enter the new age of the user")
        updateAge(x, y)
    elif selection == "5":
        x=input("enter name of user")
        y=input("enter updated customer address")
        updateAddress(x, y)
    elif selection == "6":
        x = input("enter name of user")
        y=input("Enter the updated phone number")
        updatePhone(x, y)
    elif selection == "7":
        print("** Python DB contents **")
        for i in range(len(track)):
            for j in range(len(track[i])):
                print(track[i][j], end=" ")
            print()  # printing database so far
    elif selection == "8":
        print("you have succesfully exited the program")
        key= True
    else:
        print("try again ")




