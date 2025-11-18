"""
Flowchart example: Generate a flowchart from a Python function.
"""

from renderschema import diagram


def calculate_discount(price: float, customer_type: str) -> float:
    """
    Calculate the final price after applying discounts.
    
    Args:
        price: Original price of the item.
        customer_type: Type of customer ('regular', 'premium', 'vip').
    
    Returns:
        Final price after discount.
    """
    if customer_type == "vip":
        discount = 0.20
    elif customer_type == "premium":
        discount = 0.10
    else:
        discount = 0.0
    
    final_price = price * (1 - discount)
    
    if final_price < 10:
        final_price = 10  # Minimum price
    
    return final_price


if __name__ == "__main__":
    # Generate flowchart for the function
    print("Generating flowchart...")
    diagram(calculate_discount, diagram_type="flowchart").export("discount_flow.svg")
    print("✓ Saved to discount_flow.svg")
    
    # Generate with dark theme
    print("\nGenerating dark theme flowchart...")
    diagram(
        calculate_discount, 
        diagram_type="flowchart",
        theme="dark"
    ).export("discount_flow_dark.svg")
    print("✓ Saved to discount_flow_dark.svg")
