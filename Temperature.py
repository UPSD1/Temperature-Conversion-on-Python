print('1. for Fahrenheit')
print('2. for Celsuis')
print('3. for Kelvin')
print('4. for Rankine')
x = eval(input('Please enter a temperature which you are converting from (1-4) : '))
if x == 1:
    # ASK user for temperature to convert and read the supplied value 
    degreesF = eval(input('Ask user for temperature in degrees F: '))
    # Perform the conversion 
    degreesC = 5/9*(degreesF - 32);
    degreesK = (degreesF + 459.67) / 1.8;
    degreesRa = (degreesF + 459.67);
    # Report the result
    print(degreesF, "degrees F =", degreesC, 'degrees C')
    print(degreesF, "degrees F =", degreesK, 'degrees K')
    print(degreesF, "degrees F =", degreesRa, 'degrees Ra')

elif x == 2:
    degreesC = eval(input('Enter the temperature in degrees C: '))
    # Perform the conversion
    degreesF = (degreesC * 1.8) + (32);
    degreesK = (degreesC + 273.15);
    degreesRa = (degreesC * 1.8) + (32 + 459.67);
    # Report the result
    print(degreesC, "degrees C =", degreesF, 'degrees F')
    print(degreesC, "degrees C =", degreesK, 'degrees K')
    print(degreesC, "degrees C =", degreesRa, 'degrees Ra')

elif x == 3:
    degreesK = eval(input('Enter the temperature in degrees K: '))
    # Perform the conversion
    degreesF = (degreesK * 1.8) - (459.67);
    degreesC = (degreesK - 273.15);
    degreesRa = (degreesK * 1.8);
    # Report the result
    print(degreesK, "degrees K =", degreesF, 'degrees F')
    print(degreesK, "degrees K =", degreesC, 'degrees C')
    print(degreesK, "degrees K =", degreesRa, 'degrees Ra')

elif x == 4:
    degreesRa = eval(input('Enter the temperature in degrees Ra: '))
    # Perform the conversion
    degreesF = (degreesRa - 459.67);
    degreesC = ((degreesRa - 32 - 459.67) / 1.8);
    degreesK = (degreesRa / 1.8);
    # Report the result
    print(degreesRa, "degrees Ra =", degreesF, 'degrees F')
    print(degreesRa, "degrees Ra =", degreesC, 'degrees C')
    print(degreesRa, "degrees Ra =", degreesK, 'degrees K')

else:
    print('Invalid Choice')
