num_list = []
for _ in range(5):
    value = int(input("Enter a value: "))
    num_list.append(value)

target = int(input("Enter the target: "))
find_list = []

for i in range(4):
    dub=num_list[i]
    for j in range(4):

     if (dub+ num_list[j + 1]) == target:
         find_list.append((i, i + 1))

for pair in range (len(find_list)):
    print(pair[i],"and",pair[i+1])
