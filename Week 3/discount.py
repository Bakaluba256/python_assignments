def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Parameters:
    - price (float): The original price of the item.
    - discount_percent (float): The discount percentage to be applied.

    Returns:
    - float: The final price after applying the discount if the discount is 20% or higher.
             Otherwise, returns the original price.
    """
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price
def main():
    # Prompt the user for the original price and discount percentage
    try:
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))

        if price < 0 or discount_percent < 0:
            print("Price and discount percentage must be positive numbers.")
            return

        # Calculate the final price
        final_price = calculate_discount(price, discount_percent)

        # Inform the user of the results
        if discount_percent >= 20:
            print(f"A discount of {discount_percent}% has been applied.")
        else:
            print("No discount applied as it is less than 20%.")
        print(f"The final price is: {final_price:.2f}")
        
    except ValueError:
        print("Please enter valid numeric values for price and discount percentage.")


if __name__ == "__main__":
    main()
