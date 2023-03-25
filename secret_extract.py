import seven

with open("digital.csv") as f:
	data = f.readlines()
data = [i.strip() for i in data[1:]]
data = [i.split(",")[1:] for i in data]
data = [i for i in data if i[1]=='1']


print(data)

for i,d in enumerate(data):
	seven.decode(d)
	if i %2 == 1:
		print("-"*10)

