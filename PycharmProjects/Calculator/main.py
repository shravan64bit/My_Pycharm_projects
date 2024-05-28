from art import logo

def add(n1,n2):
    return n1+n2
def substract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divison(n1,n2):
    return n1/n2
operations = {
    "+":add,
    "-":substract,
    "*":multiply,
    "/":divison
}
print(logo)
num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))
for symbol in operations:
    print(symbol)
operation_symbol = input("Enter the symbol of operation you have use")
def calculation (n1,n2,operation_symbol):
    current_symbol = operations[operation_symbol]
    return current_symbol(n1,n2)
result = calculation(num1,num2,operation_symbol)
print(f" {num1} {operation_symbol} {num2} = {result}")

continue_1 = True
while continue_1:
    loop = input("type 'y' for next operation or 'n' for stop")
    if loop == 'y':
        next_symbol = input("pick another operation")
        next_number = result
        third_number = float(input("Enter the next number"))
        print(f"{result} {next_symbol} {third_number} = {calculation(next_number, third_number, next_symbol)}")
    else:
        continue_1 = False


