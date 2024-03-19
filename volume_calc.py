total_length = 0
for i in ["가로: ","세로: ","높이: "]:
        total_length += float(input(i))
if total_length <= 80:
    total_price = 5000
elif total_length <= 100:
    total_price = 8000
elif total_length <= 120:
    total_price = 10000
elif total_length <= 160:
    total_price = 13000
print(total_price)

