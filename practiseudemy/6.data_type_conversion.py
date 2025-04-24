
price = "19.99"

price_float = float(price)
 
quant = int ("5")

total = price_float * quant
print(f"Price (string): {price}, type : {type(price)}")
print(f"\nprice float: {price_float}, price float : {type(price_float)}")
print(f"\nquant: {quant}, quant : {type(quant)}")
print(f"\ntotal: {total}, type : {type(total)}")