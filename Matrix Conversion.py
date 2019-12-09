def main():
    sum = 0.0
    Number_Of_Enteries = 4
    numbers = []
    numbers2 = []
    
    #  Get input from the user
    print('Please enter', Number_Of_Enteries, 'numbers: ')
    for i in range(0, Number_Of_Enteries):
        num = eval(input("Enter number " + str(i) + ": "))
        numbers += [num] 

    # Print the numbers entered
    print(end="Numbers entered: ")
    for num in numbers:
        print("[", num, "]", end=" ")
    print() # Print newline

    # Get Input 2 from the user
    print('Please enter', Number_Of_Enteries, 'numbers: ')
    for i in range(0, Number_Of_Enteries):
        num = eval(input("Enter number " + str(i) + ": "))
        numbers2 += [num]

    # print the numbers entered
    print(end="Numbers entered: ")
    for num in numbers2:
        print("[", num, end=" ]")
    print() # print newline

    # compute operations
    n1 = (numbers[0]*numbers2[0] + numbers[1]*numbers2[2]);
    n2 = (numbers[0]*numbers2[1] + numbers[1]*numbers2[3]);
    n3 = (numbers[2]*numbers2[0] + numbers[3]*numbers2[2]);
    n4 = (numbers[2]*numbers2[1] + numbers[3]*numbers2[3]);

    # Display Results
    print("[", n1, + n2, "]")
    print("[", n3, + n4, "]")

        
main() # Execute main
