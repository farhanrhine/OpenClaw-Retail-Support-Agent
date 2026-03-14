import csv
import sys
import json
import ast
import os

BASE_DIR = os.path.dirname(__file__)
PRODUCT_FILE = os.path.join(BASE_DIR, "../data/product_inventory.csv")

def find_product(product_id):
    with open(PRODUCT_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["product_id"] == product_id:
                return row

    return None


def check_size(product, size):
    sizes = product["sizes_available"].split("|")

    if size not in sizes:
        return {"available": False}

    stock_dict = ast.literal_eval(product["stock_per_size"])

    quantity = stock_dict.get(size, 0)

    return {
        "available": True,
        "quantity": quantity
    }


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print(json.dumps({"error": "Missing product_id"}))
        sys.exit(1)

    product_id = sys.argv[1]

    product = find_product(product_id)

    if not product:
        print(json.dumps({"error": "Product not found"}))
        sys.exit(0)

    if len(sys.argv) == 3:
        size = sys.argv[2]
        result = check_size(product, size)

        output = {
            "product_id": product_id,
            "size": size,
            "available": result["available"],
            "quantity": result.get("quantity", 0)
        }

        print(json.dumps(output))
    else:

        sizes = product["sizes_available"].split("|")

        print(json.dumps({
            "product_id": product_id,
            "sizes_available": sizes
        }))