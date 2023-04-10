import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import random
from PIL import Image
logo = Image.open('logo.png')
#pip install pandas numpy matplotlib seaborn streamlit
#to run strealit :   streamlit run test2.py 
st.set_page_config(page_title="NetFlix  EDA", page_icon=":bar_chart:", layout="wide")
st.image(logo)
# Define the list of names
names = ["21A21A6116-G.HARSHINI", "21A21A6146-P.VINAY", "21A21A6101(l1)-B.SATISH KUMAR","21A21A6125-K.VENKATA LAKSHMI","22A21A6160-V.CHANDRIKA YESASWINI","21A21A6147-P.RAKESH","21A21A6115-G.VENKATA VINAY"]
st.title("Exploratory Data Analysis on Udemy Courses Dataset")
# Add the names to the sidebar
st.sidebar.title("Project Team Members:")

for name in names:
    st.sidebar.write(name)
st.sidebar.title("Under The Guidance of :")
st.sidebar.write("Dr.Bomma.Ramakrishna")
# File upload
uploaded_file = st.file_uploader("Choose a Udemy Courses Dataset csv")
if uploaded_file is not None:
    data=pd.read_csv(uploaded_file)
    st.dataframe(data)

    

st.title("Udemy Courses Dataset")

# Checkbox to select questions to display
show_q1 = st.checkbox("Show different subjects for which Udemy is offering courses?")
# Display selected questions
if show_q1:
    st.write("Different subjects for which Udemy is offering courses:")
    st.write(data.subject.unique())
show_q2 = st.checkbox("Show subject with the maximum number of courses?")
if show_q2:
    st.write("Subject with the maximum number of courses:")
    st.write(data.subject.value_counts().idxmax())
show_q3 = st.checkbox("Show all the courses which are Free of Cost?")
if show_q3:
    st.write("All the courses which are Free of Cost:")
    st.write(data[data.is_paid == False])
show_q4 = st.checkbox("Show all the courses which are Paid?")
if show_q4:
    st.write("All the courses which are Paid:")
    st.write(data[data.is_paid == True])
show_q5 = st.checkbox("Show Top Selling Courses?")
if show_q5:
    st.write("Top Selling Courses:")
    st.write(data.sort_values('num_subscribers', ascending=False).head())
show_q6 = st.checkbox("Show Least Selling Courses?")
if show_q6:
    st.write("Least Selling Courses:")
    st.write(data.sort_values('num_subscribers').head())
show_q7 = st.checkbox("Show all courses of Graphic Design where the price is below 100?")
if show_q7:
    st.write("All courses of Graphic Design where the price is below 100:")
    data1 = data[data.price != 'Free']
    data1.price = data1.price.astype(int)
    result = data1[(data1.subject == 'Graphic Design') & (data1.price < 100)]
    st.write(result)
    st.write(f"Total {len(result)} courses found.")
show_q8 = st.checkbox("List out all the courses that are related with 'Python'?")
if show_q8:
    st.write("All the courses that are related with 'Python':")
    result = data[data.course_title.str.contains('Python')]
    st.write(result)
    st.write(f"Total {len(result)} courses found.")

show_q9 = st.checkbox("What are courses that published in year 2015?")
if show_q9:
    st.write("Courses published in year 2015:")
    data['published_timestamp'] = pd.to_datetime(data.published_timestamp)
    result = data[data['published_timestamp'].dt.year == 2015]
    st.write(result)
    st.write(f"Total {len(result)} courses found.")
show_q10 = st.checkbox("What are the Max. Number of Subscribers for Each Level of courses ?")
if show_q10:
    st.write("Max. Number of Subscribers for Each Level of courses:")
    result = data.groupby('level')['num_subscribers'].max()
    st.write(result)
show_q11 = st.checkbox("Number of subscribers across different subjects")
if show_q11:
    fig, ax = plt.subplots()
    sns.boxplot(x='subject', y='num_subscribers', data=data, ax=ax)
    ax.set_xlabel("Subject")
    ax.set_ylabel("Number of subscribers")
    st.pyplot(fig)
show_q12 = st.checkbox("Distribution of number of subscribers")
if show_q12:
    fig, ax = plt.subplots()
    sns.histplot(x='num_subscribers', data=data, bins=20, ax=ax)
    ax.set_xlabel("Number of subscribers")
    ax.set_ylabel("Number of courses")
    st.pyplot(fig)
show_q13 = st.checkbox("Distribution of course prices")
if show_q13:
    fig, ax = plt.subplots()
    sns.histplot(x='price', data=data, bins=20, ax=ax)
    ax.set_xlabel("Price")
    ax.set_ylabel("Number of courses")
    st.pyplot(fig)
show_q14 = st.checkbox("Number of paid and free courses")
if show_q14:
    fig, ax = plt.subplots()
    sns.countplot(x='is_paid', data=data, ax=ax)
    ax.set_xlabel("Paid or free")
    ax.set_ylabel("Number of courses")
    st.pyplot(fig)
show_q15 = st.checkbox("Top 10 subjects with most number of courses")
if show_q15:
    top10_subjects = data['subject'].value_counts().head(10)
    fig, ax = plt.subplots()
    sns.barplot(x=top10_subjects, y=top10_subjects.index, ax=ax)
    ax.set_xlabel("Number of courses")
    ax.set_ylabel("Subject")
    st.pyplot(fig)
    














