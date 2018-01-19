import itertools
threshold=0.25
confidence=0.5

file_name="transaction.txt"

with open(file_name) as file:
    default=file.read().splitlines()

data=[]
for s in default:
    data.append(list(map(int,s.split())))

total_rows=len(data)

frequent_set=[]
support_set=[]
# class for calculating the frequent set
def calculate(epoch,last_unique):
    print(last_unique,epoch)
    all_candid=list(itertools.combinations(last_unique,epoch)) # candid geenration

    support=[]
    for i in range(len(all_candid)):
        count=0
        for j in range(total_rows):
            if(set(all_candid[i]).issubset(data[j])):
                count+=1        
        support.append(float(count)/5)
        support_set.append(float(count)/5)


    flag=0
    new_candid=[]
    for i in range(len(support)):
        if(support[i]>=threshold):
            flag=1
            frequent_set.append(all_candid[i])
            new_candid.append(all_candid[i])
    
    if (flag==0):
        return 0
    new_unique=set()
    for i in range(len(new_candid)):
        for values in new_candid[i]:
            new_unique.add(values)
    return list(new_unique)



# global variable
epoch=1
current_unique=set()
for i in range(total_rows):
    for values in data[i]:
        current_unique.add(values)
current_unique=list(current_unique)
while True:
# for i in range(6):
    unique=calculate(epoch,current_unique)
    if(unique==0):
        break
    current_unique=unique
    epoch+=1
    
print("frequent set is : {}, {}".format(frequent_set,support_set))

