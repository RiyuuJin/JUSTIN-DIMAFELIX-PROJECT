# PHP to USD Converter
EXCHANGE_RATE = 63.06
print("Welcome to the PHP to USD Converter!")
# 1. Get the PHP amount from the user
php_amount = float(input("Enter the amount in PHP: "))
# 2. Convert PHP to USD
usd_amount = php_amount / EXCHANGE_RATE
# 3. Display the result
print(f"{php_amount} PHP = {usd_amount} USD")
# 4. Print the result
print(f"Converted amount: {usd_amount:.2f} USD")