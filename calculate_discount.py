def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If the discount percentage is 20% or higher, the discount is applied.
    Otherwise, the original price is returned.

    :param price: Original price of the item (float or int)
    :param discount_percent: Discount percentage to be applied (float or int)
    :return: Final price after applying the discount
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

# Main program
try:
    # Get input from the user
    original_price = float(input("Enter the original price of the item: $"))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Print the result
    if discount_percentage >= 20:
        print(f"The final price after applying a {discount_percentage}% discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${original_price:.2f}")
except ValueError:
    print("Invalid input! Please enter numeric values for the price and discount percentage.")
