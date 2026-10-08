# Multi-Currency Converter (PHP to JPY & NZD
EXCHANGE_RATE_JPY = 2.51
EXCHANGE_RATE_NZD =0.029 # Approximate baseline rate for PHP to NZD
print("=== Welcome to the Global Currency Converter ===")
print("[1] Convert PHP to Japanese Yen (JPY)")
print("[2] Convert PHP to New Zealand Dollar (NZD)")
# Get user choice
choice = input("Choose an option (1 or 2): ")
# Get the amount in pesos
php_input = input("Enter the amount in Philippine Pesos (PHP): ")
php_amount = float(php_input)
# Conditional logic: make a decision based on user choice
if choice == "1":
    jpy_amount = php_amount * EXCHANGE_RATE_JPY
    print(f"{php_amount} PHP is equal to {jpy_amount:.2f} JPY")
elif choice == "2":
    nzd_amount = php_amount * EXCHANGE_RATE_NZD
    print(f"{php_amount} PHP is equal to {nzd_amount:.2f} NZD")
else:
    print("Invalid choice. Please select either 1 or 2.")