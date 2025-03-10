import streamlit as st
from dataBase import *
from PIL import Image
#Code for creating a new discussion post
def createDiscussionPost():
    with st.form("new_post_form"):
            user = st.text_input("Your Name (Optional)", max_chars=50, placeholder="Enter")
            role = st.text_input("Your Role (Optional)", max_chars=50, placeholder="Enter")
            content = st.text_area("Write your message here...")
            submit = st.form_submit_button("Post")
            if submit:
                if content.strip():  
                    addPost(user, role, content)
                    st.success("Message posted!")
                    st.rerun()
                else:
                    st.warning("Message cannot be empty.")

#Code for managing a pre existing discussion post (Display, Delete, React etc.)
def managingDiscussionPost():
    st.image(image= Image.open("logo.jpeg"))
    st.subheader(" Recent Posts")
    searchQuery = st.text_input("🔍 Search messages", placeholder="Enter keyword...")
    postsDF = getPosts(searchQuery)

    if not postsDF.empty:
        for _, row in postsDF.iterrows():
            with st.container():
                st.markdown(f"**{row['user']}** ({row['role']}) 🕒 {row['timestamp']}")
                st.write(row["content"])

                    # Like / Dislike Buttons
                colLike, colDislike, colUndo, colDelete = st.columns([1, 1, 1, 1])
                    
                with colLike:
                    if st.button(f"👍 {row['likes']}", key =f"likes{row['id']}"):
                        updateReaction(row['id'], like =True)
                        st.rerun()

                with colDislike:
                    if st.button(f"👎 {row['dislikes']}", key=f"dislikes{row['id']}"):
                        updateReaction(row['id'], dislike = True)
                        st.rerun()
                
                with colUndo:
                    if st.button(f"Undo Last Action", key=f"undo{row['id']}"):
                        updateReaction(row['id'], undo = True)
                        st.rerun()
                    
                with colDelete:
                    if st.button("🗑️ Delete", key=f"delete_{row['id']}"):
                        deletePost(row['id'])
                        st.warning("Message deleted!")
                        st.rerun()

                st.markdown("---")
    else:
            st.write("No messages found.")