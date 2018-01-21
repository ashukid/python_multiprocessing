import itertools

# finle input and converting string values into list
# file_name="transaction.txt"
file_name="categories.txt"
threshold=0.01
with open(file_name) as file:
    default=file.read().splitlines()
data=[]
for s in default:
    data.append(list(map(str,s.split(';'))))
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
        support.append(float(count)/total_rows)


    flag=0
    new_candid=[]
    for i in range(len(support)):
        if(support[i]>=threshold):
            flag=1
            frequent_set.append(all_candid[i])
            new_candid.append(all_candid[i])
            support_set.append(support[i])

    if (flag==0):
        return 0
    new_unique=set()
    for i in range(len(new_candid)):
        for values in new_candid[i]:
            new_unique.add(values)
    return list(new_unique)



# global variables
epoch=1
current_unique=set()
for i in range(total_rows):
    for values in data[i]:
        current_unique.add(values)
current_unique=list(current_unique)

# while True: # use this line while finding all frequent sets (part2) and comment below line
for i in range(1): # use this line while finding level-1 frequent set (part1) and comment above line
    unique=calculate_frequent_set(epoch,current_unique)
    if(unique==0):
        break
    current_unique=unique
    epoch+=1

write_file=open("custom_pattern.txt","w")
    
# printing the generated candidate for part 1
# print(len(frequent_set))
for i in range(len(frequent_set)):
	write_file.write("{}:{}\n".format(int(support_set[i]*total_rows),frequent_set[i][0]))


# printing the generated candidate for part 2
# for i in range(len(frequent_set)):
#     print("{}:{}".format(int(support_set[i]*total_rows),frequent_set[i][0]))
#     for j in range(1,len(frequent_set[i][0])):
#         print(";{}".format(frequent_set[i][0][j]))

write_file.close()


