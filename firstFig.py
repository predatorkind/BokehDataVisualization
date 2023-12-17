from datetime import datetime
import numpy as np
from bokeh.io import output_file
from bokeh.plotting import figure, show

# setup data
x = np.linspace(1, 11, 10)
y = [234, 965, 201, 198, 302, 175, 633, 186, 432, 211]
cum_sum = np.cumsum(y)

output_file("first_figure.html",
            title="Empty Bokeh Figure")

fig = figure(background_fill_color="gray",
             background_fill_alpha=0.5,
             border_fill_color="green",
             border_fill_alpha=0.25,
             height=600,
             width=1000,
             x_axis_label='Day',
             x_minor_ticks=2,
             x_axis_location='above',
             x_range=(0, 12),
             y_axis_label='Y Values',
             y_axis_type='linear',
             y_axis_location='left',
             y_range=(0, 5000),
             title='Example Figure',
             title_location='right',
             toolbar_location='below',
             tools='save',
             )

# fig.grid.grid_line_color = None

fig.vbar(x=x, bottom=0, top=y, color='#1004aa', alpha=0.6, width=1, legend_label='Daily')

fig.line(x=x, y=cum_sum, color='green', line_width=4, legend_label='Cumulative Sum')

fig.legend.location = "top_left"

show(fig)
