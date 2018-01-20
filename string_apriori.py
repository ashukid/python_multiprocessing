file_name="transaction.txt"

with open(file_name) as file:
    default=file.read().splitlines()

data=[]
for s in default:
    data.append(list(map(str,s.split(';'))))

print(data)