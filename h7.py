print("Welcome to the receipt program!")

runningTotal = 0.00

while True:
    value = input("Enter the value for the seat ['q' to quit]: ")         

    if value == 'q':
        break
    elif value.is():
        print("I'm sorry but {} isn't valid please try again.".format(value))
    else:
        runningTotal = runningTotal + float(value)

print("Total: $ {}".format(str(runningTotal)))
