# OpenClaw Retail Support Agent

This project implements an **AI-powered customer support assistant** using OpenClaw.
The assistant automatically responds to customer inquiries on chat and WhatsApp channels.

## System Architecture

Customer messages arrive through messaging channels and are processed by an AI agent that can call tools to retrieve real data.

Flow:

Customer (WhatsApp / Telegram)
↓
OpenClaw Gateway
↓
LLM Agent (GLM-4.5-Air via OpenRouter)
↓
Tool Invocation Layer
↓
Local Data Sources

Tools used by the agent:

* `lookup_orders.py` → retrieves order status from `orders.csv`
* `lookup_product.py` → retrieves product sizes and stock from `product_inventory.csv`
* `lookup_policy.py` → retrieves return and exchange policy from `policy.txt`

## Example Query Flow

User question:

"Where is my order O0001?"

Agent workflow:

1. Detects order status request
2. Calls tool:

uv run python tools/lookup_orders.py O0001

3. Reads JSON response from dataset
4. Formats response for the customer

Example reply:

Your order **O0001** is currently **Delivered**.
Tracking ID: **TRK66993**

## Supported Customer Questions

The assistant automatically handles:

* Order status inquiries
* Product sizing and availability
* Return and exchange policies

Complex issues are escalated to a human support agent.

## Data Sources

data/

* orders.csv
* product_inventory.csv
* policy.txt

These datasets are used as the single source of truth to prevent hallucinated responses.

## Key Features

* WhatsApp and chat integration via OpenClaw
* Tool-based data retrieval
* Structured JSON responses
* Automatic first-response support
* Escalation for complex queries

This system ensures customers receive quick responses even when human support agents are unavailable.


# my final project looks like this.

```
workspace/
│
├ data/
│  ├ orders.csv
│  ├ product_inventory.csv
│  └ policy.txt
│
├ tools/
│  ├ lookup_orders.py
│  ├ lookup_product.py
│  └ lookup_policy.py
│
├ AGENTS.md
├ TOOLS.md
└ README.md
```

# how to run

```openclaw gateway
```
```
openclaw gateway --token test123
```



Below are some **good test questions** grouped by category for test .

---

# 1️⃣ Refund / complaint cases (should escalate)

Send these in WhatsApp:

```
I want a refund for my order O0001
```

```
My order arrived damaged, what should I do?
```

```
I want to cancel my order and get my money back
```

```
I’m very unhappy with my order, this is unacceptable
```

```
Your product quality is terrible, I want compensation
```

These trigger **customer frustration / refunds → escalate to human**.

---

# 2️⃣ Complex order issues

```
My order says delivered but I never received it
```

```
Can you change the shipping address for my order O0002?
```

```
I accidentally ordered the wrong product, can you fix it?
```

```
Can you expedite shipping for my order?
```

These require **manual intervention**.

---

# 3️⃣ Multi-step or unclear questions

```
Can you recommend a dress for a wedding next month?
```

```
Which product is best for summer events?
```

```
Do you have similar products to P0015?
```

These are **not supported by your dataset tools**.

---

# 4️⃣ Payment issues

```
My payment was charged twice
```

```
I paid but my order is not showing
```

```
Can I pay with PayPal?
```

Payment support should escalate.

---

# 5️⃣ Random unsupported questions

These also show the system safely refusing.

```
Do you ship internationally?
```

```
Can I speak to a manager?
```

```
I want to place a custom order
```

```
Can you apply a discount to my order?
```

---

# Expected bot response

The bot should reply something like:

```
Let me connect you with a support specialist who can assist you further.
```

This proves:

✔ escalation logic works
✔ the agent **doesn't hallucinate answers**
✔ it respects its capability boundaries

---

# (best flow)

Use this sequence:

1️⃣ **Order question**

```
Where is my order O0001?
```

2️⃣ **Product sizing**

```
Do you have product P0015 in size 14?
```

3️⃣ **Policy question**

```
Can I return a sale item?
```

4️⃣ **Escalation case**

```
My order arrived damaged, what should I do?
```

That shows **all system capabilities in under 1 minute**.

---
