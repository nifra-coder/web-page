import requests
#-from PIL import images
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
st.set_page_config(page_title="welcome to my webpage", page_icon=":tada:", layout="wide")

# def load_lottieurl(url):
       
#        r=requests.get(url)

#        if r.status_code !=200:
#         return None
#         return r.json

# #------load assets------
lottie_coding ="https://cdnl.iconscout.com/lottie/premium/preview-watermark/coding-5598277-4679571.mp4"
#--- side bar--
# with st.sidebar:
#     selected = option_menu(
#         menu_title="Main Menu", #required
#         options=["Home", "Projects" , "Contact"], #required
#         icons=["house","book","envelope"],#optional
#         menu_icon="cast",#optional
#         default_index=0,#optional
#     )
# 2.horizontal menu

selected = option_menu (
        menu_title=None, #required
        options=["Home", "Projects" , "Contact"], #required
        icons=["house","book","envelope"],#optional
        menu_icon="cast",#optional
        default_index=0,#optional
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important"},
            "icon":{"color": "white","fontsize":"25px"},
            "nav-link":{
                "font-size":"17px",
                "margin-top": "1px",
                "--hover-color":"#eee"

            }

        }
    )


if selected == "Home" :
    st.write(f" {selected}")

if selected == "Projects" :
    st.write(f" {selected}")

if selected == "Contact" :
    st.write(f"{selected}")


# ------ HEADER SECTION------
st.subheader("NIFRA CODER...")
st.header("Hi, I am Noorunisha Afrin.M :wave:")

st.write(" I'm a student currently pursuing my B.Com CA degree at Madras university,Institute pf Distance Education."
         "In the realm of programming languages, I have delved into the intricacies of both java and python,"
         "gaining valuable insights and proficiency.")

st.write("My journey extends beyond theoretical knowledge as i have, hands-on experiance with various tools and"
         "applications,including Streamlit,PyCharm,Chatgpt,and Anvil. These experiance showcase my versatility "
         "in the programming landscape.")

#-----what i do-----
with st.container():
    st.write("---")
    left_column, right_column =st.columns(2)
    with left_column:
        st.subheader("A Glimpse into my projects:")
        st.write("##")
        st.subheader("1.Personnel website in streamlit:")
        st.write("     Embarking on the creative endeavor of developing a personnel website"
                 "     using streamlit,i navigated the complexities without personal guidance."
                 "     this project highlighted my ability to tackle tasks autonomously and"
                 "     implement solutions effectively.")

        st.subheader("2.Website development using Anvil:")
        st.write("     Leveraging the power of Anvil, i contributed to the creation"
                 "     endeavor of developing a personal website, emphasizing "
                 "     user-friendly interfaces.")
        st.write("http://membership-form-project.anvil.app")

        st.subheader("3.Mablibs")
        st.write("engaging in the madlibs projects,"
                 "i created it for the entertainment purpose"
                 "i honed my problemsolving skills.")

        st.subheader("4.Basic Calculator:")
        st.write("in the realm ofpractical application,"
                 " i designed a fundamental calculator,"
                 "blending simplicity with utility.")



with st.container():
    st.write("---")
    st.write("##")
    text_column, image_column = st.columns((2, 1))
    with image_column:
       


     with text_column:
          st.subheader("Fun Fact: From Drama to Code ??")
          st.write("in a quiry turn of events,my interest in coding sparked"
             "while watching chinese,korean dramas.the cool portrayal of"
             "coders on-screen inspired me,even though i knew the reality"
             "was different today, i approach coding with a serious "
             "commitment to building a career in this dynamic field.")

          st.subheader("Connecting with me??:")
          st.write("to establish a connection or discuss potential collaborations,"
                   "feel free to reach out to me through email")
          st.write("nifracoder@gmail.com ")


          st.write("          THANK YOU FOR VISITING MY  PAGE           ")  

          with st.container():
              st.write("---")
              st.write("##")
              st.subheader(":mailbox: Get in touch with me!")

              contact_form = """<form action="https://formsubmit.co/nifracoder@gmail.com" method="POST">
                                    <input type="hidden" name="_captcha" value="false">
                                     <input type="text" name="name"  placeholder="Your Name" required>
                                     <input type="email" name="email" placeholder="Your Email" required>
                                     <textarea name="message" placeholder="Your message here!"></textarea>
                                     <button type="submit">Send</button>
                                </form>
                               """
st.markdown(contact_form, unsafe_allow_html=True)    

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

    