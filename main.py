import streamlit as st
import json
import os

TODO_FILE = "todo.json"  # Define the filename where tasks are stored


# Function to load tasks from the JSON file
def load_tasks():
    if not os.path.exists(TODO_FILE):  # Check if file exists
        return []  # If not, return an empty list
    with open(TODO_FILE, "r") as file:  # Open the file in read mode
        return json.load(file)  # Load and return the JSON data as a Python list

# Function to save tasks to the JSON file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:  # Open the file in write mode
        json.dump(tasks, file, indent=4)  # Save tasks as formatted JSON

def add():
    new_task = st.text_input("Add new task")
    if st.button("Add Task") and new_task:
     tasks = load_tasks()  # Load existing tasks
     tasks.append({"task": new_task, "done": False})  # Append a new task (default: not done)
     save_tasks(tasks)  # Save the updated tasks
     st.rerun() # Print a success message


def remove_list():
    st.write("----")
    tasks = load_tasks()  # Load existing tasks
    for i , task in enumerate(tasks):
        col1, col2, col3 = st.columns([0.1,0.7,0.2])
        with col1:
            is_done= st.checkbox("",value=task["done"], key=f"done_{i}") #checks if the user just clicked the checkbox,
            if is_done != task["done"]: #if clicked so mark as completed or if not clicked so incomplete 
                tasks[i]["done"] = is_done
                save_tasks(tasks)# Save the updated tasks
                st.rerun()  # Print a success message
        with col2:
            if task["done"]:
                st.markdown(f"~~{task['task']}~~")
            else:
                st.write(task["task"])
        with col3:
            if st.button("Remove", key=f"remove_{i}"): #to remove task 
                tasks.pop(i)
                save_tasks(tasks)# Save the updated tasks
                st.rerun() # Print a success message
            
            if task["done"]:
                if st.button("Reset", key=f"reset_{i}"): #to reset task as incomplete
                    tasks[i]["done"]= False
                    save_tasks(tasks)# Save the updated tasks
                    st.rerun() # Print a success message
    if not tasks:  # If there are no tasks
       st.info("Your To-do list is empty")

def main():
    st.title("MY STREAMLIT TODO LIST")
    add()
    remove_list()

# This tells Python to run the main() function when the script is executed
if __name__ == "__main__":
    main()
