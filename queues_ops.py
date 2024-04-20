# HighestPr = [34, 52, 69, 420, 18]
# ele = int(input("Enter an element : "))
HighestPr = [23, 47]
NormalPr = []
LowestPr = [1, 9]
def enqueue() :
    ele = int(input("Enter the element : "))
    priority = input("Enter the priority (H/N/L) : ") 
    if priority == "H" : 
        HighestPr.append(ele)
    elif priority == "N" : 
        NormalPr.append(ele)
    elif priority == "L" : 
        LowestPr.append(ele)
        
def delete(element, queue_name) :
    if queue_name == 1 : 
        HighestPr.remove(element)
    elif queue_name == 2 :
        NormalPr.remove(element)
    elif queue_name == 3 : 
        LowestPr.remove(element)

def display() : 
    print(HighestPr)
    print(NormalPr)
    print(LowestPr)

def search(search_ele) : 
    if search_ele in HighestPr : 
        print("Element found in HighestPr")
        return "H"
    elif search_ele in NormalPr : 
        print("Element found in NormalPr")
        return "N"
    elif search_ele in LowestPr : 
        print("Element found in LowestPr")
        return "L"
    else :
        print("Element not found")
        return 0

def change() : 

    change_ele = int(input("Enter the element to be changed : "))
    search_cond = search(change_ele)
    if search_cond == 0 : 
        return 0
    update_priority = input("Want to increase or decrease it's priority? (I/D) : ")


    
    if update_priority == "I" : 
        if search_cond == "H" : 
            print("Cannot increase priority")
            return 0
        elif search_cond == "N" : 
            delete(change_ele, search_cond)
            HighestPr.append(change_ele)
        elif search_cond == "L": 
            delete(change_ele, search_cond)
            NormalPr.append(change_ele)
    elif update_priority == "D" : 
        if search_cond == "H" : 
            delete(change_ele, search_cond)
            NormalPr.append(change_ele)
        elif search_cond == "N" : 
            delete(change_ele, search_cond)
            LowestPr.append(change_ele)
        elif search_cond == "L" : 
            print("Cannot decrease priority")
            return 0

def choice() : 
    while True : 
        print("Enter your choice : \n1. Insert Element \n2. Search for Element\n 3. Change Priority\n 4. Display queues")
        ch = int(input("Enter your choice : "))
        if ch == 1 : 
            enqueue()
        elif ch == 2 : 
            search_ele = int(input("Enter the element to be searched : "))
            search(search_ele)
        elif ch == 3 : 
            change()
        elif ch == 4 :
            display()
# main
choice()