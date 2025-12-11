def marks(marks):
    if marks>=90:
        return "GRADE A"
    elif marks>=79:
        return "GRADE B"
    elif marks>=50:
        return "GRADE C"
    elif marks>=35:
        return "GRADE D"
    else:
        return "FAIL"
    

print(marks(85))