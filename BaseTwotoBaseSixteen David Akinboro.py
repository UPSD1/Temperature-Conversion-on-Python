# Python Program - Convert Binary to Hexadecimal and Octal

print("This is a program converting BASE 2 to BASE 16");
print("Enter 'x' for exit.");
binary = input("Enter a number in Binary Format (1's AND 0's): ");
if binary == 'x':
    exit();
else:
# converting binary to Hexadecimal using the hex built-in function
    temp = int(binary, 2);
    print(binary,"in Hexadecimal =",hex(temp));
    
print("Enter 'x' for exit.");
res = input("Enter x to exit the program: ");
if res == 'x':
    exit();
else:
    print("invalid input enetered.");




