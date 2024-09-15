items_list = []
items_list=["Speaker","mic","mobile","laptop"]

print(items_list)
print(items_list[2])
a=items_list[-1]
print(a)

## Slicing a list:

print(items_list[2:3])

## Modifying a List
items_list.append("Macbook")
items_list.append("Iphone")

print(items_list)

## Checking for existence
#are Iphone in the list ?
print("Iphone" in items_list )

# Length of list:
len(items_list)

# List Comprehension

Score = [70,80,90,121,251]
for i in Score:
    print(i/2)
