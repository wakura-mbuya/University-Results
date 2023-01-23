import streamlit as st
import pandas as pd 
import os

path = os.path.dirname(__file__)
my_file = path+'/train.csv'
my_file2 = path+'/store.csv'
def write():
    
    with st.spinner("Loading Data ..."):
        st.title('Data description  ')
        # na_value=['',' ','nan','Nan','NaN','na', '<Na>']
        train = pd.read_csv(my_file, engine='python') #na_values=na_value)
        st.write(train.sample(20))