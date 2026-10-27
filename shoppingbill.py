product1="shirt"
price1=1000
quantity1=1
product2="shoes"
price2=2000
quantity2=2
product3="bed sheets"
price3=500
quantity3=3
total_shirts=price1*quantity1
total_shoes=price2*quantity2
total_bed_sheets=price3*quantity3
total_price=total_shirts+total_shoes+total_bed_sheets
total_discount=total_price*10/100
final_bill=total_price-total_discount
print(f"product1:{product1},price1:{price1},quantity1:{quantity1}")
print(f"product2:{product2},price2:{price2},quantity2:{quantity2}")
print(f"product3:{product3},price3:{price3},quantity3:{quantity3}")
print("total no.of shirts:",quantity1)
print("total no.of shoes:",quantity2)
print("total no.of bed_sheets:",quantity3)
print("total_price:",total_price)
print("total_discount:",total_discount)
print("final_bill:",final_bill)
print(f"we bought the products like {product1},{product2},{product3} and their total price is {total_price} and the total discount is {total_discount} and the final bill is {final_bill}")
