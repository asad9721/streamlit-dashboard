import pandas as pd
import plotly.express as px
import streamlit as st
import scipy.stats
import time

df = pd.read_csv('vehicles_us.csv')
model_year_medians = df.groupby('model')['model_year'].median()
df['model_year'] = df['model_year'].fillna(df['model'].map(model_year_medians))

cylinders_medians = df.groupby('model_year')['cylinders'].median()
df['cylinders'] = df['cylinders'].fillna(df['model_year'].map(cylinders_medians))

df['odometer'] = df['odometer'].fillna(df['odometer'].median())

df['paint_color'] = df['paint_color'].fillna('unknown')
df['is_4wd'] = df['is_4wd'].fillna(0)

fig = px.histogram(df, x='price', nbins=50, title='Distribution of Vehicle Prices')
fig.update_xaxes(title='Price')
fig.update_yaxes(title='Count')
st.plotly_chart(fig)

fig = px.scatter(df, x='odometer', y='price', color='condition', 
   title='Price vs. Odometer (Colored by Condition)')
fig.update_xaxes(title='Odometer (miles)')
fig.update_yaxes(title='Price')
st.plotly_chart(fig)

avg_price_by_type = df.groupby('type')['price'].mean().reset_index()
fig = px.bar(avg_price_by_type, x='type', y='price', title='Average Price by Vehicle Type')
fig.update_xaxes(title='Vehicle Type')
fig.update_yaxes(title='Average Price')
st.plotly_chart(fig)

fig = px.line(df.groupby('model_year')['price'].mean().reset_index(), 
 x='model_year', y='price', title='Trend of Average Price by Model Year')
fig.update_xaxes(title='Model Year')
fig.update_yaxes(title='Average Price')
st.plotly_chart(fig)