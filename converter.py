# PHP to JPY currency converter
# Current exhange rate baseline: ~2.51 JPY per 1 PHP
EXHANGE_RATE = 2.51
print("Philippine Peso to Japanese Yen Currency Converter")
# 1. Ask the user for input (how many Pesos they want to convert)
php_input = input("Enter the amount in Philippine Pesos (PHP): ")
# 2. Convert the text input into a decimal number (float) so we can do math
php_amount = float(php_input)
# 3. Calculate the conversion
jpy_amount = php_amount * EXHANGE_RATE
# 4. Print the result cleanly on the screen
print(f"{php_amount} PHP is equal to {jpy_amount:.2f} JPY")