

sales_data = [
    [200, 150, 300], # product A sales list
    [100, 350, 600],
    [600, 500, 400],
]

daily_totals = (sum(day) for day in sales_data)
print(f" total sales for 1 day in ${next(daily_totals)}")
print(f" total sales for 2 day in ${next(daily_totals)}")
print(f" total sales for 3 day in ${next(daily_totals)}")
product_total = list(map(sum, sales_data))
print(product_total)

unique_data = set()
for product in sales_data:
    for sales in product: 
        unique_data.add(sales)

print("unique sales data:", sorted(unique_data,reverse=True))
