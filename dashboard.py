import lightningchart as lc
import pandas as pd
import time

with open("license_key.txt", "r") as file:  # License key is stored in 'license_key.txt'
    key = file.read()
lc.set_license(key)

dashboard = lc.Dashboard(columns=3, rows=4, theme=lc.Themes.Black)  # initialize Dashboard
chart_ecg = dashboard.ChartXY(column_index=0, row_index=0, column_span=2, title='ECG')  # group charts as you like
chart_pleth = dashboard.ChartXY(column_index=0, row_index=1,column_span=2, title='PLETH')
chart_art = dashboard.ChartXY(column_index=0, row_index=2, column_span=2, title='ART')
chart_co2 = dashboard.ChartXY(column_index=0, row_index=3, column_span=2, title='CO2')
chart_temp = dashboard.GaugeChart(column_index=2, row_index=0, row_span=2)
chart_heartrate = dashboard.GaugeChart(column_index=2, row_index=2, row_span=2)

chart_ecg.set_title_position('left-top').set_title_color(lc.Color(0, 255, 0))  # initialize titles
chart_pleth.set_title_position('left-top').set_title_color(lc.Color(0, 255, 0))
chart_art.set_title_position('left-top').set_title_color(lc.Color(0, 255, 0))
chart_co2.set_title_position('left-top').set_title_color(lc.Color(0, 255, 0))
chart_temp.set_title_color(lc.Color(0, 255, 0)).set_label_font(40)
chart_heartrate.set_title_color(lc.Color(0, 255, 0)).set_label_font(40)

df = pd.read_csv('data/data_cut.csv', header=None)  # read csv
df.fillna(0, inplace=True)  # fill NaN values with 0s
df.columns = ['x', 'Primus/CO2', 'SNUADC/ART', 'SNUADC/PLETH', 'SNUADC/ECG_II', 'Solar8000/BT', 'Solar8000/HR']  # name columns
y_ecg = df['SNUADC/ECG_II'].to_list()  # Extract Ys from DataFrame and cast to list
y_pleth = df['SNUADC/PLETH'].to_list()
y_art = df['SNUADC/ART'].to_list()
y_co2 = df['Primus/CO2'].to_list()
temp = df['Solar8000/BT'].to_list()
heartrate = df['Solar8000/HR'].to_list()
x = df['x'].to_list()  # same with Xs


series_ecg = chart_ecg.add_line_series(
            data_pattern='ProgressiveX')  # add series to chart
series_ecg.set_line_color(lc.Color(0, 255, 0))  # color the line green
x_axis_ecg = chart_ecg.get_default_x_axis()  # get axis
y_axis_ecg = chart_ecg.get_default_y_axis()
x_axis_ecg.set_scroll_strategy(strategy='progressive')  # Set the x_axis_ecg to progressive scroll strategy
x_axis_ecg.set_interval(start=-300, end=300, stop_axis_after=False)  # define intervals for x and y
y_axis_ecg.set_default_interval(start=-0.5, end=1)
x_axis_ecg.set_tick_formatting('')  # this feature is experimental and not yet available in public version
y_axis_ecg.set_tick_formatting('')  # of LightningChart library, it removes axis (only visual purpose)

series_pleth = chart_pleth.add_line_series(  # same with other series and charts
            data_pattern='ProgressiveX')
series_pleth.set_line_color(lc.Color(0, 255, 0))
x_axis_pleth = chart_pleth.get_default_x_axis()
y_axis_pleth = chart_pleth.get_default_y_axis()
x_axis_pleth.set_scroll_strategy(strategy='progressive')
x_axis_pleth.set_interval(start=-300, end=300, stop_axis_after=False)
y_axis_pleth.set_default_interval(start=20, end=60)
x_axis_pleth.set_tick_formatting('')
y_axis_pleth.set_tick_formatting('')

series_art = chart_art.add_line_series(
            data_pattern='ProgressiveX')
series_art.set_line_color(lc.Color(0, 255, 0))
x_axis_art = chart_art.get_default_x_axis()
y_axis_art = chart_art.get_default_y_axis()
x_axis_art.set_scroll_strategy(strategy='progressive')
x_axis_art.set_interval(start=-300, end=300, stop_axis_after=False)
y_axis_art.set_default_interval(start=50, end=150)
x_axis_art.set_tick_formatting('')
y_axis_art.set_tick_formatting('')

series_co2 = chart_co2.add_line_series(
            data_pattern='ProgressiveX')
series_co2.set_line_color(lc.Color(0, 255, 0))
x_axis_co2 = chart_co2.get_default_x_axis()
y_axis_co2 = chart_co2.get_default_y_axis()
x_axis_co2.set_scroll_strategy(strategy='progressive')
x_axis_co2.set_interval(start=-300, end=300, stop_axis_after=False)
y_axis_co2.set_default_interval(start=0, end=50)
x_axis_co2.set_tick_formatting('')
y_axis_co2.set_tick_formatting('')

chart_temp.set_interval(start=25, end=50)  # range of the chart
chart_temp.set_angle_interval(start=225, end=-45)  # angles (visual)
chart_temp.set_thickness(5)  # thickness of the circle
chart_temp.set_slice_color(lc.Color(0, 255, 0))  # color
chart_temp.set_title('TEMP')  # title
chart_temp.set_animations_enabled(False)  # disable animation to minimize distraction

chart_heartrate.set_interval(start=40, end=150)
chart_heartrate.set_angle_interval(start=225, end=-45)
chart_heartrate.set_thickness(5)
chart_heartrate.set_slice_color(lc.Color(0, 255, 0))
chart_heartrate.set_title('Heartrate')
chart_heartrate.set_animations_enabled(False)

series_ecg.set_max_sample_count(10000)
series_pleth.set_max_sample_count(10000)
series_art.set_max_sample_count(10000)
series_co2.set_max_sample_count(10000)

dashboard.open(live=True)

for point in range(0, len(x), 5):
    series_ecg.add(x[point:point+5], y_ecg[point:point+5])
    series_pleth.add(x[point:point+5], y_pleth[point:point+5])
    series_art.add(x[point:point+5], y_art[point:point+5])
    series_co2.add(x[point:point+5], y_co2[point:point+5])

    for i in range(point, point + 5):
        if temp[i] != 0:
            chart_temp.set_value(temp[i])
    for i in range(point, point + 5):
        if heartrate[i] != 0:
            chart_heartrate.set_value(heartrate[i])

    time.sleep(0.01)

dashboard.close()
