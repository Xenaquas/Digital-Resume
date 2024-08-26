from pathlib import Path
import streamlit as st
from PIL import Image

# --------- Path Settings --------
current_dir = Path(__file__).parent if "_file_" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "hamza.png"

# Hide Streamlit Style
hide_st_style = """
        <style>
        #MainMenu {visibility: hidden;}
        .stActionButton div{visibility: hidden;}
        #header {visibility: hidden;}
        #footer {visibility: hidden;}
        </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# ---- General Settings ----
PAGE_TITLE = "Digital CV | Hamza Shaikh"
PAGE_ICON = ":wave:"
NAME = "Hamza Shaikh"
DESCRIPTION = "Data Analyst, assisting by supporting data-driven decision-making."
EMAIL = "hmsk.tech@gmail.com"

SOCIAL_MEDIA = {
    "GitHub": "https://github.com/Xenaquas",
    "LinkedIn": "https://www.linkedin.com/in/hamza-shaikh-ds/",
    "Gmail": "https://mail.google.com/mail/?view=cm&fs=1&to=hmsk.tech@gmail.com"
}

PROJECTS = {
    ":penguin: Predicting Penguin Species using Machine Learning": "https://ds-machinelearning.streamlit.app/",
    ":house: House Price Analysis Dashboard": "https://programmingprojectdevelopement.blogspot.com/2024/05/house-prices-in-mumbai-in-depth-analysis.html",
    ":frame_with_picture: Image Background Remover": "https://img-bg-remover.streamlit.app/"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# ------ Load CSS, PDF & PROFILE PIC ------
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

# ----- HERO SECTION -----
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=190)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write(":e-mail: [Gmail](https://mail.google.com/mail/?view=cm&fs=1&to={})".format(EMAIL))

# ----- SOCIAL LINKS ------
st.write("#")
st.subheader('Social Link & Repository')
st.write('---')
with st.expander('Social Links'):
    st.info('Click on the below link to check GitHub, LinkedIn Profile, or Email.')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")

# ----- QUALIFICATION & SKILLS ------
st.write("#")
st.subheader("Qualification & Skills")
st.write("---")
with st.expander('Experience & Qualifications'):
    st.subheader("Experience & Qualifications")
    st.success("""
    - 	:white_check_mark: 2 Years experience extracting actionable insights from data.
    - 	:white_check_mark: Strong hands-on experience & knowledge in Python & MySQL.  
    - 	:white_check_mark: Good understanding of statistical principles and their respective applications.
    - 	:white_check_mark: Excellent team-player and displaying a strong sense of initiative on tasks.  
    """)

# ------ SKILLS ------
with st.expander('Hard Skills'):
    st.subheader("Hard Skills")
    st.success("""
    - :male-technologist: Programming: Python, R Programming, SQL
    - :bar_chart: Data Visualization: Power BI, Ggplot2, Plotly, MS Excel
    - :books: Modeling: Linear Regression, Logistic Regression, Decision Trees
    - :memo: Databases: MySQL, Sqlite
    """)

# ------- WORK HISTORY ------
st.write("#")
st.subheader("Work History")
st.write("---")
with st.expander('**UNOSYS Solution**'):
    st.success("**Unosys Solution | DATA SCIENCE RESEARCH INTERN**")
    st.warning("*April 2024 - July 2024*")
    st.write("Internship focusing on data analysis, data visualization and machine learning")
    st.info("""
    - :small_blue_diamond:  Collected and analyzed data on over 50,000 house prices from sources including Data.gov, Zillow, and Kaggle, refining datasets to ensure
    accuracy and increasing reliability for predictive modeling efforts by 25%.
    - :small_blue_diamond:  Utilized SQL and Python to analyze large datasets, identifying key trends and patterns, improving data-driven decision-making by 45%.
    - :small_blue_diamond:  Designed and implemented interactive data visualization dashboards using Python and Power BI, improving report generation speed by 40%
    and enabling real-time analytics for over 25 users across departments.
    - :small_blue_diamond:  Developed and deployed machine learning models for house price prediction using Streamlit, enhancing the model evaluation process and
    providing accessible web-based predictions.
    """)

with st.expander('**MAK Tutorials**'):
    st.success("**MAK Tutorials | Teaching Assistant**")
    st.warning("*April 2022 - August 2024*")
    st.write("Internship focusing on teaching, learning, development & collaboration.")
    st.info("""
    - :small_blue_diamond:  Conducted interactive and engaging classes for students from grade 6 to 10, covering a range of subjects to enhance their understanding and
    academic performance.
    - :small_blue_diamond:  Collaborated closely with a Senior Full Stack Developer on diverse
    projects, engaging in tasks such as data collection, mining, analysis, and interpretation under expert mentorship.
    - :small_blue_diamond:  Acquired hands-on experience in integrating new technologies and solutions, effectively translating theoretical concepts into real-world
    applications through hands-on work with a senior developer.
    """)

# ---- PROJECTS & ACHIEVEMENTS ----
st.write("#")
st.subheader("Projects & Accomplishment")
st.write("---")
for project, link in PROJECTS.items():
    with st.expander(f'**Project** - {project}'):
        st.subheader("Link")
        st.info(f"[{project}]({link})")
