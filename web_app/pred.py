# libraries
import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import os
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, RobustScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline, make_pipeline
from scipy import stats
from scipy.stats import skew, norm
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.base import BaseEstimator, TransformerMixin, RegressorMixin, clone
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
import datetime
import pickle
import gzip
import warnings
warnings.filterwarnings(action="ignore")

path = os.path.dirname(__file__)
my_model = path+'/model.pkl'      
        
        
# def write():
def write():
    with st.spinner("Loading Plots ..."):
         st.title('University Students Performance Prediction ')
    st.subheader("Random Forest Classifier")
    
    st.write("""
        The Random Forest Classifier Model used in the system has an accuracy of 73.33%. Upload a csv file with the features you would like to predict and the model will give you its predictions
        """)
    # the models + predictions
    st.sidebar.title("Predictions using Random Forest Classifier")
    
    # set up file upload
    uploaded_file = st.sidebar.file_uploader(label='Upload the csv or Excel File',
                                type=['csv', 'xlsx'])
    if uploaded_file is not None:
        try:
            results = pd.read_csv(uploaded_file)
        except Exception as e:
            results = pd.read_excel(uploaded_file)
            
        st.subheader('Features to be used for prediction')
        st.write(results)
        
        
        #load the model
        X_test = results.drop(['GRADE'], axis = 1)
        y=results['GRADE']
        Y_test = y.to_frame()
        pickled_model = pickle.load(open('model.pkl', 'rb'))
        predictions = pickled_model.predict(X_test)
        df = pd.DataFrame(predictions, columns=['PREDICTED GRADE'])
        # st.write(Y_test.columns)
        df['Actual Grade'] = Y_test['GRADE']
        # df.rename(columns = {'0':'PREDICTED GRADE'}, inplace = True)
        # st.subheader("Predicted Grade")
        # st.write(predictions)
        st.subheader('Predictions by the system')
        st.write(df)
        st.write('Accuracy:', pickled_model.score(X_test,y)*100, '%')
        
  