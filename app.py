import streamlit as st

st.title('Test: Why Am I Being Tested?')

st.write('Assalamu alaykum! Ahlan bik! Please check all boxes that apply:')
st.write('NOTE: The descrption of "consistent" varies person to person so please judge accordingly)')
salah = st.checkbox('My salah has been consistent')
quran = st.checkbox('My quran has been consistent')
adhkar = st.checkbox('My adhkar has been consistent')
no_tawbah = st.checkbox('There is no sin I have committed for which I have yet to make specific tawbah')
heart = st.checkbox('I feel spiritually well/ clean/ connected')

all_true = all([salah, quran, adhkar, no_tawbah, heart])
any_true = any([salah, quran, adhkar, no_tawbah, heart])

if all_true:
     st.success('Alhamdulillah! THis a test that will elevate your ranks; have sabr for it will be over soon')
elif any_true:
     st.info('Pattern, g and may Allah guide you')
else:
     st.warning('Pattern, g fr and may Allah guide you')
