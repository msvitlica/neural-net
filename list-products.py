import json

# Define the file path (update if needed)
file_path = "tropic_products_1.json"  

try:
    # Load the JSON file
    with open(file_path, "r", encoding="utf-8") as f:
        products = json.load(f)

    # Print the number of products
    total_products = len(products)
    print(f"Total number of products: {total_products}")

except FileNotFoundError:
    print("Error: JSON file not found. Please check the file path.")
except json.JSONDecodeError:
    print("Error: JSON file is not properly formatted.")
