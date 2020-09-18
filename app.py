import streamlit as st

def main():
    st.title('''Epsilon tech presents: Q analytics''')
    st.sidebar.radio('select an option',['Track all people', 'Select people to track'])

if __name__ == "__main__":
    main()
