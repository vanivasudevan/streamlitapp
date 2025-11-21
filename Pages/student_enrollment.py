mport streamlit as st
st.title('Student Enrollment Page')
subjects=st.multiselect('Select Subjects',['Maths','Science','Physics','Chemistry',
'English'])
st.write('Selected Subjects : ',subjects)
 
