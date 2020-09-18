import streamlit as st

def main():
    st.title('''Epsilon tech presents: Q analytics''')
    st.sidebar.radio('select an option',['Track all people', 'Select people to track'])

    # upload video
    video_file = open('resources/queue_two_people.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)

if __name__ == "__main__":
    main()
