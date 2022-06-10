import streamlit as st
import pickle
import numpy as np
import pandas as pd
from PIL import Image
from pyexpat import model
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array, smart_resize

# st.cache()

st.markdown("<h1 style='text-align: center; color: light blue;'>NYC Budget- Friendly Weekend Guide</h1>", unsafe_allow_html=True)
# https://discuss.streamlit.io/t/how-do-i-align-st-title/1668/4
# st.markdown("<h2 style='text-align: center; color: white'>Learn About NYC's History</h2>", unsafe_allow_html=True)

landmarks = {'Name': ['Empire State', 'Met Museum', 'Statue of Liberty', 'Rockefeller Ctr', 'Grand Central', 
                      'Hudson Yards', 'BK Bridge', '911 Memorial', 'LIC', 'Roosevelt Island'], 
             'lat': [40.7484, 40.7794, 40.6892, 40.7587, 40.7527, 40.7538, 40.7061, 40.7114, 40.7425, 40.7605], 
             'lon': [-73.9857, -73.9632, -74.0445, -73.9787, -73.9772, -74.0022, -73.9969, -74.0125, -73.9601, -73.9510]}

df = pd.DataFrame(landmarks)
st.map(df)

if st.button(label="1. Roosevelt Island", help="Take the Roosevelt Island Tram for 2.75 and upload a picture of the 'RI' statue on the island to unlock the history"):
    st.write('2nd Avenue, between 59th Street and 60th Street')
if st.button(label="2. The Metropolitan Museum of Art", help='Upload a picture of the Met Museum entrance/ building to unlock the history'):
    st.write('1000 5th Ave, New York, NY 10028')
if st.button(label="3. Rockefeller Center", help='Upload a picture of the Golden Prometheus Statue to unlock the history'):
    st.write('45 Rockefeller Plaza, New York, NY 10111')
if st.button(label="4. Grand Central Terminal", help='Upload a picture of the Clock atop the Information Desk to unlock the history'):
    st.write('89 E 42nd St, New York, NY 10017')
if st.button(label="5. Empire State Building", help='Upload a picture of the building to unlock the history'):
    st.write('20 W 34th St, New York, NY 10001')
if st.button(label="6. Hudson Yards", help='Upload a picture of the Vessel to unlock the history'):
    st.write('20 Hudson Yards, New York, NY 100011')
if st.button(label="7. 9/11 Memorial", help='Upload a picture of one of the 9/11 Memorial Pools to unlock the history'):
    st.write('180 Greenwich St, New York, NY 10007')
if st.button(label="8. Statue of Liberty", help='Take a free ride on the Staten Island Ferry and upload a picture of the Statue of Liberty to unlock the history'):
    st.write('4 Whitehall St, New York, NY 10004')
if st.button(label="9. Brooklyn Bridge - DUMBO", help='Walk or bike across the Brooklyn Bridge and upload a picture of bridge to unlock the history'):
    st.write('Manhattan entrance: Brooklyn Bridge Promenade on Centre Street/Park Row')
    st.write('Brooklyn entrance: Brooklyn Bridge Underpass at Prospect Street & Cadman Plaza East')
if st.button(label="10. Gantry Plaza State Park - LIC", help='Upload a picture of PepsiCola sign to unlock the history'):
    st.write('4-09 47th Rd, Queens, NY 10007')


user_input = st.file_uploader(
    type = ['png', 'jpg', 'jpeg'],
    label='Upload a picture of a NYC Landmark',
    key='file_uploader'
)

model = tf.keras.models.load_model('model.h5')

def predictions(pred_model, user_input):

    user_input = Image.open(user_input)
    user_input = img_to_array(user_input)
    user_input = smart_resize(user_input, (256, 256))
    user_input = np.expand_dims(user_input, axis=0)
    pred = model.predict(user_input).round()
    pred = pred[0] 

    if pred[0] == 1.:
        link = "[History of 9/11 Memorial](https://www.911memorial.org/911-faqs)"
        return st.write(link, unsafe_allow_html=True)
    if pred[1] == 1.:
        link1 = "[History of Brooklyn Bridge](https://www1.nyc.gov/html/dot/html/infrastructure/brooklyn-bridge.shtml)"
        return st.write(link1, unsafe_allow_html=True)
    if pred[2] == 1.:
        link2 = "[History of Grand Central Terminal](https://www.grandcentralterminal.com/history/)"
        return st.write(link2, unsafe_allow_html=True)
    if pred[3] == 1.:
        link3 = "[History of Empire State Building](https://www.esbnyc.com/about/history)"
        return st.write(link3, unsafe_allow_html=True)
    if pred[4] == 1.:
        link4 = "[History of Rockefeller Center](https://www.rockefellercenter.com/history/)"
        return st.write(link4, unsafe_allow_html=True)
    if pred[5] == 1.:
        link5 = "[History of Metropolitan Museum of Art](https://www.metmuseum.org/about-the-met/history)"
        return st.write(link5, unsafe_allow_html=True)
    if pred[6] == 1.:
        link6 = "[History of Long Island City](https://www.lic.nyc/historyandcurrentcontext)"
        return st.write(link6, unsafe_allow_html=True)
    if pred[7] == 1.:
        link7 = "[History of Roosevelt Island](https://www.nps.gov/places/blackwell-s-island-new-york-city.htm)"
        return st.write(link7, unsafe_allow_html=True)
    if pred[8] == 1.:
        link8 = "[History of Statue of Liberty](https://www.statueofliberty.org/statue-of-liberty/overview-history/)"
        return st.write(link8, unsafe_allow_html=True)
    if pred[9] == 1.:
        link9 = "[History of Hudson Yards](https://ny.curbed.com/2016/12/13/13933084/hudson-yards-new-york-history-manhattan)"
        link10 = "[here](https://www.hudsonyardsnewyork.com/food-drink)"
        st.write(link9, unsafe_allow_html=True)
        st.write("Next stop, The High Line!")
        st.write("If you are hungry, I recommend looking ", link10, "for food options.", unsafe_allow_html=True)
    return ""

if user_input:
    st.text(predictions(model, user_input))
