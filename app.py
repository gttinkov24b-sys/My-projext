import sreamlit as st
st.title("my first app(maybe)")
name = st.text_input("What your name: ")
if name:
  st.write(f"Hello {name}!")
