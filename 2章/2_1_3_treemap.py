import plotly.express as px
import numpy as np
import kaleido
import plotly.io as pio

df = px.data.gapminder().query("year == 2007")
fig = px.treemap(df, path=[px.Constant("world"), 'continent', 'country'], values='pop',
                 color='lifeExp', hover_data=['iso_alpha'],
                 color_continuous_scale='RdBu',
                 color_continuous_midpoint=np.average(df['lifeExp'], weights=df['pop']))
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

fig.write_image("2_1_3_treemap_test.png")
# fig.write_image("2_1_3_treemap_test.svg") # memo 後回し

# plotly-orca
