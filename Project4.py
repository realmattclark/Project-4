#print receipt for customers after 40% discount
#import input.txt doc for transaction id, name, total before discount

#import file.txt

#Display menu to user
def displayMenu():
    choice=0
    print("1- Print Transaction ID and user name\n2- Print user name, total before and total after discount\n3- Quit ")
    while choice<1 or choice>3:
        try:
            choice=int(input("Enter your choice ==>"))
            if choice<1 or choice>3:
                print("Enter valid option")
        except:
            print("Enter valid option")
            print("Enter your choice ==> ")
    return choice

#Get filename from user and validate it
def readFileToList():
    fileName='input.txt'
    while True:
        userFileName=input("Enter file name ==> ")
        if userFileName.lower()==fileName:
            break
        else:
            print("Enter correct file name")
    print("Reading data.....")

    fileData=[]
    try:
        with open(userFileName,'r') as f:
        #Read file
            data=f.read().split('\n')
           #For every line
            for line in data:
                fileData.append(line)
        return fileData
    except IOError:
        print("File not accessible. Please reenter")
            
def main():
    continueOrQuit='y'
    while continueOrQuit.lower()=='y':
        choice=displayMenu()
        if choice==1:
            fileData=readFileToList()
            print ("{:<8} {:<10} {:<10}".format('ID','FirstName','LastName'))
            for line in fileData:
                row=line.split(",")
                print("{:<8} {:<10} {:<10}".format(row[0],row[1],row[2]))
        elif choice==2:
            fileData=readFileToList()
            print ("{:<8} {:<10} {:<10} {:<10} {:<10}".format('ID','FirstName','LastName','Before','After'))

            for line in fileData:
                row=line.split(",")
                afterDiscount=float(row[3])-(float(row[3])*0.4)
                print("{:<8} {:<10} {:<10} {:<10.2f} {:<10.2f}".format(row[0],row[1],row[2],float(row[3]),afterDiscount))
        elif choice==3:
            continueOrQuit='n'
        continueOrQuit=input("Do you want to see more option Y/N: ")
    print("Have a great day")
    
#Driver code
if __name__ == "__main__":
    main()