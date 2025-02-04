import plotly.express as px 

data = {
    'Country':['Taiwan', 'United States', 'Canada', 'Brazil', 'India'],
    'Values':[100, 80, 60, 40, 20]
}

fig = px.choropleth(
    data,
    locations='Country',
    locationmode='country names',
    color='Values',
    color_continuous_scale='rdgy',
    title='Choropleth Map of Values by Country'
)
fig.show()
