import plotly.plotly as py

py.sign_in('danielebarros', 'bsA0eORCKDQkj03kLB1G')

import plotly.figure_factory as ff

import pandas as pd

df = pd.read_csv('/home/dani/Documentos/projetos/algorithms_common/Graficos/exemplo2.csv')

fig = ff.create_gantt(df, colors=['#333F44', '#93e4c1'], index_col='Complete', show_colorbar=True,
                      bar_width=0.2, showgrid_x=True, showgrid_y=True)
py.iplot(fig, filename='exemplo2', world_readable=True)