from ast import In
from re import I
import streamlit as st
import pandas as pd
import altair as alt 
from PIL import Image

#image = Image.open('name of logo')
st.write("We will be coding a vowel counter")
# st.write(image, use_column_width =True)
Input_variable = 'AEIOU'

input1 = st.text_area('Write input', Input_variable, height = 150)
#st.textarea whats in the '' will be the title of the box
# whats in the input varibale will be side the box 
# height is for max height of the box ie size of box

st.subheader('How to write outputs'
             'This is method one')

def vowelCoun(sentence):
    d = dict([
        ('A',sentence.count('A')),
        ('E',sentence.count('E')),
        ('I',sentence.count('I')),
        ('O',sentence.count('O')),
        ('U',sentence.count('U'))

    ])
    return d 


X = vowelCoun(input1.upper())

#X_label = list(X)
#X_values = list(X.values())

X

st.subheader('second print option ')
st.write('There are ' + str(X['A']) + ' Letter A')
st.write('There are ' + str(X['E']) + ' Letter E')
st.write('There are ' + str(X['I']) + ' Letter I')
st.write('There are ' + str(X['O']) + ' Letter O')
st.write('There are ' + str(X['U']) + ' Letter U')

st.subheader('second print option ')
st.subheader('Here will be method 3 where we use inputs to create data frames')

df = pd.DataFrame.from_dict(X, orient = 'index')
df = df.rename({0:'count'}, axis ='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'letter'})

st.write(df)

st.subheader('fourth print option')
p = alt.Chart(df).mark_bar().encode(
    x = 'letter' , 
    y = 'count'
)
p = p.properties(
    width=alt.Step(80)
)
#This changes the properties and this will change the width of the bar
st.write(p)