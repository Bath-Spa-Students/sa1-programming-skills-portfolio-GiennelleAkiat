
# ----------- HOMO LIST
# names = ["Giennelle", "Bathspa", "Code Lab 1"]
# print(names[:1])
# print(names[1])

# ----------- HETRO LIST
# student = ["Giennelle", "17", "5'2"]
# print(student)
# # The count always starts at 0 unless you add a 1 or typed in [:1]

# ----------- ADDING TO LIST
# List = ["2 Apple", "2 Oranges"]
# print(List)
# added_item = input("Add another item to the list: ")
# List.append(added_item)
# print(List)

# ----------- CREATING LIST USING WHILE LOOP

print("Type '0' to stop.")
CreateList = True
List = []

while CreateList == True:
    items = input("Input items to add to the list: ")
    items = items.capitalize()

    if items != '0':       
        List.append(items)
    else:
        print(List) 
        for index, item in enumerate(List):
            print(f"{index+1}. {item}")
        CreateList = False
        break
    