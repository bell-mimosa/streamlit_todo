import streamlit as st
import streamlit.components.v1 as components
# ターミナルで streamlit run streamlit_todo.py と打つと開く

components.html(
    """
    <script>
        document.documentElement.lang = 'ja';
    </script>
    """,
    height=0,
)
st.set_page_config(
    page_title="ToDo List",
)

# Todo追加用関数
def add_todo():
    if st.session_state.new_todo:
       st.session_state.todos.append({"task": st.session_state.new_todo, "done": False})
       st.session_state.new_todo = ""

st.title("ToDo List")

if 'todos' not in st.session_state:
    st.session_state.todos = []

st.text_input("新しいタスクを入力してください", key="new_todo")
# st.session_state.new_todoに一時保存される
st.button("タスクを追加", on_click=add_todo)
# add_todo関数を呼び出す

st.subheader("未完了のタスク")
for index, todo in enumerate(st.session_state.todos):
    if not todo["done"]:
        col1, col2 = st.columns([0.9, 0.1])
        # 分割後の領域の名前1,2 = st.columns([割合,割合]) → 画面を左右に分割
        col1.write(todo["task"])
        if col2.button("完了", key=f"done_{index}"):
           #f"" → f-string(Python) :文字列に変数を埋め込む方法
           #JSでいう``(バッククォート)
           st.session_state.todos[index]["done"] = True
           st.rerun()

st.subheader("完了済みのタスク")
for index, todo in enumerate(st.session_state.todos):
    # for index, リスト内要素 in enumerate(リスト):リスト内の要素を1つずつ処理する
    if todo["done"]:
        col1, col2 = st.columns([0.9, 0.1])
        col1.write(f"~~{todo['task']}~~") #打消し線
        if col2.button("削除", key=f"delete_{index}"):
            del st.session_state.todos[index]
            st.rerun()
