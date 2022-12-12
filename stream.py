import streamlit as st
import subprocess
from PIL import Image

st.header('🎈 R x Python Streamlit App')

st.sidebar.markdown('''
# About
This demo shows the use of R in a Streamlit App by showcasing 3 example use cases.
The R code for all 3 examples are rendered on-the-fly in this app.
R packages used:
- `ggplot2`
- `cowplot`
''')

st.subheader('1. Printing text in R')
with st.expander('See code'):
  code1 = '''print("Hello world ...")
  '''
  st.code(code1, language='R')
process1 = subprocess.Popen(["Rscript", "helloworld.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result1 = process1.communicate()
st.write(result1)


st.subheader('3. MLB `ggplot2`')
with st.expander('See code'):
  code3 = '''ggplot() + 
  geom_mlb_stadium(stadium_ids = "all_mlb", 
                   stadium_segments = "all") + 
  facet_wrap(~team) + 
  coord_fixed() + 
  theme_void()
  '''
  st.code(code3, language='R')
process3 = subprocess.Popen(["Rscript", "plot1.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result3 = process3.communicate()
image = Image.open('plot.png')
st.image(image)

