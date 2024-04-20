HighestPr = [23, 47]
NormalPr = []
LowestPr = [1, 9]

def enqueue():
    ele = int(input("Enter the element: "))
    priority = input("Enter the priority (H/N/L): ").upper()
    if priority == "H":
        HighestPr.append(ele)
    elif priority == "N":
        NormalPr.append(ele)
    elif priority == "L":
        LowestPr.append(ele)
    else:
        print("Invalid priority. Please enter H, N, or L.")

def delete(element, queue_name):
    if queue_name == "H":
        remove_element(HighestPr, element)
    elif queue_name == "N":
        remove_element(NormalPr, element)
    elif queue_name == "L":
        remove_element(LowestPr, element)

def remove_element(queue, element):
    if element in queue:
        queue.remove(element)
    else:
        print("Element not found in the queue.")

def display():
    print("Highest Priority Queue:", HighestPr)
    print("Normal Priority Queue:", NormalPr)
    print("Lowest Priority Queue:", LowestPr)

def search(search_ele):
    for queue, name in [(HighestPr, "HighestPr"), (NormalPr, "NormalPr"), (LowestPr, "LowestPr")]:
        if search_ele in queue:
            print(f"Element found in {name}.")
            return name
    print("Element not found.")
    return None

def change():
    change_ele = int(input("Enter the element to be changed: "))
    search_cond = search(change_ele)
    if search_cond:
        update_priority = input("Want to increase or decrease its priority? (I/D): ").upper()
        if update_priority == "I":
            increase_priority(change_ele, search_cond)
        elif update_priority == "D":
            decrease_priority(change_ele, search_cond)

def increase_priority(element, queue_name):
    if queue_name == "H":
        print("Cannot increase priority.")
    elif queue_name == "N":
        delete(element, "N")
        HighestPr.append(element)
    elif queue_name == "L":
        delete(element, "L")
        NormalPr.append(element)

def decrease_priority(element, queue_name):
    if queue_name == "H":
        delete(element, "H")
        NormalPr.append(element)
    elif queue_name == "N":
        delete(element, "N")
        LowestPr.append(element)
    elif queue_name == "L":
        print("Cannot decrease priority.")

def choice():
    while True:
        print("\nEnter your choice:")
        print("1. Insert Element")
        print("2. Search for Element")
        print("3. Change Priority")
        print("4. Display Queues")
        print("5. Exit")
        ch = input("Enter your choice: ")
        if ch == "1":
            enqueue()
        elif ch == "2":
            search_ele = int(input("Enter the element to be searched: "))
            search(search_ele)
        elif ch == "3":
            change()
        elif ch == "4":
            display()
        elif ch == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# main
choice()
