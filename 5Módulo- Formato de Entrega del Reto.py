import streamlit as st
import pandas as pd 
import datetime
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import codecs

st.title('Reto 5 módulo - José Antonio Velasco Pérez')


employees_data = pd.read_csv('Employees.csv')

#("Eliminación de los registros que contengan NaN")
#employees_data.dropna(axis=0, subset=['Age'], inplace=True )
#employees_data.dropna(axis=0, subset=['Time_of_service'], inplace=True )
#employees_data.dropna(axis=0, subset=['Pay_Scale'], inplace=True )
#employees_data.dropna(axis=0, subset=['Work_Life_balance'], inplace=True )

@st.cache
def load_data(nrows):
    doc = codecs.open('Employees.csv','rU','latin1')
    data = pd.read_csv(doc, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data

def filter_data_by_EmployeeID(employeeID):
    filtered_data_employee = data[data['Employee_ID'].str.upper().str.contains(employeeID)]
    return filtered_data_employee

def filter_data_by_hometownInput(hometown):
    filtered_data_home = data[data['Hometown'].str.upper().str.contains(hometown)]
    return filtered_data_home

def filter_data_by_homeunitInput(unit):
    filtered_data_unit = data[data['Unit'].str.upper() == unit]
    return filtered_data_unit



def filter_data_by_hometown(hometown):
    filtered_data_hometown = data[data['Hometown'] == hometown]
    return filtered_data_hometown

def filter_data_by_unit(unit):
    filtered_data_unit = data[data['Unit'] == unit]
    return filtered_data_unit

def filter_data_by_education_level(level):
    filtered_data_education_level = data[data['Education_Level'] == level]
    return filtered_data_education_level


# Create the title for the web app
st.title("Employees App ")
st.markdown("Site that would help and make easier for us to analyze the performance of dataframe employees")


# Creamos sidebar
sidebar = st.sidebar
# Agregamos title y texto en sidebar
sidebar.title("Information filter")


data_load_state = st.text('Loading employees data...')
data = load_data(500)
data_load_state.text("Done! (using st.cache)")



#--- SIDEBAR FILTERS ---#

if st.sidebar.checkbox('Show dataframe structure and content'):
    st.subheader('Dataframe structure and content')
    st.write(f"Dataframe shape \n\n  {employees_data.shape}")
    st.write(f"Dataframe columns \n\n  ")
    st.write(data.columns)
    st.write(f"Dataframe dtypes \n\n ")
    st.write(data.dtypes)
    st.write(f"Dataframe head(3) \n\n  ")
    st.write(data.head(3))



if st.sidebar.checkbox('Show all employees'):
    st.subheader('All employees')
    st.dataframe(employees_data)

st.sidebar.markdown("##")

titleSearchID = st.sidebar.text_input('Find by Employee ID :')
btnSearchID = st.sidebar.button('Search by  Employee ID')

if (btnSearchID):
   data_filme = filter_data_by_EmployeeID(titleSearchID.upper())
   count_row = data_filme.shape[0]  # Gives number of rows
   st.write(f"Total Employee by ID : {count_row}")
   st.write(data_filme)

titleSearchHometown = st.sidebar.text_input('Find by Hometown :')
btnSearchHometown = st.sidebar.button('Search by Employee Hometown')

if (btnSearchHometown):
   data_filme = filter_data_by_hometownInput(titleSearchHometown.upper())
   count_row = data_filme.shape[0]  # Gives number of rows
   st.write(f"Total Employee by Hometown : {count_row}")
   st.write(data_filme)


titleSearchUnit = st.sidebar.text_input('Find by Unit :')
btnSearchUnit = st.sidebar.button('Search by Employee Unit')

if (btnSearchUnit):
   data_filme = filter_data_by_homeunitInput(titleSearchUnit.upper())
   count_row = data_filme.shape[0]  # Gives number of rows
   st.write(f"Total Employee by Unit : {count_row}")
   st.write(data_filme)


st.sidebar.markdown("##")
st.sidebar.markdown("##")
st.sidebar.markdown("##")
selected_hometown = st.sidebar.selectbox("Select Hometown", employees_data['Hometown'].unique())
btnFilterbyHometown = st.sidebar.button('Filter Hometown ')


if (btnFilterbyHometown):
   filterbyhometown = filter_data_by_hometown(selected_hometown)
   count_row = filterbyhometown.shape[0]  # Gives number of rows
   st.write(f"Total filter by Hometown : {count_row}")
   st.dataframe(filterbyhometown)


st.sidebar.markdown("##")
selected_unit = st.sidebar.selectbox("Select Unit", employees_data['Unit'].unique())
btnFilterbyUnit = st.sidebar.button('Filter Unit ')

if (btnFilterbyUnit):
   filterbyUnit = filter_data_by_unit(selected_unit)
   count_row = filterbyUnit.shape[0]  # Gives number of rows
   st.write(f"Total filter by Unit : {count_row}")
   st.dataframe(filterbyUnit)


st.sidebar.markdown("##")
selected_level = st.sidebar.selectbox("Select Education Level", employees_data['Education_Level'].unique())
btnFilterbyEducationLevel = st.sidebar.button('Filter Education Level ')

if (btnFilterbyEducationLevel):
   filterbyEducationLevel = filter_data_by_education_level(selected_level)
   count_row = filterbyEducationLevel.shape[0]  # Gives number of rows
   st.write(f"Total filter by Education Level : {count_row}")
   st.dataframe(filterbyEducationLevel)

# En caso de querer que las graficas se muevan con los filtros
#df_selection=employees_data.query("Hometown == @selected_hometown & Unit==@selected_unit & Education_Level==@selected_level")


st.markdown("___")
#Chart to visualize Number of Employees by Unit
df_grouped = employees_data.groupby(by=['Age']).count()[['Employee_ID']]
df_grouped = df_grouped.reset_index()

df_grouped.rename(columns = {'Employee_ID':'Count'}, inplace = True)
fig_distribution_perf=px.histogram(df_grouped,
                             x='Age',    
                             y='Count',       
                             title="Age distribution histogram",                         
                             color_discrete_sequence=["#7ECBB4"],
                             template="plotly_white")
fig_distribution_perf.update_layout(plot_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig_distribution_perf)


st.markdown("___")
#Chart to visualize Number of Employees by Unit
df_grouped = employees_data.groupby(by=['Unit']).count()[['Employee_ID']]
df_grouped.sort_values(by=['Employee_ID'], inplace=True)
df_grouped = df_grouped.reset_index()
df_grouped.rename(columns = {'Employee_ID':'Count'}, inplace = True)

fig_distribution_perf=px.bar(df_grouped,
                             x='Unit',    
                             y='Count',                    
                             title="Number of Employees by Unit",
                             color_discrete_sequence=["#7ECBB4"],
                             template="plotly_white")
fig_distribution_perf.update_layout(plot_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig_distribution_perf)

st.markdown("___")
#Chart to visualize Cities (hometowns) they have the highest attrition rate
df_grouped = employees_data.groupby(by=['Hometown']).count()[['Attrition_rate']]
df_grouped.sort_values(by=['Attrition_rate'],ascending=False, inplace=True)
df_grouped = df_grouped.reset_index()
df_grouped.rename(columns = {'Attrition_rate':'Attrition rate'}, inplace = True)

fig_distribution_perf=px.bar(df_grouped,
                             x='Hometown',    
                             y='Attrition rate',                    
                             title="Cities (hometowns) they have the highest attrition rate",
                             color_discrete_sequence=["#7ECBB4"],
                             template="plotly_white")
fig_distribution_perf.update_layout(plot_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig_distribution_perf)

#--- CONCLUSION ---#
st.markdown("**Analysis**")
st.markdown("""In general, we see that the city with the highest attrition rate is Lebanon followed by Springfield """)

 

st.markdown("___")
#Chart to visualize Age vs attrition rate.
df_grouped = employees_data.groupby(by=['Age']).count()[['Attrition_rate']]
df_grouped = df_grouped.reset_index()
df_grouped.rename(columns = {'Attrition_rate':'Attrition rate'}, inplace = True)

fig_distribution_perf=px.scatter(df_grouped,
                             x='Age',    
                             y='Attrition rate',                    
                             title="Age vs. attrition rate",                          
                             color_discrete_sequence=["#7ECBB4"],
                             template="plotly_white")
fig_distribution_perf.update_layout(plot_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig_distribution_perf)

#--- CONCLUSION ---#
st.markdown("**Analysis**")
st.markdown("""In general, we see that when the age of the employees is lower, the attrition rate is higher. """)



st.markdown("___")
#Chart to visualize Time of service vs attrition rate.
df_grouped = employees_data.groupby(by=['Time_of_service']).count()[['Attrition_rate']]
df_grouped = df_grouped.reset_index()

df_grouped.rename(columns = {'Attrition_rate':'Attrition rate'}, inplace = True)

fig_distribution_perf=px.scatter(df_grouped,
                             x='Time_of_service',    
                             y='Attrition rate',                    
                             title="Time of service vs. attrition rate",                          
                             color_discrete_sequence=["#7ECBB4"],
                             template="plotly_white")
fig_distribution_perf.update_layout(plot_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig_distribution_perf)


#--- CONCLUSION ---#
st.markdown("**Analysis**")
st.markdown("""In general, we see that when the service time is shorter, the attrition rate is higher. """)


