name = input("enter a first name: ")#שם לקוח 
name_prodact = input("entaer a name a prodact: ")#שם מוצר
price_prodact = float(input("enter a price prodact: "))#מחיר מוצר
amount_prodact = int( input("enter a amount prodact: "))#כמת מוצר
Discount_Percentage =float (input("enter aDiscount Percentage 1.-: "))#אחוז הנחה

VAT = 1.18
prodect = name_prodact.upper() #שם מוצר באותיות גדולו
Subtotal= price_prodact * amount_prodact #מחיר הקנייה המקורי
Discount_Amount =  Subtotal * Discount_Percentage / 100 #סכןם ההנחה
amont = Subtotal - Discount_Amount # סכום לאחר הנחה
total = amont * VAT 
print(f"""
================================
          PURCHASE INVOICE
================================

Customer: {name}
Product: {prodect}
Unit Price: {price_prodact}
Quantity: {amount_prodact}
Subtotal: {Subtotal}
Discount: {Discount_Amount}
After Discount: {amont}
VAT: 18%

TOTAL: {total:.2f}

================================
       THANK YOU FOR SHOPPING
================================


""")