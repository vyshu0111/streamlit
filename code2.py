import streamlit as st
st.title("prime num")
a = st.text_input(label="Enter the number ")
if st.button("Submit"):
    num=int(a)
    count=0
    for i in range(1,num+1):
        if(num%i==0):
            count+=1
    if(count==2):
        st.write("prime number")
    else:
        st.write("not a prime number")
    