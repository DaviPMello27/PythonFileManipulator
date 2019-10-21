from os import system
from cv2 import waitKey

#checkDoubleDots() ckecks if the string given contains ":" in it.
def checkDoubleDots(name, string):
    if(string.find(':') > -1):
        print(f"{name} can't contain \":\".")
        return " "
    else:
        return string

#checkSize() checks if a string length is bigger than the number given.
def checkSize(name, string, limit):
    if(len(string) > limit):
        print(f"{name}'s too big!")
        return " "
    else:
        return string

#saveFile() writes all of the user data in the file.
def saveFile(matrix):
    file = open("passwd.txt", "w")
    for i in range(len(matrix)):
        file.write(f"{matrix[i][0]}:x:{matrix[i][2]}:{matrix[i][3]}:{matrix[i][4]}:{matrix[i][5]}:{matrix[i][6]}")
    file.close()

#addUsername() applies the conditions to the Username string.
def addUsername(matrix, index):
    while(matrix[index][0] == " " or matrix[index][0] == ""):
        matrix[index][0] = input("Type your username: ")
        for i in range(index):
            if(matrix[index][0] == matrix[i][0]):
                matrix[index][0] = " "
                print("This user already exists!")
                break
        matrix[index][0] = checkSize("Username", matrix[index][0], 15)
        matrix[index][0] = checkDoubleDots("Username", matrix[index][0])

#addPassword() applies the conditions to the Password string.
def addPassword(matrix, index):
    while(matrix[index][1] == " " or matrix[index][1] == ""):
        matrix[index][1] = input("Type your password: ")
        if(len(matrix[index][1]) < 6):
            print("Password's too short!")
            matrix[index][1] = ""
        matrix[index][1] = checkSize("Password", matrix[index][1], 10)
        matrix[index][1] = checkDoubleDots("Password", matrix[index][1])

#addUserID() applies the conditions to the User ID string.
def addUserID(matrix, index):
    while(matrix[index][2] == " "):
        matrix[index][2] = input("Type your user ID (or leave blank to set it to default): ")
        if(not matrix[index][2].isdigit() and matrix[index][2] != ""):
            print("Your user ID must contain only numbers!")
            matrix[index][2] = " "
        for i in range(index):
            if(matrix[index][2] == matrix[i][2]):
                matrix[index][2] = " "
                print("This user ID is already being used!")
                break
        #Default ID generation:
        if(matrix[index][2] == ""):
            defaultUserID = 0
            for i in range(len(matrix) - 1):
                if(int(matrix[i][2]) > defaultUserID and int(matrix[i][2]) < 60000):
                    defaultUserID = int(matrix[i][2])
            matrix[index][2] = defaultUserID + 1
        else:
            matrix[index][2] = checkSize("User ID", matrix[index][2], 9)

#addGroupID() applies the conditions to the Group ID string.
def addGroupID(matrix, index):
    while(matrix[index][3] == " "):
        matrix[index][3] = input("Type your group ID (or leave blank to set it to default): ")
        if(not matrix[index][3].isdigit() and matrix[index][3] != ""):
            print("Your group ID must contain only numbers!")
            matrix[index][3] = " "
        if(matrix[index][3] == ""):
            matrix[index][3] = matrix[index][2]
        else:
            matrix[index][3] = checkSize("Group ID", matrix[index][3], 10)

#addName() applies the conditions to the Name string.
def addName(matrix, index):
    while(matrix[index][4] == " "):
            matrix[index][4] = input("Type your name (or leave blank to set it to default): ")
            if(matrix[index][4] == ""):
                matrix[index][4] = matrix[index][0]
            else:
                matrix[index][4] = checkSize("Name", matrix[index][4], 60)
                matrix[index][4] = checkDoubleDots("Name", matrix[index][4])

#addHomeDirectory() applies the conditions to the Home Directory string.
def addHomeDirectory(matrix, index):
    while(matrix[index][5] == " "):
        matrix[index][5] = input(f"Type your home directory (or leave blank to set it to home/{matrix[index][0]}): ")
        if(matrix[index][5] == ""):
            matrix[index][5] = "home/" + matrix[index][0]
        else:
            matrix[index][5] = checkSize("Home Directory", matrix[index][5], 22)
            matrix[index][5] = checkDoubleDots("Home Directory", matrix[index][5])

#ChangeUserData() changes the user data using one of the "add" functions declared above, then asks for the user's confirmation.
def changeUserData(matrix, line, column, function):
    temp = matrix[line][column]
    matrix[line][column] = " "
    function(matrix, line)
    choice = ""
    while(choice.upper() != 'Y' and choice.upper() != 'N'):
        system("CLS")
        choice = input(f"Change from {temp} to {matrix[line][column]}? (Y/N)")
    if(choice.upper() == 'Y'):
        saveFile(matrix)
    else: 
        matrix[line][column] = temp

#changeUser() asks the user which part of the user he wants to change, by using changeUserData().
def changeUser(matrix):
    searchIndex = -1
    search = input("Which user do you want to change?")
    #Searches for the username given.
    for i in range(len(matrix)):
        if(search ==  matrix[i][0]):
            searchIndex = i
            #Stops when it's found.
            break
    if(searchIndex == -1):
        print("This user does not exist.")
    else:
        system("CLS")
        print(f"Changing {matrix[searchIndex][0]}...")
        key = ""
        #Asks the user what he wants to change and wait for an adequate answer.
        while(key.upper() != 'U' and key.upper() != 'P' and key.upper() != 'I' and key.upper() != 'G' and key.upper() != 'N' and key.upper() != 'H'):
            system("CLS")
            key = input("Select what you want to change.\n(U)sername;\n(P)assword;\nUser (I)D;\n(G)roup ID;\n(N)ame;\n(H)ome Directory;")
            if(key.upper() == 'U'):
                changeUserData(matrix, searchIndex, 0, addUsername)
            elif(key.upper() == 'P'):
                changeUserData(matrix, searchIndex, 1, addPassword)
            elif(key.upper() == 'I'):
                changeUserData(matrix, searchIndex, 2, addUserID)
            elif(key.upper() == 'G'):
                changeUserData(matrix, searchIndex, 3, addGroupID)
            elif(key.upper() == 'N'):
                changeUserData(matrix, searchIndex, 4, addName)
            elif(key.upper() == 'H'):
                changeUserData(matrix, searchIndex, 5, addHomeDirectory)

#removeUser() asks for an username and uses .pop() to remove it
def removeUser(matrix):
    searchIndex = -1
    #Searches for the username.
    search = input("Which user do you want to remove?")
    for i in range(len(matrix)):
        if(search ==  matrix[i][0]):
            searchIndex = i
            #Stops when it's found.
            break
    if(searchIndex == -1):
        print("This user does not exist.")
    else:
        choice = ""
        while(choice.upper() != 'Y' and choice.upper() != 'N'):
            system("CLS")
            choice = input(f"Remove {matrix[searchIndex][0]}? (Y/N)")
        if(choice.upper() == 'Y'):
            print(f"Removing {matrix[searchIndex][0]}...")
            matrix.pop(searchIndex)
            print("Done!")
    #Writes everything back to mantain the file's formatting.
    saveFile(matrix)

#addUser() uses the "add" functions declared in the begginning to ask for every aspect of a new user in sequence,
#then asks for the user's confirmation and appends it to the text file.
def addUser(matrix):
    matrix.append([" ", " ", " ", " ", " ", " ", " "])
    last = len(matrix) - 1
    #============================USERNAME============================
    addUsername(matrix, last)
    #============================PASSWORD============================
    addPassword(matrix, last)
    #============================USER ID============================
    addUserID(matrix, last)
    #============================GROUP ID============================
    addGroupID(matrix, last)
    #============================NAME============================
    addName(matrix, last)
    #============================HOME DIRECTORY============================
    addHomeDirectory(matrix, last)
    #============================SHELL============================
    matrix[last][6] = "/bin/bash"
    key = ""
    while(key.upper() != 'Y' and key.upper() != 'N'):
        system("CLS")
        key = input(f"Are you sure you want to add this user? (Y/N)\n\n\
        Username: {matrix[last][0]};\n\
        Password: {matrix[last][1]};\n\
        User ID: {matrix[last][2]};\n\
        Group ID: {matrix[last][3]};\n\
        Name: {matrix[last][4]};\n\
        Home Directory: {matrix[last][5]};\n\
        Shell: {matrix[last][6]}.")
    if(key.upper() == 'Y'):
        passwd = open("passwd.txt", "a")
        passwd.write(f"\n{matrix[last][0]}:x:{matrix[last][2]}:{matrix[last][3]}:{matrix[last][4]}:{matrix[last][5]}:{matrix[last][6]}\n")
        passwd.close()
    elif(key.upper() == 'N'):
        #Removes the line if the user cancels.
        matrix.pop(last)

#showList() prints the matrix contents.
def showList(matrix):
    print("Username         Password  User ID  Group ID  Name                                                       Home Directory        Shell")
    for i in range(len(matrix)):
        print(f"{matrix[i][0]}", end = " "*(17-len(str(matrix[i][0])))) #  This function uses 
        print(f"{matrix[i][1]}", end = " "*(10-len(str(matrix[i][1])))) #  N-len(str(matrix[i][j]))
        print(f"{matrix[i][2]}", end = " "*(9-len(str(matrix[i][2]))))  #  to align the columns.
        print(f"{matrix[i][3]}", end = " "*(10-len(str(matrix[i][3]))))
        print(f"{matrix[i][4]}", end = " "*(59-len(str(matrix[i][4]))))
        print(f"{matrix[i][5]}", end = " "*(22-len(str(matrix[i][5]))))
        print(f"{matrix[i][6]}", end = "")

#Program starts here:
print("Welcome to the super-advanced file manipulator!")
key = ""
#Program only quits if the user presses "q".
while(key != 'q'):
    file = open("passwd.txt", 'r')
    lines = file.readlines()
    #Removes any blank lines
    for i in range(len(lines) - 1, 0, -1):
        if(lines[i] == "\n"):
            lines.pop(i)
    file.close()
    for i in range(len(lines)):
        #Splits the strings separated by ":" in multiple elements of a vector.
        lines[i] = lines[i].split(":")
    saveFile(lines)
    #Adds a line break in the end of the file, if there isn't one:
    if("\n".find(lines[len(lines) - 1][6]) == -1):
        lines[len(lines) - 1][6] = lines[len(lines) - 1][6] + "\n"
    key = input("\nPlease select an option:\n\n(L)ist users;\n(A)dd a user;\n(C)hange a user;\n(R)emove a user;\n(Q)uit")
    if(key.upper() == 'L'):
        showList(lines)
    elif(key.upper() == 'A'):
        addUser(lines)
    elif(key.upper() == 'C'):
        changeUser(lines)
    elif(key.upper() == 'R'):
        removeUser(lines)