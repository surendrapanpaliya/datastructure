
import DoublyLinkedListModule

#help(DoublyLinkedListModule)

# dir(DoublyLinkedListModule)

dll = DoublyLinkedListModule.DoublyLinkedList()


Menu = '''
Select following Data Structure Operation:
1. Append Data
2. Access data by Index
3. Delete data
4. Display DLL data
5. Exit from Menu
6. Select Choice from 1..5 only'''

while True:
    print(Menu)
    option = int(input("Enter option 1..6"))
    if option == 1:
        print("Append data")
        data = input("Enter book name:")
        dll.append(data)
    elif option == 2:
        print("Access first book by index",dll.get(0))
    elif option == 3:
        print("Delete Data")
    elif option == 4:
        print("Doubly Linked List is",dll)
        break
    elif option == 5:
        print("Exit from Menue")
        break
    else:
        print("Select choice from 1--5 only")
