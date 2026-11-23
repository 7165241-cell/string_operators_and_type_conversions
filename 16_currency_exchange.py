amount_shekels = float(input( "Enter amount in shekels: "))
usd_rate = 3.25
Euro =3.75
commission = 0.2
dollar = amount_shekels // usd_rate
is_Euro = amount_shekels // Euro
commission_dollar = dollar * commission
commission_euro = is_Euro * commission
print(f"""
dollar: {dollar}
is_Euro: {is_Euro}
commission_dollar: {commission_dollar}
commission_euro: {commission_euro}
""")
