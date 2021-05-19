import os
#this week's new import

def fileprocessing():
#fileprocessing is the function

    directory = input("Enter the name of the directory: ")
    filename = input("Enter the name of the file: ")
    name = input("Enter your name: ")
    address = input("Enter your address : ")
    phone_number = input("Enter your phone number : ")
    if os.path.isdir(directory):
    #return true if the directory exists
        writeFile = open(os.path.join(directory,filename),'w')
        #file to write
        writeFile.write(name+','+address+','+phone_number+'\n')
        #write the data to file
        writeFile.close()
        #close the file
        print("File contents: ")
        readFile = open(os.path.join(directory,filename),'r')
        #store data
        for line in readFile:
            print(line)
        readFile.close()
    else:
        print("Sorry, that directory was not found.")
fileprocessing()