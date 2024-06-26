import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# This is an example of a deployed Streamlit App.

This is a simple example of a Streamlit app that generates a spiral using the Altair library. And while this has nothing to do with a project, I'm just trying to show you how we can use Streamlit to create a simple app, and it was pretty easy to limit the access to the app to only certain users.

In the meantime, below is an example of what you can do with just a few lines of code:
"""

num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame(
    {
        "x": x,
        "y": y,
        "idx": indices,
        "rand": np.random.randn(num_points),
    }
)

st.altair_chart(
    alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    )
)
