#print receipt for customers after 40% discount
#import input.txt doc for transaction id, name, total before discount

import input
def menu():
    choice = 0
    print('1: Print Transaction ID and username \n2: Print username and total before and after discount \n3: Quit')
    while choice < 1 or choice > 3:
        try:
            choice = int(input('Enter your choice: '))
            if choice < 1 or choice > 3:
                print('Enter valid option')
        except:
            print('Enter your choice: ')
    return choice

def read_file():
    file_name = 'input.txt'
    while True:
        user_file = input('Enter file name: ')
        if user_file.lower() = file_name:
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



