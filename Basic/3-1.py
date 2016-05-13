width=15

price_width=5
item_width=width-price_width

header_format = '%-*s%*s'
price_format='%-*s%*.2f'

print '='*width

print header_format % (item_width,'Item',price_width,'Price')

print '-'*width

print price_format%(item_width,'Apples11111',5,0.4)


print '='*width
