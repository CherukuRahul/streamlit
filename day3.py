import streamlit as st
import pandas as pd
st.header("Day - 3 :sunglasses:")
st.text("Today we are goint to know about the metrics in the streamlit module")
st.metric(
    label = "Mood :orange[supper] :smile:",
    value = "Happy",
    delta = "30 ",
    delta_color = "normal",
    help = "This is my mood :innocent:"

)
st.metric(
    label = "Mood :red[bad] :angry:",
    value = "Upset",
    delta = "-30",
    delta_color = "normal",
    help = "This is the mood of my gf :cry:"
)

data = {
    "label" : ["This is the first thing in the metric syntax",
               "It support the emojis and styling to the text"],
    "value" : ["This is the data shown as the larger one in the page",
               "it doesn't support the emojis are stylin"],
    "delta" : ["This is the value that displays below the value",
               "It can be used like increase in the sales or decrease in the sales etc"],
    "delta_color": ["It is used to adjust the color red green for positive and negative values",
                    "It has three options  they are 1.normal 2.inverse 3.off"],
    "label_visibility" : ["You can check in the documentation",
                          "chusko pora puka"]
}
st.text("this are the attributes used in the creation of the above")
x = pd.DataFrame(data)
st.dataframe(x,hide_index = True)

