import math

def _float(val):
    return float(val.replace(',', '.'))

lon = _float(input())
lat = _float(input())
n = int(input())

d = float('inf')
data = {}
name = ''
for i in range(n):
    defib = input().split(';')
    
    lng, lati = _float(defib[-2]), _float(defib[-1])
    x = (lng-lon)*math.cos((lat+lati)/2)
    y = lati-lat
    
    if d > math.sqrt(x**2 + y**2):
        d = math.sqrt(x**2 + y**2)
        name = defib[1]

print(name)