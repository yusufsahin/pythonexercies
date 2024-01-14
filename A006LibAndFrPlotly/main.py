import plotly.graph_objects as go

# Data for the chart
x_data = ['A', 'B', 'C', 'D']
y_data = [10, 15, 7, 12]

# Create a bar chart
fig = go.Figure(data=go.Bar(x=x_data, y=y_data))

# Customize aspects of the chart
fig.update_layout(
    title='Simple Bar Chart',
    xaxis_title='Categories',
    yaxis_title='Values'
)

# Show the chart
fig.show()
