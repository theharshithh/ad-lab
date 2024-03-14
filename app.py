import streamlit as st
import os

from code_storage import jkff, jkff_tb, dff, dff_tb, encoder83, encoder83_tb, mux8x1, mux8x1_tb, decoder24, decoder24_tb
from code_storage import priority_enc, priority_enc_tb

# Define the options as a dictionary
options = {
    'jkff': jkff,
    'jkff_tb': jkff_tb,
    'dff': dff,
    'dff_tb': dff_tb,
    'encoder': encoder83,
    'encoder_tb': encoder83_tb,
    'mux': mux8x1,
    'mux_tb': mux8x1_tb,
    'decoder': decoder24,
    'decoder_tb': decoder24_tb,
    'priority_enc': priority_enc,
    'priority_enc_tb': priority_enc_tb
}

if (st.button('clear')):
    st.session_state.second = ''  

password = st.text_input('Enter the key (needed for py)', type='password', label_visibility="hidden", key='second')

if password == 'pypip':
    selected_option = st.selectbox('Select a component:', list(options.keys()))
    st.code(options[selected_option], language="python")
else:
    pass
    
