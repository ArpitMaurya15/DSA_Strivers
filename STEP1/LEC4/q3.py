num = 121
a = str(abs(num))  # Convert absolute value to string
b = int(a[::-1])

if num == b:
    print( True)
else:
    print( False)
