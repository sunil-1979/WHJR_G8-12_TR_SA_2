import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
%matplotlib inline
 
df = pd.read_csv("https://raw.githubusercontent.com/jainharshit27/datasets/main/runs_by_team_ball_by_ball.csv")
 
df.head()
 
df_team_total_runs = df.groupby("batting_team").sum()


'''
We want df_team_GT10K to be created such that only those observations
are accepted which have total_runs value more than 10000
like df_team_total_runs["total_runs"]>10000
'''
df_team_GT10K = df_team_total_runs[''' type here ''']


'''
We want to plot bar chart for df_team_GT10K.index value as categories
or x-axis of the chart and df_team_GT10K["total_runs"] as y-axis.
'''
plt.figure(figsize=(20,5))
plt.title("Runs scored for each player for KKR")
plt.bar(''' type here ''')
plt.show()