from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, CDSView, GroupFilter, HoverTool
from bokeh.io import output_file
from bokeh.layouts import column, gridplot
from bokeh.models import TabPanel, Tabs

from read_laliga_data import real_games1516, real_games1617, real_games1718, real_games1819, barca_games1516, \
    barca_games1617, barca_games1718, barca_games1819, goals_15_16, goals_16_17, goals_17_18, goals_18_19

output_file("LaLigaStats.html")

# Real vs Barca Race
real_cds1516 = ColumnDataSource(real_games1516)
barca_cds1516 = ColumnDataSource(barca_games1516)
real_cds1617 = ColumnDataSource(real_games1617)
barca_cds1617 = ColumnDataSource(barca_games1617)
real_cds1718 = ColumnDataSource(real_games1718)
barca_cds1718 = ColumnDataSource(barca_games1718)
real_cds1819 = ColumnDataSource(real_games1819)
barca_cds1819 = ColumnDataSource(barca_games1819)

select_tools = ['box_select', 'crosshair', 'lasso_select', 'poly_select', 'tap', 'pan', 'box_zoom', 'zoom_in', 'reset']

# figure for season 15/16
fig = figure(width=800,
             height=500,
             x_axis_type="datetime",
             title="Real Madrid vs Barcelona season 15/16",
             x_axis_label="Date",
             y_axis_label="Points Won",
             tools=select_tools)

fig.step('Date', 'RealPoints',
         color='#abcc33',
         alpha=0.8,
         legend_label="Real Madrid",
         source=real_cds1516,
         line_width=4,
         selection_color='#DD4545',
         nonselection_color='lightgray',
         nonselection_alpha=0.5)

fig.step('Date', 'BarcaPoints',
         color='#ab4386',
         alpha=0.8,
         legend_label="Barcelona",
         source=barca_cds1516,
         line_width=4)

fig.legend.location = "top_left"

# figure for season 16/17
fig2 = figure(width=800,
              height=500,
              x_axis_type="datetime",
              title="Real Madrid vs Barcelona season 16/17",
              x_axis_label="Date",
              y_axis_label="Points Won",
              tools=select_tools)

fig2.step('Date', 'RealPoints',
          color='#abcc33',
          alpha=0.8,
          legend_label="Real Madrid",
          source=real_cds1617,
          line_width=4)

fig2.step('Date', 'BarcaPoints',
          color='#ab4386',
          alpha=0.8,
          legend_label="Barcelona",
          source=barca_cds1617,
          line_width=4)

fig2.legend.location = "top_left"

# figure for season 17/18
fig3 = figure(width=800,
              height=500,
              x_axis_type="datetime",
              title="Real Madrid vs Barcelona season 17/18",
              x_axis_label="Date",
              y_axis_label="Points Won",
              tools=select_tools)

fig3.step('Date', 'RealPoints',
          color='#abcc33',
          alpha=0.8,
          legend_label="Real Madrid",
          source=real_cds1718,
          line_width=4)

fig3.step('Date', 'BarcaPoints',
          color='#ab4386',
          alpha=0.8,
          legend_label="Barcelona",
          source=barca_cds1718,
          line_width=4)

fig3.legend.location = "top_left"

# figure for season 18/19
fig4 = figure(width=800,
              height=500,
              x_axis_type="datetime",
              title="Real Madrid vs Barcelona season 18/19",
              x_axis_label="Date",
              y_axis_label="Points Won",
              tools=select_tools)

fig4.step('Date', 'RealPoints',
          color='#abcc33',
          alpha=0.8,
          legend_label="Real Madrid",
          source=real_cds1819,
          line_width=4)

fig4.step('Date', 'BarcaPoints',
          color='#ab4386',
          alpha=0.8,
          legend_label="Barcelona",
          source=barca_cds1819,
          line_width=4)

fig4.legend.location = "top_left"

# Goals Scored per Match Day (all teams)
goals_15_16_cds = ColumnDataSource(goals_15_16)
goals_16_17_cds = ColumnDataSource(goals_16_17)
goals_17_18_cds = ColumnDataSource(goals_17_18)
goals_18_19_cds = ColumnDataSource(goals_18_19)

# Format the Tooltip
tooltips = [("Date", "@Date{%F}"),
            ("Home Goals", "@FTHG"),
            ("Away Goals", "@FTAG")]

formatters = {'@Date': 'datetime'}

# figure for season 15/16
fig5 = figure(width=800,
              height=500,
              x_axis_type="datetime",
              title="Goals in season 15/16",
              x_axis_label="Date",
              y_axis_label="Goals Scored",
              tools=select_tools,)

fig5.square('Date', 'FTHG',
                 color='#ab51bb',
                 alpha=0.8,
                 legend_label="Home Goals",
                 source=goals_15_16_cds,
                 size=10,
                 nonselection_color='lightgray',
                 nonselection_alpha=0.5,
                 hover_color='yellow',
                 hover_alpha=0.8)

fig5.circle('Date', 'FTAG',
                 color='#24ccdd',
                 alpha=0.8,
                 legend_label="Away Goals",
                 source=goals_15_16_cds,
                 size=10,
                 nonselection_color='lightgray',
                 nonselection_alpha=0.5,
                 hover_color='yellow',
                 hover_alpha=0.8,
                 )

fig5.add_tools(HoverTool(tooltips=tooltips, formatters=formatters))
fig5.legend.click_policy = "mute"

# figure for season 16/17
fig6 = figure(width=800,
              height=500,
              x_axis_type="datetime",
              title="Goals in season 16/17",
              x_axis_label="Date",
              y_axis_label="Goals Scored",
              tools=select_tools)

fig6.square('Date', 'FTHG',
            color='#ab51bb',
            alpha=0.8,
            legend_label="Home Goals",
            source=goals_16_17_cds,
            size=10,
            nonselection_color='lightgray',
            nonselection_alpha=0.5)

fig6.circle('Date', 'FTAG',
            color='#24ccdd',
            alpha=0.8,
            legend_label="Away Goals",
            source=goals_16_17_cds,
            size=10,
            nonselection_color='lightgray',
            nonselection_alpha=0.5)

fig6.add_tools(HoverTool(tooltips=tooltips, formatters=formatters))
fig6.legend.click_policy = "mute"

# figure for season 17/18
fig7 = figure(width=800,
              height=500,
              x_axis_type="datetime",
              title="Goals in season 17/18",
              x_axis_label="Date",
              y_axis_label="Goals Scored",
              tools=select_tools)

fig7.square('Date', 'FTHG',
            color='#ab51bb',
            alpha=0.8,
            legend_label="Home Goals",
            source=goals_17_18_cds,
            size=10,
            nonselection_color='lightgray',
            nonselection_alpha=0.5)

fig7.circle('Date', 'FTAG',
            color='#24ccdd',
            alpha=0.8,
            legend_label="Away Goals",
            source=goals_17_18_cds,
            size=10,
            nonselection_color='lightgray',
            nonselection_alpha=0.5)

fig7.add_tools(HoverTool(tooltips=tooltips, formatters=formatters))
fig7.legend.click_policy = "mute"

# figure for season 18/19
fig8 = figure(width=800,
              height=500,
              x_axis_type="datetime",
              title="Goals in season 18/19",
              x_axis_label="Date",
              y_axis_label="Goals Scored",
              tools=select_tools)

fig8.square('Date', 'FTHG',
            color='#ab51bb',
            alpha=0.8,
            legend_label="Home Goals",
            source=goals_18_19_cds,
            size=10,
            nonselection_color='lightgray',
            nonselection_alpha=0.5)

fig8.circle('Date', 'FTAG',
            color='#24ccdd',
            alpha=0.8,
            legend_label="Away Goals",
            source=goals_18_19_cds,
            size=10,
            nonselection_color='lightgray',
            nonselection_alpha=0.5)

fig8.add_tools(HoverTool(tooltips=tooltips, formatters=formatters))
fig8.legend.click_policy = 'mute'

# fig5.x_range = fig6.x_range = fig7.x_range = fig8.x_range
print(dir(fig5.x_range))

# arrange all figures in two 2x2 grids each belonging to a separate tab
grid_plot = gridplot([[fig, fig2], [fig3, fig4]], toolbar_location='left')
grid_plot2 = gridplot([[fig5, fig6], [fig7, fig8]], toolbar_location='left')
tab1 = TabPanel(child=grid_plot, title="Real vs Barca Race")
tab2 = TabPanel(child=grid_plot2, title="Goals per Match Day")

show(Tabs(tabs=[tab1, tab2]))
