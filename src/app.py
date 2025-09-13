import json
from pathlib import Path

DATA_FILE = Path("data/tasks.json")

def load_tasks():
    """Load tasks from JSON file."""
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def display_tasks(tasks):
    """Print all tasks."""
    if not tasks:
        print("\n✅ No tasks yet!")
    else:
        print("\n📋 Your Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()
    while True:
        display_tasks(tasks)
        print("\nOptions: [a] Add | [r] Remove | [q] Quit")
        choice = input("Choose an option: ").lower()

        if choice == "a":
            task = input("Enter new task: ").strip()
            if task:
                tasks.append(task)
                print(f"➕ Task added: {task}")
        elif choice == "r":
            try:
                idx = int(input("Enter task index to remove: "))
                removed = tasks.pop(idx)
                print(f"🗑 Removed: {removed}")
            except (ValueError, IndexError):
                print("⚠ Invalid index.")
        elif choice == "q":
            save_tasks(tasks)
            print("💾 Tasks saved. Goodbye!")
            break
        else:
            print("⚠ Invalid option. Try again.")

if __name__ == "__main__":
    main()
