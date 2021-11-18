


def add(num1, num2):
	return num1 + num2

def subtract(num1, num2):
	return num1 - num2

def multiply(num1, num2):
	return num1 * num2

def divide(num1, num2):
	return num1 / num2

print("Hallo ik ben Cal" \
		"Ik maak graag berekeningen" \
		"+ voor optellen" \
		"- voor aftrekken" \
		"* voor vermenigvuldigen" \
		"/ voor delen")

while True :
    num1 = float(input("Voer eerste nummer in"))

    choice = input("kies een berekening (+,-,*,/)")

    
    if choice in ('+', '-', '*', '/'):
        
        num2 = float(input("Voer tweede nummer in "))

        if choice == '+':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '/':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        
        next_calculation = input("Laten we nog een berekeing maken? (ja/nee): ")
        if next_calculation == "nee":
          break
    
    else:
        print("Invoer is foutief")

