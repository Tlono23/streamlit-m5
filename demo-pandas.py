import streamlit as st 
import pandas as pd 
 

#names_link = 'dataset.csv'
#names_data = pd.read_csv(names_link)

st.title('Streamlit and pandas')

#st.dataframe(names_data)


st.title('Streamlit con cache')

DATA_URL = 'dataset.csv'

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

data_load_state = st.text('Loading data...')
data = load_data(1000)
data_load_state.text("Done !")

st.dataframe(data)


#myname = st.text_input('nombre :')

#if (myname):
#    st.write(f"tu nombre es : {myname}")

#mensaje=""

#def bienvenida(nombre):
#    mymensaje = 'bienvenido/a :' + nombre
#    return mymensaje

#myname = st.text_input('nombre :')

#if (myname):
#    mensaje = bienvenida(myname)


#st.write(f" : {mensaje}")




#st.title('Streamlit - Search names') 

#@st.cache
#def load_data_byname(name):
#    data = pd.read_csv(DATA_URL)
#    filtered_data_byname = data[data['name'].str.contains(name)]
#    return filtered_data_byname

#myname = st.text_input('Name :')
#if (myname):
#    filterbyname = load_data_byname(myname)
#    count_row = filterbyname.shape[0]
#    st.write(f"Total names : {count_row}")

#    st.dataframe(filterbyname)

st.title('Streamlit - Search ranges') 


@st.cache
def load_data_byrange(startid, endid):
    data = pd.read_csv(DATA_URL)
    filtered_data_byrange = data[ (data['index']>=startid) & (data['index']<=endid) ]
    return filtered_data_byrange

startid = st.text_input('Start index :')
endid   = st.text_input('End index :')
btnRange = st.button('Search by range')

if (btnRange):
    filterbyrange = load_data_byrange( int(startid), int(endid) )
    count_row = filterbyrange.shape[0]
    st.write(f"Total items : {count_row}")

    st.dataframe(filterbyrange)