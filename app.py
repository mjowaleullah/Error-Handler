import streamlit as st
from api_calling import bug_explatation, debug
from PIL import Image

st.title("Hey! Error Debugger is Here...", anchor=False)
st.divider()


with st.sidebar:
    image = st.file_uploader("Upload Your Error Screenshot...",
                            type = ["jpeg", "jpg", "png"],
                            accept_multiple_files = False)

    if image:
        st.image(image)
        pil_img = Image.open(image)




    solution = st.selectbox("Select your solution Type.",
                            options=["Hints", "Solution with Code"],
                            index=None)

    button = st.button("**Submit and initiate with AI**", type="primary")


if button:
    if not image:
        st.error("Please Insert screenshot")
    if not solution:
        st.error("Please Select Solution Type.")

    if image and solution:

        with st.container(border=True):
            st.header("This Issue", anchor=False)
            with st.spinner("Processing Your Image..."):
                issue = bug_explatation(pil_img)
                st.markdown(issue)

        st.divider()

        with st.container(border=True):
            st.header("The Solution", anchor=False)
            with st.spinner("Processing Your Solution..."):
                bug = debug(pil_img, solution)
                st.markdown(bug)
