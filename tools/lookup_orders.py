import csv
import sys
import json

import os

BASE_DIR = os.path.dirname(__file__)
ORDERS_FILE = os.path.join(BASE_DIR, "../data/orders.csv")


def find_order(order_id):
    with open(ORDERS_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["order_id"] == order_id:
                return row

    return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Missing order_id"}))
        sys.exit(1)

    order_id = sys.argv[1]

    result = find_order(order_id)

    if result:
        print(json.dumps(result))
    else:
        print(json.dumps({"error": "Order not found"}))