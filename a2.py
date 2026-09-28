try:
    num1, num2 = eval(input("Enter two numbers, seperated by a coma:"))
    result = num1/num2
    print("Result is" , result)
except ZeroDivisionError:
    print("Division by zero is an error!!")
        
except SyntaxError:
    print("Coma is missing.Enter numbers seperated by a coma like this 1,2")
except:
    print("Wrong Input")
else:
    print("No Exceptions")
finally:
    print("This will execute no matter what")
