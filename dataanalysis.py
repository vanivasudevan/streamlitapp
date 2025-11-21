import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("Student Performance Analysis")
st.write("Upload a CSV file containing student performance data.")
# upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    st.subheader("Raw Data")
    st.dataframe(df)

    # line chart
    st.subheader("Line Chart of Marks")             
    st.line_chart(df.set_index('Month')[['Math', 'Science', 'English']])    
    # bar chart
    st.subheader("Bar Chart of Marks")
    st.bar_chart(df.set_index('Month')[['Math', 'Science', 'English']])    
    # pie chart
    st.subheader("Pie Chart of Total Marks Distribution")
    total_marks = df[['Math', 'Science', 'English']].sum()
    fig1, ax1 = plt.subplots()          
    ax1.pie(total_marks, labels=total_marks.index, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)    
    # histogram
    st.subheader("Histogram of Math Marks")
    fig2, ax2 = plt.subplots()
    ax2.hist(df['Math'], bins=10, color='blue', alpha=0.7)
    ax2.set_xlabel('Marks')
    ax2.set_ylabel('Number of Students')
    st.pyplot(fig2)     
    # box plot
    st.subheader("Box Plot of Science Marks")
    fig3, ax3 = plt.subplots()
    ax3.boxplot(df['Science'])
    ax3.set_ylabel('Marks')
    st.pyplot(fig3)
    # scatter plot
    st.subheader("Scatter Plot of English vs Math Marks")
    fig4, ax4 = plt.subplots()
    ax4.scatter(df['Math'], df['English'], color='green', alpha=0.7)
    ax4.set_xlabel('Math Marks')
    ax4.set_ylabel('English Marks')
    st.pyplot(fig4)    
    st.success("Data analysis complete!")
