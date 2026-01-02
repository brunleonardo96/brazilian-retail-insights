import json
import pandas as pd
import plotly.express as px

# 1. Carico i dati CSV
df = pd.read_csv('geo_spending_results.csv')

# 2. Carico il GeoJSON del Brasile
with open('brazil_states.json') as f:
    geojson_local = json.load(f)

# 3. Creazione della mappa
fig = px.choropleth(
    df,
    geojson=geojson_local,
    locations='customer_state',
    featureidkey="id",
    color='total_revenue',
    hover_name='customer_state',
    title='Brazilian E-commerce Revenue by State (Olist)',
    color_continuous_scale="Viridis"
)

fig.update_geos(fitbounds="locations", visible=False)
fig.show()

# 4. Salva il risultato
fig.write_html("brazil_revenue_map.html")