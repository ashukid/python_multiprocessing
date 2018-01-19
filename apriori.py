import itertools
from itertools import chain
threshold=0.25
confidence=1

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
def calculate_frequent_set(epoch,last_unique):
    # print(last_unique,epoch)
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
    unique=calculate_frequent_set(epoch,current_unique)
    if(unique==0):
        break
    current_unique=unique
    epoch+=1
    
print("Frequent set : {} with suuport : {}".format(frequent_set,support_set))

candid_support={}
for i in range(len(frequent_set)):
    candid_support[frequent_set[i]]=support_set[i]


def calculate_assoc_rule(frequent_set,support_set):

    for i in range(len(frequent_set)):
        current_element=set(frequent_set[i])
        all_candid=[]
        for j in range(1,len(current_element)):
            all_candid.append(map(set,itertools.combinations(current_element,j)))

        all_candid=list(chain.from_iterable(all_candid))

        for j in range(len(all_candid)):
            current_candid=all_candid[j]
            remain_candid=current_element-current_candid
            total_candid=current_candid.union(remain_candid)
            total_candid=tuple(total_candid)
            current_candid=tuple(current_candid)
            remain_candid=tuple(remain_candid)

            current_confidence=candid_support[total_candid]/float(candid_support[current_candid])
            if(current_confidence>=confidence):
                print("Assoc rule {} --> {} with Confidence : {}".format(current_candid,remain_candid,current_confidence))

calculate_assoc_rule(frequent_set,support_set)