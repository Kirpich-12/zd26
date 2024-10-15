from math import sqrt

data_s =  open('input.txt', 'r')
data = data_s.read()
x1, y1, r1, x2, y2, r2 = data.split()

x1, y1, r1, x2, y2, r2 = int(x1), int(y1), int(r1), int(x2), int(y2), int(r2)

if sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) - r1 - r2 <= 0 and r1 - sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) - r2 <= 0 and r2 - sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) - r1 <= 0:
    ans = "YES"
else:
    ans = 'NO'


output_data = open('output.txt', 'w')
output_data.write(ans)
#запись

data_s.close()
output_data.close()
#ОБЯЗАТЕЛЬНО не забывать