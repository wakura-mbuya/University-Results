from turtle import title
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

path = os.path.dirname(__file__)
my_file = path+'/train.csv'
my_file2 = path+'/student_prediction.csv'
#st.set_option('deprecation.showfileUploaderEncoding', False)
def write():
    with st.spinner("Loading Plots ..."):
        st.title('Data Visualizations')


        # read the datasets
        
        # set up file upload
        uploaded_file = st.sidebar.file_uploader(label='Upload the csv or Excel File',
                                 type=['csv', 'xlsx'])
        if uploaded_file is not None:
            try:
                results = pd.read_csv(uploaded_file)
            except Exception as e:
                results = pd.read_excel(uploaded_file)
        else:           
            # na_value=['',' ','nan','Nan','NaN','na', '<Na>']
            train = pd.read_csv(my_file, engine = 'python') #na_values=na_value)
            results = pd.read_csv(my_file2, engine='python')
            #st.sidebar.title("Gallery")
        st.sidebar.subheader("Choose Feature to plot")
        plot = st.sidebar.selectbox("feature", ( "Students Demographic Information",'Students Education Background', 'Students Occupation', 'Students Transport and Accomodation',"Students Family Background", "Students Participation in In-Class and Extra-Curricular Activities",))

        if plot == 'Students Demographic Information':
           
            st.subheader("Students Demographic Information Plots")
            st.set_option('deprecation.showPyplotGlobalUse', False)
            # time_data = full_train[['Date', 'Sales']]
            # time_data['datetime'] = pd.to_datetime(time_data['Date'])
            # time_data = time_data.set_index('datetime')
            # time_data = time_data.drop(['Date'], axis = 1)
            
            fig, axes = plt.subplots(1, 2, squeeze=False, figsize=(14,5))
            ax1 = axes[0][0]
            labels = ['18-21 years', '22-25 years', 'above 26 years']
            sizes = results['AGE'].value_counts().values
            ax1.pie(sizes, labels=labels, startangle=90, counterclock=False, autopct='%1.1f%%')
            ax1.set_title("Students' Age distribution")
            ax1.set_frame_on(True)

            #plot gender ditribution on axis2
            ax2 = axes[0][1]
            labels = ['Male', 'Female']
            sizes = results['GENDER'].value_counts().values
            ax2.pie(sizes, labels=labels, startangle=90, counterclock=False, autopct='%1.1f%%')
            ax2.set_title('Gender Distrubution')
            ax2.set_frame_on(True)
            fig.suptitle('Age and Gender Distribution')
            plt.grid() 
            st.pyplot() 
            
            #plot correlation btn age and performance
            age_df = results.groupby(['AGE'])['GRADE'].mean().reset_index()
            # for readability, change age values from the coded value to some meaningful string
            age_df.at[0, 'AGE'] = '18 -21 Years'
            age_df.at[1, 'AGE'] = '22 -25 Years'
            age_df.at[2, 'AGE'] = '26 Years and Above'
            age_df[['AGE','GRADE']].plot(kind='bar', x='AGE', y='GRADE', ylabel='Average Grade', title='Comparison of performance of students in different age groups', color=['brown', 'blue', 'green'])
            st.pyplot()

            
        if plot == 'Students Education Background':            
            st.subheader("Students Education Background Plots")
            st.set_option('deprecation.showPyplotGlobalUse', False)
            fig, axes = plt.subplots(1, 2, squeeze=False, figsize=(14,5))
            fig.suptitle('Former High School and Scholarships distribution')

            #plot graduated high school distribution on axis1
            ax1 = axes[0][0]
            labels = ['Public', 'Private', 'Other']
            sizes = results['HS_TYPE'].value_counts().values
            ax1.pie(sizes, labels=labels, startangle=90, counterclock=False, autopct='%1.1f%%')
            ax1.set_title("Former High school type")
            ax1.set_frame_on(True)
            # plt.grid() 
            # st.pyplot() 

            #plot Scholarships ditribution on axis2
            ax2 = axes[0][1]
            labels = ['50%', '75%', 'Full', '25%', 'None']
            sizes = results['SCHOLARSHIP'].value_counts().values
            ax2.pie(sizes, labels=labels, startangle=90, counterclock=False, autopct='%1.1f%%', explode=[0,0,0,0,0.1])
            ax2.set_title('Scholarships Distribution')
            ax2.set_frame_on(True)
           # plt.grid() 
            st.pyplot() 
            
            
            # comparing the performance of students from various high schools
            highSkul_df = results.groupby(['HS_TYPE'])['GRADE'].mean().reset_index() # group students based on their high school and get mean of the grade for each group

            # for readability, change High school type values from the coded value to some meaningful string
            highSkul_df.at[0, 'HS_TYPE'] = 'Private'
            highSkul_df.at[1, 'HS_TYPE'] = 'Public'
            highSkul_df.at[2, 'HS_TYPE'] = 'Other'
            # Visualize the performance based on former high school
            highSkul_df[['HS_TYPE','GRADE']].plot(kind='bar', x='HS_TYPE', y='GRADE', xlabel='Former high school type', ylabel='Average Grade', title="Comparison of performance of students based on former high school", color=['brown', 'blue', 'green'])
            # plt.grid() 
            st.pyplot() 
            
            
        if plot == 'Students Occupation':
            flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
            st.subheader("Students Occupation Plots")
            # visualize students employment status
            results['WORK'].value_counts().plot(kind='pie', title='Students Empoyment status', labels=['No', 'Yes'], startangle=90, counterclock=False, autopct='%1.1f%%') 
            st.pyplot()
            
            # compare the performance of students who are employed and those who are no
            emp_df = results.groupby(['WORK'])['GRADE'].mean().reset_index() # group students based on their age and get mean of the grade for each group 
            # for readability, change WORK values from the coded value to some meaningful string
            emp_df.at[0, 'WORK'] = 'Employed'
            emp_df.at[1, 'WORK'] = 'Not Employed'
            

            #Visualize
            emp_df[['WORK','GRADE']].plot(kind='bar', x='WORK', y='GRADE', xlabel='Employment status', ylabel='Average Grade', title="Comparison of performance of students based on employment status", color=['brown', 'blue', 'green'])
            st.pyplot()
            
            def employment_label(row):
                '''Decode the work column'''
                if row['WORK'] == 1:
                    return 'Employed'
                else:
                    return 'Unemployed'
    
            def study_hrs_label(row):
                '''Decode study hours column'''
                if row['STUDY_HRS'] == 1:
                    return 'None'
                elif row['STUDY_HRS'] == 2:
                    return 'Less than 5 hours'
                elif row['STUDY_HRS'] == 3:
                    return '6-10 Hours'
                elif row['STUDY_HRS'] == 4:
                    return '11 - 20 Hours'
                else:
                    return 'More than 20 Hours'
                
            work_df=results[['WORK', 'STUDY_HRS']].copy()
            work_df =work_df.groupby(['WORK', 'STUDY_HRS'])['STUDY_HRS'].sum().to_frame(name='count').reset_index()
            work_df['emp_status'] = work_df.apply (lambda row: employment_label(row), axis=1)
            work_df['study_hrs'] = work_df.apply (lambda row: study_hrs_label(row), axis=1)
            work_df.drop(['WORK', 'STUDY_HRS'], inplace=True, axis=1)
            sns.catplot(data=work_df, x="study_hrs", y="count", hue="emp_status", kind="bar")
            plt.xticks(rotation=45)
            plt.ylabel('Number of students')
            plt.xlabel('Weekly study hours')
            plt.title('Hours Spent for studying by Employed and Unemployed students')
            st.pyplot()


        if plot == 'Students Transport and Accomodation':
            st.subheader("Students Transport and Accomodation Plots")
            fig, axes = plt.subplots(1, 2, squeeze=False, figsize=(14,5))
            fig.suptitle('Student Transport and Accomodation Types')
            #plot mode of transport
            ax1 = axes[0][0]
            labels = ['Bus', 'Private car/taxi', 'Other', 'Bicycle']
            sizes = results['TRANSPORT'].value_counts().values
            ax1.pie(sizes, labels=labels, startangle=90, counterclock=False, autopct='%1.1f%%', explode=[0,0,0,.1])
            ax1.set_title("Students' Mode of Transport to School")
            ax1.set_frame_on(True)

            #plot Accomodation type
            ax2 = axes[0][1]
            labels = ['Rental', 'Dormitory/Hostel', 'With Family', 'Other']
            sizes = results['LIVING'].value_counts().values
            ax2.pie(sizes, labels=labels, startangle=90, counterclock=False, autopct='%1.1f%%',explode=[0,0,0,.1] )
            ax2.set_title("Students' Accomodation Type")
            ax2.set_frame_on(True)
            st.pyplot()
            
            # compare the performance of students based on their place of stay
            accom_df = results.groupby(['LIVING'])['GRADE'].mean().reset_index() # group students based on their accomodation type
            accom_df.at[0, 'LIVING'] = 'Rental'
            accom_df.at[1, 'LIVING'] = 'Dormitory/Hostel'
            accom_df.at[2, 'LIVING'] = 'With Family'
            accom_df.at[3, 'LIVING'] = 'Other'
            #visualize the accomodation vs performance
            sns.catplot(data=accom_df, x="LIVING", y="GRADE",width=.8, kind="bar")
            plt.xticks(rotation=45)
            plt.ylabel('Average Grade')
            plt.xlabel('Accomodation Type')
            plt.title("Relationship between student's accomodation type and the performance")
            st.pyplot()

            
        if plot == 'Students Family Background':
            st.subheader("Students Family Background Plots")
            st.set_option('deprecation.showPyplotGlobalUse', False)
            # compare performance of students based on number of siblings they have
            siblings_df = results.groupby(['#_SIBLINGS'])['GRADE'].mean().reset_index() # group students based on their accomodation type
            sns.catplot(data=siblings_df, x="#_SIBLINGS", y="GRADE",width=.8, kind="bar")
            plt.xticks(rotation=45)
            plt.ylabel('Average Grade')
            plt.xlabel('Number of siblings')
            plt.title("Relationship between Number of siblings and the students' performance")
            st.pyplot()
            
            # Marital status
            results['PARTNER'].value_counts().plot(kind='pie', title="Students' marital status", labels=['No', 'Yes'], startangle=90, counterclock=False, autopct='%1.1f%%')
            st.pyplot()
            
            marital_df = results.groupby(['PARTNER'])['GRADE'].mean().reset_index() # group students based on their accomodation type
            sns.catplot(data=marital_df, x="PARTNER", y="GRADE",width=.8, kind="bar")
            plt.xticks(rotation=45)
            plt.ylabel('Average Grade')
            plt.xlabel('Marital status')
            plt.title("Relationship between Marital status and the students' performance")
            st.pyplot()
            
            # parents' level of education
            fig, axes = plt.subplots(1, 2, squeeze=False, figsize=(14,5))
            fig.suptitle("Parents' Highest Level of Education")
            #plot mother's edudation level
            ax1 = axes[0][0]
            labels = ['Primary school', 'High school', 'Secondary school', 'University', 'MSc', 'Ph.D']
            sizes = results['MOTHER_EDU'].value_counts().values
            ax1.pie(sizes, labels=labels, startangle=90, counterclock=False, autopct='%1.1f%%', explode=[0,0,0,0,0,.1])
            ax1.set_title("Mother's Highest Education Level")
            ax1.set_frame_on(True)

            #plot Accomodation type
            ax2 = axes[0][1]
            labels = ['High school', 'Secondary school', 'Primary school', 'University', 'MSc', 'Ph.D']
            sizes = results['FATHER_EDU'].value_counts().values
            ax2.pie(sizes, labels=labels, startangle=90, counterclock=False, autopct='%1.1f%%', explode=[0,0,0,0,0,.1])
            ax2.set_title("Father's Highest Education Level")
            ax2.set_frame_on(True)

            
            st.pyplot()
            
            #MOTHER_EDUC vs the student's performance
            sns.catplot(data=results.groupby(['MOTHER_EDU'])['GRADE'].mean().reset_index() , x="MOTHER_EDU", y="GRADE",width=.8, kind="bar")
            plt.title('Mothers Education versus Student Grade')
            st.pyplot()
            
            #FATHER_EDUC vs the student's performance
            sns.catplot(data=results.groupby(['FATHER_EDU'])['GRADE'].mean().reset_index() , x="FATHER_EDU", y="GRADE",width=.8, kind="bar")
            plt.title('Father Education versus Student Grade')
            st.pyplot()
            
        if plot == 'Students Participation in In-Class and Extra-Curricular Activities':
            st.subheader('Students Participation in In-Class and Extra-Curricular Activities Plots')
            #participation in co-curricular activities
            sns.catplot(data=results.groupby(['ACTIVITY'])['GRADE'].mean().reset_index() , x="ACTIVITY", y="GRADE",width=.8, kind="bar")
            plt.title('Student participation in co-curricular activities')
            st.pyplot()
            
            # study hours and class ATTENDance
            fig, axes = plt.subplots(1, 2, squeeze=False, figsize=(14,5))

            #plot weekly study hours
            ax1 = axes[0][0]
            labels = ['Less than 5 hours', '6-10 Hours', 'None', '11-20 Hours', 'More than 20 Hours']
            sizes = results['STUDY_HRS'].value_counts().values
            ax1.pie(sizes, labels=labels, startangle=90, counterclock=False, autopct='%1.1f%%', explode=[0,0,0,0,.1])
            ax1.set_title("Weekly Study Hours")
            ax1.set_frame_on(True)

            #Class ATTENDance
            ax2 = axes[0][1]
            labels = ['Always', 'Sometimes']
            sizes = results['ATTEND'].value_counts().values
            ax2.pie(sizes, labels=labels, startangle=90, counterclock=False, autopct='%1.1f%%' )
            ax2.set_title("Class Attendance")
            ax2.set_frame_on(True)

            fig.suptitle('Weekly Study Hours and Class Attendance')
            st.pyplot()
            
            
            #self study
            sns.catplot(data=results.groupby(['STUDY_HRS'])['GRADE'].mean().reset_index() , x="STUDY_HRS", y="GRADE",width=.8, kind="bar")
            plt.title('Effect of Personal study hours')
            st.pyplot()
            
            
            #Impact of reading books and journals (both scientific and non-scientific)
            fig, axes = plt.subplots(1, 2, squeeze=False, figsize=(14,5))
            fig.suptitle('Reading Frequency Effect to Performance')
            #Reading scientific books and journals
            ax1 = axes[0][0]
            sns.barplot(data=read_sci , x="READ_FREQ_SCI",ax=ax1, y="GRADE",width=.8)
            ax1.set_title("Scientific books and journals")
            ax1.set_ylabel('Average Grade')
            ax1.set_xlabel("Reading Frequency")
            ax1.set_frame_on(True)

            #Reading non-scientific books and journals
            ax2 = axes[0][1]
            sns.barplot(data=read_fic, x="READ_FREQ",ax=ax2, y="GRADE",width=.8)
            ax2.set_title("Non-scientific books and journal")
            ax2.set_ylabel('Average Grade')
            ax2.set_xlabel("Reading Frequency")
            ax2.set_frame_on(True)
            st.pyplot()