import streamlit as st 
import pandas as pd 
import numpy as np 
 
st.title("This is My Page",False,help = "not a link")
st.header(":gray[Cheruku rahul]:blush:",False, help= "user name",divider = 'orange')
st.subheader("content",False,help = "skills", divider = False)
st.caption("This all about learning")
code = '''
class Java{
    public static void main(String[] args){
    System.out.println("Today iam going to say about the java");
    }
}
'''
st.divider()
st.code(code,language = "java")
st.divider()
st.text("This is about today class let me tell you about greedy approach")
data  = pd.read_csv(r"c:\Users\C ARAVIND\Downloads\contacts_to_import.csv")
st.data_editor(data,hide_index = True, column_config={
        "widgets": st.column_config.Column(
            "Streamlit Widgets",
            help="Streamlit **widget** commands 🎈",
            width="medium",
            required=True,
        )
    })

