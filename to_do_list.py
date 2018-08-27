import sqlite3

def change_the_list():
    users_input = input("Co chcesz zrobić? ")
    if users_input == 'NEW':
        task_text = input("Wpisz treść zadania: ")
        connection.execute("INSERT INTO TO_DO_LIST (TASK) VALUES (?)", (task_text,))
        connection.commit()

    if users_input == 'CHANGE':
        id_number = input("Wpisz numer zadania, które chcesz zmienić: ")
        new_task = input("Wpisz nową treść zadania: ")
        connection.execute("UPDATE TO_DO_LIST set TASK = ? WHERE ID = ?", (new_task, id_number))
        connection.commit()

    if users_input == "CLEAR":
        id_number = input("Wpisz numer zadania, które chcesz usunąć: ")
        connection.execute("DELETE FROM TO_DO_LIST WHERE ID = ?", id_number)
        connection.commit()

    if users_input == "EXIT":
        quit()

connection = sqlite3.connect('tasks.db')

# connection.execute('''CREATE TABLE TO_DO_LIST
#          (id integer primary key autoincrement,
#          task varchar(50))''')
#
# connection.execute("INSERT INTO TO_DO_LIST (TASK) \
#       VALUES ('Wstawić pranie' )")
#
# connection.execute("INSERT INTO TO_DO_LIST (TASK) \
#       VALUES ('Zrobić zakupy' )")
#
# connection.execute("INSERT INTO TO_DO_LIST (TASK) \
#       VALUES ('Ugotować obiad' )")
#
# connection.commit()


cursor = connection.execute("SELECT id, task from TO_DO_LIST")
for row in cursor:
   print(row[0] , row[1])

change_the_list()

connection.close()