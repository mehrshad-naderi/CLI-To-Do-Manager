#CLI-To-Do-Manager
import csv
csv_file='tasks.csv'
def display_menu():
    """
    Display the main menu options for the CLI To-Do Manager.
    """
    print("\n==============================")
    print("       CLI To-Do Manager      ")
    print("==============================")
    print("1. ➕ Add Task")
    print("2. 📋 Show Tasks")
    print("3. 🔄 Change Status")
    print("4. ❌ Delete Task")
    print("5. 🚪 Exit")
    print("==============================")
def add_task():
    """
    Add a new task with default status 'pending' to the CSV file.
    """
    title = input("Enter your task: ")
    status = "pending"
    # Open the file in append mode
    with open(csv_file, mode="a", newline="", encoding="utf-8") as file:
        fieldnames = ["title", "status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # If file is empty, write the header first
        if file.tell() == 0:
            writer.writeheader()
        # Write the new task row
        writer.writerow({"title": title, "status": status})
    print(f"\n✅ Your task '{title}' has been added with status [pending].")
def display_task():
    """
    Display all tasks from the CSV file with their index and status.
    """
    try:
        with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            tasks = list(reader)
            if not tasks:
                print("\n⚠️ No tasks found! Your list is empty.")
                return
            print("\n📋 Your Tasks:")
            print("-------------------------------")
            for idx, task in enumerate(tasks, start=1):
                status_icon = "✅" if task["status"] == "done" else "⏳"
                print(f"{idx}. {task['title']} [{status_icon}]")
    except FileNotFoundError:
        print("\n⚠️ No task file found. Please add a task first.")
def change_status():
    """
    Change the status of a specific task in the CSV file.
    """
    title = input("Enter the task title to change status: ")
    rows = []
    task_found = False
    with open(csv_file, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["title"] == title:
                old_status = row["status"]
                # Toggle between 'pending' and 'done'
                row["status"] = "done" if old_status == "pending" else "pending"
                print(f"🔄 Task '{row['title']}' status changed: {old_status} → {row['status']}")
                task_found = True
            rows.append(row)
    if not task_found:
        print(f"\n⚠️ Task '{title}' not found!")
    # Rewrite the file with updated rows
    with open(csv_file, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["title", "status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
def delete_task():
    """
    Delete a specific task from the CSV file.
    """
    title = input("Enter the task title to delete: ")
    rows = []
    deleted = False
    with open(csv_file, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["title"] == title:
                print(f"❌ Task '{row['title']}' deleted successfully!")
                deleted = True
                continue
            rows.append(row)
    if not deleted:
        print(f"\n⚠️ Task '{title}' not found!")
    with open(csv_file, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["title", "status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
def main():
    while True:
        display_menu()
        choise=int(input('Please Enter Your Choise: '))
        if choise==5:
             print('\nGood-Luck')
             break
        if choise==1:
             add_task()
        if choise==2:
             display_task()     
        if choise==3:
             change_status()
        if choise==4:
             delete_task()
if __name__ == "__main__":
     main()
     



