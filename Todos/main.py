todos = []

while True:
    user_action = input("Type add, show, edit, complete ,exit: ")

    match user_action.strip().lower():
        case "add":
            user_todo = input("Enter Todo: ")
            todos.append(user_todo)
        case "show":
            for index,todo in enumerate(todos):
                print(index+1,todo)
        case "edit":
            editCode = int(input("Number of the todo to edit: "))
            editCode-=1
            new_todo = input("Enter the New Todo: ")
            todos[editCode] = new_todo
            print("List has been Updated!")
        case "complete":
            index = int(input("Enter the Number of Complete Item: "))
            print(f"{todos.pop(index - 1)} is Completed!!")
        case "exit":
            break
print("Bye!")