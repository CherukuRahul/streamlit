import pandas as pd
import numpy as np
import streamlit as st 
from datetime import datetime

dict = {
    "Name" : ["Rahul"],
    "Age" :  [21],
    "Gender" : [1],
    "Female" : [0],
    "Qualification" : ["none"],
    "Branch" : ["csm"],
    "date of Joinig" : [  datetime(2024, 2, 5)],
    "rating" : [1],
    "linkedin" : ["https://www.w3schools.com/python/python_regex.asp"],
    "marks" : [90]
    }
Data = pd.DataFrame(dict)
x = st.data_editor(Data,hide_index = True,
                num_rows = "dynamic",
                column_config = {
                    "Qualification" : st.column_config.Column(
                        label = "Educational Qualification",
                        help = "It is for B_tech students only",
                        required = True,
                        width = "medium",
                        disabled = False
                    ),
                    "Name" : st.column_config.TextColumn(
                        label = "Student Name",
                       required = True,
                        help = "Enter your name",
                        disabled = False,
                        max_chars = 20,
                        validate = "^[a-z]+[^0-9]+$"
                        
                    ),
                    "Age"  : st.column_config.NumberColumn(
                        help = "Your Age",
                        required = True,
                        default = 20,
                        min_value = 19,
                        max_value = 21,
                        format = "%d",
                        step = 1
                    ),
                    "Gender" : st.column_config.CheckboxColumn(
                        label = "Male",
                        help = "If your male tick the box",
                        default = False
                    ),
                    "Female" : st.column_config.CheckboxColumn(
                        label = "Female",
                        help = "if your female tick the box",
                        default  = False
                    ),
                    "Branch" : st.column_config.SelectboxColumn(
                        label = "branch",
                        help = "Specify your branch",
                        options = [
                            "csm",
                            "cse",
                            "ece",
                            "eee",
                            "it",
                            "csd",
                            "others"
                        ],
                        default = None,
                        required = True
                    ),
                    "date of Joining" : st.column_config.DatetimeColumn(
                        label = "When we know",
                        help = "casual date when you seen me",
                        format = "DD Mo YYYY",
                        step = 60,
                    ),
                    "rating" : st.column_config.ListColumn(
                        label = "Friendship Rating",
                        help = "Adhoo urike mowa"
                    ),
                    "linkedin" : st.column_config.LinkColumn(
                        help = "Enter your Linked In account Link",
                        required = True,
                        display_text = "Linked In Profile"
                    ),
                    "marks" : st.column_config.ProgressColumn(
                        min_value = 0,
                        max_value = 100,
                        format="$%f",
                        help = "It is statics",
                        
                    )

                }
                )
