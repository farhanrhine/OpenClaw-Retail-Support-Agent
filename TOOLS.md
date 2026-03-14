# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.


---

## Retail Support Data (Assignment)

Local dataset directory:

C:\Users\farha\.openclaw\workspace\data

### Orders Dataset
File: orders.csv

Columns:
- order_id
- order_date
- product_id
- size
- price_paid
- customer_id
- status
- tracking_id

Purpose:
Used to answer customer questions about order tracking and delivery status.


### Product Inventory
File: product_inventory.csv

Columns:
- product_id
- title
- vendor
- price
- compare_at_price
- tags
- sizes_available
- stock_per_size
- is_sale
- is_clearance
- bestseller_score

Purpose:
Used to answer sizing questions and product availability.


### Policy File
File: policy.txt

Contains:
- Normal return window
- Sale item return rules
- Clearance rules
- Vendor-specific exceptions
- Exchange rules

Purpose:
Used to answer FAQ and policy questions.


### Tool: lookup_orders

Script location:
tools/lookup_orders.py

Purpose:
Retrieve order information from orders.csv using an order_id.

Usage example:

uv run python tools/lookup_orders.py O0001

Returns JSON containing:

* order_id
* order_date
* product_id
* size
* price_paid
* customer_id
* status
* tracking_id

The assistant should call this tool whenever a user asks about order status.



### Tool: lookup_product

Script location:
tools/lookup_product.py

Purpose:
Retrieve product sizing and availability information from `product_inventory.csv`.

Usage examples:

Check available sizes:

uv run python tools/lookup_product.py P0015

Example output:

{
"product_id": "P0015",
"sizes_available": ["16","14","10"]
}

Check specific size availability:

uv run python tools/lookup_product.py P0015 14

Example output:

{
"product_id": "P0015",
"size": "14",
"available": true,
"quantity": 1
}

Returns JSON containing:

* product_id
* sizes_available
* size
* available
* quantity

The assistant should call this tool whenever a user asks about:

* product availability
* available sizes
* stock quantity for a specific size.




### Tool: lookup_policy

Script location:
tools/lookup_policy.py

Purpose:
Retrieve the store policy information from `policy.txt`.

Usage example:

uv run python tools/lookup_policy.py

Example output:

{
"policy": "Full policy text..."
}

The assistant should use this tool whenever a user asks about:

* return policies
* exchanges
* sale item returns
* clearance rules
* vendor-specific exceptions
