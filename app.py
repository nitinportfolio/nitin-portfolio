import streamlit as st
import requests
from PIL import Image
from streamlit_lottie import st_lottie

st.set_page_config(page_title = 'My Portfolio', page_icon = ":telescope:", layout = "wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

# USE LOCAL CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

local_css("style/style.css")
# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_3rwasyjy.json")
img_recommendation = Image.open("images/movie.jpg")
img_olympics = Image.open("images/olympics.png")

#------Header Section------#

with st.container():


    st.subheader("Hi, I am Nitin :wave:")
    st.title("A Data Scientist from India")
    st.write("I am passionate about Data Science & Machine Learning & its applications in "
             "Businesses & Humans. I would really like to work on Cognitive Artificial Intelligence")
    st.write("[Learn More >](https://Google.com)")

with st.container():
    st.write("--------")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write("""
        BlaBla Bla blabalbal blabal bla & more blaBlaBla Bla blabalbal blabal bla & more bla
        - BlaBla Bla blabalbal blabal bla & more bla
        - BlaBla Bla blabalbal blabal bla & more bla
        - BlaBla Bla blabalbal blabal bla & more bla
        - BlaBla Bla blabalbal blabal bla & more bla
        
        if this sounds interesting to you, please BlaBla Bla blabalbal blabal bla & more bla some more
        
        """)

    with right_column:
        st_lottie(lottie_coding, height = 300, key = "coding")

        #---- PROJECTS ----#
with st.container():

    st.write("---")
    st.header("My Data Science Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_recommendation)
    with text_column:
        st.subheader(" Movie Recommender System")
        st.write(
            """
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
            """
        )
        st.markdown("[Watch GitHub Repo](https://github.com/nitinportfolio/gitportfolio.git)")

    st.write("#")
    st.write("#")
    st.write("##")
with st.container():

    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_olympics)
    with text_column:
        st.subheader(" Movie Recommender System")
        st.write(
            """
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
            """
        )
        st.markdown("[Watch GitHub Repo](https://github.com/nitinportfolio/gitportfolio.git)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https??formsubmit.com/ !!!
    contact_form = """
    <form action="https://formsubmit.co/nitinportfolio.ai@gmail.com" method="POST">
    <input type = "hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder = "Your Name" required>
     <input type="email" name="email" placeholder = "Your Email" required>
     <textarea name = "message" placeholder = Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html = True)
    with right_column:
        st.empty()



