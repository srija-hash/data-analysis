#7.2 File Processing
print("Python Data Analytics Lab Test")
orders = [] #new list for raw data
with open ("C:\\Users\\rjith\\OneDrive\\Desktop\\Book1.csv","r") as file:
        lines = file.readlines()
        header = lines[0].strip().split(",")
        for line in lines[1:]:
            data = line.strip().replace('"','').split(",")
            orders.append(data)
#7.3 Data Type Processing
clean_orders = [] #new list for clean data
for row in orders:

    order_id = row[0]
    customer_name = row[1].strip() #removing extra spaces
    city = row[2].strip().lower()
    product = row[3].strip()
    category = row[4].strip()
# type casting
    price = float(row[5])
    quantity = int(row[6])

    order_status = row[7].strip()
    order_date = row[8]
# Missing status replace for row 4 
    if order_status == "":
        order_status = "Pending"

    total_amount = round(price * quantity, 2)

    clean_orders.append([
        order_id,customer_name,city,product,category,
        price,quantity,order_status,order_date,total_amount
    ])
#7.4 Data Cleaning
#missing customer name
for order in clean_orders:
    if order[1] == "":
        print("Missing customer name:", order)
#7.5 String Processing
categories = []
#Displaying product categories
for order in clean_orders:
    if order[4] not in categories:
        categories.append(order[4])
print("Categories:",categories)
#Identifying products containing the word "top"
for order in clean_orders:
    if "top" in order[3].lower():
        print("Product containing 'top':",order[3])
#Converting customer names to uppercase
for order in clean_orders:
    order[1] = order[1].upper()
#Extracting year from order dates
for order in clean_orders:
    year = order[8].split("-")[0]
    print("Order Year:",year)
#7.6 Conditional Analysis
#Orders where price exceeds 30,000
for order in clean_orders:
    if order[5] > 30000:
        print("High price order:",order)
#Orders with Cancelled status
for order in clean_orders:
    if order[7] == "Cancelled":
        print("Cancelled order:",order)
#Categorize orders based on value:
for order in clean_orders:
    total = order[9]

    if total > 50000:
        category = "High Value"
    elif total > 10000:
        category = "Medium Value"
    else:
        category = "Low Value"

    print(order[0],category)
#7.7 List Processing
#Extract product names
products = []
for order in clean_orders:
    products.append(order[3])
print(products)
#Identify unique cities
cities = []
for order in clean_orders:
    if order[2] not in cities:
        cities.append(order[2])
print("Cities:",cities)
#Count total orders
print("Total Orders:",len(clean_orders))
#Sort orders based on price
sorted_orders = sorted(clean_orders, key=lambda x: x[5])
for order in sorted_orders:
    print(order)
#7.8 Dictionary Analysis
orders_city = {}
#Order count per city
for order in clean_orders:
    city = order[2]

    if city in orders_city:
        orders_city[city] += 1
    else:
        orders_city[city] = 1
print(orders_city)
#Order count per category
orders_category = {}

for order in clean_orders:
    cat = order[4]

    if cat in orders_category:
        orders_category[cat] += 1
    else:
        orders_category[cat] = 1
print(orders_category)
#Total revenue per category
revenue_category = {}

for order in clean_orders:
    cat = order[4]
    total = order[9]

    if cat in revenue_category:
        revenue_category[cat] += total
    else:
        revenue_category[cat] = total
print(revenue_category)
#7.9 Functions
#calculate_total(price, quantity) Returns total order value.
def calculate_total(price,quantity):
    return price * quantity
#get_high_value_orders(orders)
#Returns orders exceeding a specified value threshold.
def get_high_value_orders(orders):
    result = []

    for order in orders:
        if order[9] > 50000:
            result.append(order)

    return result
# orders_by_city(orders, city)
def orders_by_city(orders,city):
    result = []

    for order in orders:
        if order[2] == city:
            result.append(order)

    return result
#7.10 Lambda Functions
#Sorting orders by total amount
sorted_orders = sorted(clean_orders, key=lambda x: x[9])
#Extracting price values
prices = list(map(lambda x: x[5], clean_orders))
print(prices)
#Identifying maximum order value
max_order = max(clean_orders, key=lambda x: x[9])
print("Max order:",max_order)
#7.11 Error Handling
try:
    price = float("abc")
except ValueError:
    print("Invalid numeric value")
else:
    print("Conversion success")
finally:
    print("Execution completed")
#7.12 Data Export
with open("clean_orders.csv","w") as file:

    header = "order_id,customer_name,city,product,category,price,quantity,order_status,order_date,total_amount\n"
    file.write(header)

    for order in clean_orders:
        line = ",".join(map(str,order))
        file.write(line + "\n")