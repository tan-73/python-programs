import psutil

# Initialize queues
queues = {'H': [23, 47], 'N': [], 'L': [1, 9]}

# Function to enqueue elements
def enqueue():
    ele = int(input("Enter the element: "))
    priority = input("Enter the priority (H/N/L): ").upper()
    if priority in queues:
        queues[priority].append(ele)
    else:
        print("Invalid priority. Please enter H, N, or L.")

# Function to delete elements from a queue
def delete(element, queue_name):
    if element in queues[queue_name]:
        queues[queue_name].remove(element)
    else:
        print("Element not found in the queue.")

# Function to display all queues
def display():
    for priority, queue in queues.items():
        print(f"{priority}: {queue}")

# Function to search for an element
def search(search_ele):
    for priority, queue in queues.items():
        if search_ele in queue:
            print(f"Element found in {priority} queue.")
            return priority
    print("Element not found.")
    return None

# Function to change priority of an element
def change_priority(element, current_priority):
    new_priority = input("Enter the new priority (H/N/L): ").upper()
    if new_priority in queues:
        delete(element, current_priority)
        queues[new_priority].append(element)
    else:
        print("Invalid priority. Please enter H, N, or L.")

# Main function for user interaction
def main():
    process = psutil.Process()
    while True:
        print("\n1. Insert Element")
        print("2. Search for Element")
        print("3. Change Priority")
        print("4. Display Queues")
        print("5. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                enqueue()
            elif choice == 2:
                search_ele = int(input("Enter the element to be searched: "))
                search(search_ele)
            elif choice == 3:
                change_ele = int(input("Enter the element to change priority: "))
                current_priority = search(change_ele)
                if current_priority:
                    change_priority(change_ele, current_priority)
            elif choice == 4:
                display()
            elif choice == 5:
                print("Exiting program.")
                print("Memory usage:", process.memory_info().rss, "bytes")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Execute the main function
if __name__ == "__main__":
    main()
