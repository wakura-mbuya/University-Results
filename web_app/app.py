# import the child scripts
import streamlit as st
import awesome_streamlit as ast
import home
import data 
import plots
import pred
import dashboard
from PIL import Image

ast.core.services.other.set_logging_format()

# create the pages
PAGES = {
    "Home": home,
    "Data":data,
    "Data visualisations": plots,
    "Predictions": pred,
    # "predictions": dashboard
}


# render the pages
def main():
   
    st.sidebar.title("University Students Performance Analysis and Prediction")
    selection = st.sidebar.selectbox("Select", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)
    if selection =="Home":
        st.sidebar.title("INFORMATION")
        st.sidebar.info(
        """
        Data is one of the most valuable currencies of our time. Data without organization, segmentation and analysis, it is essentially useless. Data aggregation is the process of compiling typically large amounts of information from a given database and organizing it into a more consumable and comprehensive medium. One application area of data aggregation is data mining applied to data available in an educational institution. Vast amounts of data generated in a setting like a university can give insights and predictions that would enhance management of such institutions.

Educational data mining applies data mining techniques to allow extraction of meanings and patterns from large amounts of data generated in educational institutions.Every academic year, universities generate large volumes of data from the students’ examination results information
The system allows the user to analyze and predict student's performance based on the dataset generated from the databases at the university
        """
    )
        image = Image.open('pic.png')
        st.image(image, caption='University Students Performance Analysis and Prediction using Machine Learning')
    elif selection=="Predictions":
        st.sidebar.title("")


if __name__ == "__main__":
    main()