#print receipt for customers after 40% discount
#import input.txt doc for transaction id, name, total before discount

#import input

def read_file():
    file_name = 'input.txt'
    while True:
        user_file = input('Enter file name: ')
        if user_file.lower() == file_name:
            break
        else:
            print('Enter correct file name')
    file_data = []
    try:
        with open(user_file, 'r') as f:
            data = f.read().split('\n')
            for i in data:
                data.append(i)
        return data
    except IOError:
        print('Enter correct file name')


def main():
    choice = int(input('1: Print Transaction ID and Username \n2: Print username, total before and total after discount \n3: Quit'))
                 
    if choice == 1:
        file_data = read_file()
        print('ID \tFirst Name \tLast Name \tBefore \tAfter')
        print(file_data[0])
        print(file_data[1])
        print(file_data[2])
        print(file_data[3])
        print(file_data[4])
                 
    elif choice == 2:
        file_data = read_file()
        print('ID \tFirst Name \tLast Name \tBefore \tAfter')
        print(file_data[0])
        print(file_data[1])
        print(file_data[2])
        print(file_data[3])
        print(file_data[4])
        
    elif choice == 3:
        print('Have a great day')
main()
