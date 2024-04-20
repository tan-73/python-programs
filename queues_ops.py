# lst1 = [34, 52, 69, 420, 18]
# ele = int(input("Enter an element : "))
lst1 = [23, 47]
lst2 = []
lst3 = [1, 9]
def enqueue() :
    ele = int(input("Enter an element : "))
    priority = input("Enter the priority (H/N/L) : ") 
    if priority == "H" : 
        lst1.append(ele)
    elif priority == "N" : 
        lst2.append(ele)
    elif priority == "L" : 
        lst3.append(ele)
        
def dequeue() : 
    # pos = int(input("Enter the position : "))
    priority = input("Enter the priority : ")
    if priority == "high" :
        del lst1[0]
    elif priority == "medium" : 
        del lst2[0]
    elif priority == "low" : 
        del lst3[0]

def display() : 
    print(lst1)
    print(lst2)
    print(lst3)

def search(search_ele) : 
    if search_ele in lst1 : 
        return 1
    elif search_ele in lst2 : 
        return 2
    elif search_ele in lst3 : 
        return 3

def change() : 
    change_ele = int(input("Enter the element to be changed : "))
    search_cond = search(change_ele)
    print(search_cond)
    new_priority = input("Enter the new priority : ")
    if new_priority == "high" : 
        lst1.append(change_ele)
    elif new_priority == "medium" : 
        lst2.append(change_ele)
    elif new_priority == "low" : 
        lst3.append(change_ele)
    

def choice() : 
    while True : 
        print("Enter your choice : \n1. Insert Element \n2. Search for Element\n 3. Change Priority\n 4. Display queues")
        ch = int(input("Enter your choice : "))
        if ch == 1 : 
            enqueue()
        elif ch == 2 : 
            search()
        elif ch == 3 : 
            change()
        elif ch == 4 :
            display()
# main
choice()