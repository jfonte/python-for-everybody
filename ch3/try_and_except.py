inp = input('Enter Fahrenheit Temperature:\n')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(round(cel,2))
except:
    print('Please make sure you are entering a number :]')

