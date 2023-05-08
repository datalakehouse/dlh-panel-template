import panel as pn
import pandas as pd
import hvplot.pandas

pn.extension()

# Dashboard 2: Python script
data2 = {'Category': ['E', 'F', 'G', 'H'], 'Value1': [5, 6, 7, 8], 'Value2': [8, 7, 6, 5], 'Value3': [50, 60, 70, 80]}
df2 = pd.DataFrame(data2)

bar_plot2 = df2.hvplot.bar(x='Category', y='Value1', title='Bar Plot')
line_plot2 = df2.hvplot.line(x='Category', y=['Value1', 'Value2'], title='Line Plot')
scatter_plot2 = df2.hvplot.scatter(x='Value1', y='Value2', title='Scatter Plot')
area_plot2 = df2.hvplot.area(x='Category', y='Value3', title='Area Plot')

row3 = pn.Row(bar_plot2, line_plot2)
row4 = pn.Row(scatter_plot2, area_plot2)

template2 = pn.template.FastListTemplate(title='Dashboard 2', main=[row3, row4])

template2.servable()
