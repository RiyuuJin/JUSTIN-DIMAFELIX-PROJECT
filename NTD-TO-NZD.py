# NTD to NZD Currency Converter
EXCHANGE_RATE = 17.87
print("Welcome to the NTD to NZD Currency Converter!")
# 1. Get the NTD amount from the user
ntd_amount = float(input("Enter the amount in NTD: "))
# 2. Convert NTD to NZD
nzd_amount = ntd_amount / EXCHANGE_RATE
# 3. Display the result
print(f"{ntd_amount} NTD is equal to {nzd_amount:.2f} NZD.")
# 4. Ask the user if they want to convert another amount
while True:
    another_conversion = input("Do you want to convert another amount? (yes/no): ").strip().lower()
    if another_conversion == 'yes':
        ntd_amount = float(input("Enter the amount in NTD: "))
        nzd_amount = ntd_amount / EXCHANGE_RATE
        print(f"{ntd_amount} NTD is equal to {nzd_amount:.2f} NZD.")
    elif another_conversion == 'no':
        print("Thank you for using the NTD to NZD Currency Converter!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
    # 5. Print the final result
    print(f"Final converted amount: {nzd_amount:.2f} NZD")