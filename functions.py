FILEPATH = "C:/Users/sydne/Documents/Coding/Python/App1/py_course_main/todos.txt"

text = """
You can add in multi-line strings outside of functions.
You don't need to add in break-lines for this - it will
look the same as it does here if you print it out.
"""


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items."""
    # you don't need to write code to close a file when using
    # the 'with context manager' - it does this automatically
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Opens a text file and writes to-do items in the file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
        # no 'return' needed as we are not calling anything up


if __name__ == "__main__":
    # ^ keeps everything below from being executed in the main program
    print("Hello")
    print(get_todos())