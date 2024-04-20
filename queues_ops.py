import time
import psutil

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
    if queue_name == "H" : 
        HighestPr.remove(element)
    elif queue_name == "N" :
        NormalPr.remove(element)
    elif queue_name == "L" : 
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
    process = psutil.Process()
    start_time = time.time()
    while True : 
        print("\n1. Insert Element")
        print("2. Search for Element")
        print("3. Change Priority")
        print("4. Display Queues")
        print("5. Exit")
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
        elif ch == 5 : 
            print(process.memory_info().rss)
            break
        else : 
            print("Wrong Choice")
    end_time = time.time()
    print(end_time - start_time)


# main
choice()