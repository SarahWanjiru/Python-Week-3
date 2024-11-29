# Python-Week-3

# Calculate Discount Program

## Overview
This Python program calculates the final price of an item after applying a discount. The program determines whether to apply the discount based on the discount percentage provided by the user. If the discount percentage is **20% or higher**, the discount is applied. Otherwise, the program returns the original price.

## Features
- **Calculate Discounts:** Computes the final price after applying the discount if it meets the threshold.
- **User Interaction:** Prompts the user to input the original price and discount percentage.
- **Error Handling:** Provides feedback if invalid input (non-numeric) is entered.
- **Dynamic Pricing:** Handles both integers and floating-point numbers for accurate calculations.

## Code Explanation
### `calculate_discount` Function
This function is the core of the program. Here's how it works:
1. Accepts two parameters:
   - `price`: Original price of the item.
   - `discount_percent`: Percentage of the discount.
2. Checks if the discount percentage is **20% or higher**.
   - If yes, calculates the discount using the formula:
     ```
     discount_amount = price * (discount_percent / 100)
     final_price = price - discount_amount
     ```
   - If not, returns the original price.

### Main Program
1. Prompts the user for:
   - Original price of the item.
   - Discount percentage.
2. Calls `calculate_discount` to compute the final price.
3. Outputs:
   - The final price if the discount is applied.
   - A message indicating no discount was applied if the threshold is not met.
4. Handles invalid inputs (e.g., non-numeric values).

## How to Use
1. **Install Python:** Ensure Python 3 is installed on your system.
2. **Run the Program:** Save the code in a `.py` file (e.g., `calculate_discount.py`) and execute it using a terminal or an IDE:
   ```
   python calculate_discount.py
   ```
3. **Enter Input:** Provide the original price and discount percentage when prompted.

## Example Usage
### Input:
```
Enter the original price of the item: $100
Enter the discount percentage: 25
```
### Output:
```
The final price after applying a 25% discount is: $75.00
```

### Input:
```
Enter the original price of the item: $50
Enter the discount percentage: 10
```
### Output:
```
No discount applied. The original price is: $50.00
```

## Error Handling
If invalid input is entered (e.g., text instead of numbers), the program will display:
```
Invalid input! Please enter numeric values for the price and discount percentage.
```

## Customization
- Adjust the discount threshold by modifying the condition in the `calculate_discount` function:
  ```python
  if discount_percent >= <new_threshold>:
  ```
- Enhance with additional features such as tax calculations or multiple item discounts.

## License
This program is free to use for educational purposes. Modify and share as needed.

## Acknowledgments
- [Python Documentation](https://docs.python.org/3/)
- [Python Tutorial](https://www.w3schools.com/python/default.asp)



