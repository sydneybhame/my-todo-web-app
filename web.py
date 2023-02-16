import streamlit as st
import functions
import time

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


clock = time.strftime("%a %b %d %I:%M%p")

st.title("My Todo App")
st.subheader(clock)
st.write("I get to: ")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="I would like to...", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')