inventory = ['pepperoni', 'sausage', 'cheese', 'peppers']

print('Welcome to Top Order')

t1 = input('Please give me a topping: ')

order = []

if t1 in inventory:
    print('Yes we have that in stock!')
    order.append(t1)
else:
    print('Sorry not in stock')


t2 = input('Please give me one more topping: ')

if t2 in inventory:
    print('Yes we have that in stock!')
    order.append(t2)    
else:
    print('Sorry not in stock')
    

print('here are your toppings')
print(order)