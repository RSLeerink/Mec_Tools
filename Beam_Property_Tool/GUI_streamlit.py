import streamlit as st
import numpy as np
import pandas as pd
from Profile_tool_rev00a import Profile_Select

#https://eurocodeapplied.com/design/en1993/ipe-hea-heb-hem-design-properties

st.title('My first app')

#ProfielSize = st.slider('Select profile size', 100, 400,100,20)
ProfielSize = st.text_input('Select profile size:', '100')
st.write("Selected profile size:", ProfielSize)

#Select profile
ProfileType = st.selectbox('Select profile type',('HEB', 'IPE'))
st.write('Profile type:', ProfileType)

#Profile size
ProfielSize = str(ProfielSize)
print(ProfielSize)

#FilePath = 'D:/Codeing/Python/TestingSpace/Mec_Tools/Mec_Tools/Beam_Property_Tool'
FilePath = 'D:/Codeing/Python/TestingSpace/Mec_Tools/Mec_Tools/Beam_Property_Tool/Profiles_S235_Eurocode_3.xlsx'
#ProfileType = 'HEB'
#ProfielSize = '200'

df = Profile_Select(FilePath,ProfileType,ProfielSize)


#title = st.text_input('Movie title', 'Life of Brian')
#st.write('The current movie title is', title)

Show1 = st.checkbox('Show Profile Dimensions')
if Show1:
    st.text('Profile Dimensions:')
    st.table(df[1])

Show2 = st.checkbox('Show Area Properties')
if Show2:
    st.text('Area Properties:')
    st.table(df[2])

Show3 = st.checkbox('Show Inertia properties about major axis y-y')
if Show3:
    st.text('Inertia properties about major axis y-y:')
    st.table(df[3])

Show4 = st.checkbox('Inertia properties about minor axis z-z:')
if Show4:
    st.text('Inertia properties about minor axis z-z:')
    st.table(df[4])

Show5 = st.checkbox('Torsional & warping properties ')
if Show5:
    st.text('Torsional & warping properties ')
    st.table(df[5])

Show6 = st.checkbox('Axial force & shear resistance')
if Show6:
    st.text('Axial force & shear resistance')
    st.table(df[6])

Show7 = st.checkbox('Bending major axis y-y')
if Show7:
    st.text('Bending major axis y-y')
    st.table(df[7])	

Show8 = st.checkbox('Bending minor axis z-z')
if Show8:
    st.text('Bending minor axis z-z')
    st.table(df[8])

Show9 = st.checkbox('Buckling curve')
if Show9:
    st.text('Buckling curve')
    st.table(df[9])

Show10 = st.checkbox('Section classification')
if Show10:
    st.text('Section classification')
    st.table(df[10])
