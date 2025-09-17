import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Chart")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.subheader("Area chart")
st.area_chart(chart_data)

st.subheader("Pyplot chart")
fig, ax = plt.subplots()
ax.plot(chart_data['A'], label='A')
ax.plot(chart_data['B'], label='B')
ax.plot(chart_data['C'], label='C')
ax.set_title("Pyplot Line Chart")
ax.legend()
st.pyplot(fig)