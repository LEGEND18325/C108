import csv
import plotly.figure_factory as px
import pandas as pd


fileName=pd.read_csv('Data.csv')

figure=px.create_distplot([fileName['Height'].tolist()],['Height'],show_hist=False)

figure.show()
