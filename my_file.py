a=10
b=20


print(a*b,'-called from my_file')

def abc():
    print('Good message')

# dunder
if __name__ == '__main__':
    print('Called from main')  
    a= int(input('Enter first value- '))
    b= int(input('Enter second value- '))  