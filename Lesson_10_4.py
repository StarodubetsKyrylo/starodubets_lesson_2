# Завдання 4
# Створіть магазин канцтоварів використовуючи списки для зберігання
# елементів. Для додавання елементів створіть функцію, яка буде
# запитувати дані в користувача і зібрані дані у вигляді кортежу
# додавати у створений список на початку. Результат вивести на екран.
# Під час створення дотримуйтесь правил специфікації PEP 8.

office_supplies_store = []  # create empty list


def data_to_store():
    """Function collect and add data
    to the list 'office_supplies_store'
    """
    while True:
        try:  # input data
            user_name = input("Enter your name:")
            user_needs = input("Enter your needs:")
        except ValueError:  # check value exceptions
            print("Wrong value!")

        # Create tuple and add to the first place of list
        tuple_data = tuple(user_name.split()) + tuple(user_needs.split())
        if len(tuple_data) > 0:
            office_supplies_store.insert(0, tuple_data)

        # repeat or break the program
        answer = input("\nEnter 'stop' if you wont break or continue:")
        if answer == "stop":
            break


data_to_store()  # call function

print(f"Office list: {office_supplies_store}")  # print list
