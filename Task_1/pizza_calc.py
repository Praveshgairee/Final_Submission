# Constants
PIZZA_PRICE = 12.00
TUESDAY_DISCOUNT = 0.50
DELIVERY_CHARGE = 2.50
FREE_DELIVERY_THRESHOLD = 5
APP_DISCOUNT = 0.25

# Function to get valid integer input
def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer!")
        except ValueError:
            print("Please enter a number!")

# Function to get yes/no input
def get_yes_no_input(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ['y', 'n']:
            return answer == 'y'
        else:
            print('Please answer "Y" or "N".')

# Main function
def calculate_pizza_price():
    print("BPP Pizza Price Calculator")
    print("==========================\n")

    # Get user inputs
    num_pizzas = get_integer_input("How many pizzas ordered? ")
    delivery_required = get_yes_no_input("Is delivery required? (Y/N): ")
    is_tuesday = get_yes_no_input("Is it Tuesday? (Y/N): ")
    used_app = get_yes_no_input("Did the customer use the app? (Y/N): ")

    # Calculate base price
    base_price = num_pizzas * PIZZA_PRICE

    # Apply Tuesday discount
    if is_tuesday:
        base_price *= (1 - TUESDAY_DISCOUNT)

    # Calculate delivery charge
    delivery_price = 0 if num_pizzas >= FREE_DELIVERY_THRESHOLD or not delivery_required else DELIVERY_CHARGE

    # Calculate total price
    total_price = base_price + delivery_price

    # Apply app discount
    if used_app:
        total_price *= (1 - APP_DISCOUNT)

    # Output the total price
    print(f"\nTotal Price: £{total_price:.2f}.")

if __name__ == "__main__":
    calculate_pizza_price()
