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

st.subheader('2. Creating a plot using `ggplot2`')
process2 = subprocess.Popen(["Rscript", "plot.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result2 = process2.communicate()
image = Image.open('plot.png')
st.image(image)
st.caption('**Figure 1.** A simple scatter plot of *wt* as a function of *mpg* from the mtcars dataset.')
