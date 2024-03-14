import streamlit as st
import os

from code_storage import jkff, jkff_tb, dff, dff_tb, encoder83, encoder83_tb, mux8x1, mux8x1_tb, decoder24, decoder24_tb
from code_storage import priority_enc, priority_enc_tb

def find_program(ques):
    directory = 'dataset-ques'
    file_names = os.listdir(directory)
    for file_name in file_names:
        if ques in file_name:
            st.image(os.path.join(directory, file_name))

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

if password == 'hkm':
    
    exp_type = st.radio("Select experiment type:", options=['Software', 'Hardware'])
    if exp_type == 'Software':
        selected_option = st.selectbox('Select a component:', list(options.keys()))
        st.code(options[selected_option], language="python")
    else:
        
        ques = st.text_input('Enter the problem', type='password', key='ques', label_visibility="hidden")
        if ques != '':
            find_program(ques)
