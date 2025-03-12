user_input = input("Do you want to print the triangle? (yes/no): ")
if user_input == "yes":
    height = 10
    for i in range(1, height +1):
        print("*"*i)
else:
    print("Edi don't!")