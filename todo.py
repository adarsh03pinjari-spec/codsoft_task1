# Task 1 - To-Do List App
# Internship: CodSoft | Python Programming Internship
# Created by Adarsh Pinjari - First Year CSE Student

tasks = [] # List to store task dictionaries

def display_menu():
    print("\n=== WELCOME TO ADARSH’S TO-DO LIST APP ===")
    print("1. ➕ Add New Task")
    print("2. 📋 View All Tasks")
    print("3. ✅ Mark Task as Complete")
    print("4. 🗑️ Delete a Task")
    print("5. 🚪 Exit")

def add_new_task():
    task = input("🆕 Enter a task to add: ")
    tasks.append({"task": task, "done": False})
    print("🎉 New task added!")

def view_tasks():
    if not tasks:
        print("⚠️ No tasks found.")
        return
    print("\n📋 Your Current Tasks:")
    for i, t in enumerate(tasks):
        status = "✔️" if t["done"] else "❌"
        print(f"{i + 1}. [{status}] {t['task']}")

def mark_task_done():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("🔢 Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print("👍 Task marked as completed!")
        else:
            print("🚫 Invalid task number.")
    except ValueError:
        print("❗ Please enter a valid number.")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("🗑️ Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"🗑️ Deleted: {removed['task']}")
        else:
            print("🚫 Invalid task number.")
    except ValueError:
        print("❗ Please enter a valid number.")

# Main program loop
while True:
    display_menu()
    choice = input("👉 Choose an option (1-5): ")

    if choice == '1':
        add_new_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_task_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("👋 Thank you for using Adarsh’s To-Do App. Stay organized!")
        break
    else:
        print("🚫 Invalid choice. Please select between 1 to 5.")
