from create_bar_chart_race_data import CreateBarChartRaceData
import plotly.express as px
import pandas as pd
from raceplotly.plots import barplot

create_bar_chart_race_data = CreateBarChartRaceData()
cumulative_votes_by_time_candidate = create_bar_chart_race_data.create_cumulative_votes_by_time_candidate()
covid_19_confirmed = create_bar_chart_race_data.create_covid_19_confirmed()
early_collected = cumulative_votes_by_time_candidate[cumulative_votes_by_time_candidate["collected_at"] < pd.to_datetime("2024-01-13 17:30:00")]
max_cumulative_votes = early_collected["cumulative_sum_votes"].max()

# 投開票完成時間：使用 raceplotly 模組
# item_column: 指定類別變數。
# value_column: 指定數值變數。
# time_column: 指定日期時間變數。
# top_entries: 預設為 10。
# frame_duration: 每幀動畫停留的毫秒數。

vote_raceplot = barplot(early_collected, item_column="candidate", value_column="cumulative_sum_votes",
                        time_column="collected_at", top_entries=3)
fig = vote_raceplot.plot(item_label = "Votes collected by candidate", value_label="Number of votes",
                         frame_duration=50)
fig.write_html("bar_chart_race_votes.html")

confirmed_raceplot = barplot(covid_19_confirmed, item_column="country", value_column="confirmed",
                             time_column="reported_on")
fig = confirmed_raceplot.plot(item_label = "Confirmed by country", value_label="Number of cases",
                              frame_duration=50)
fig.write_html("bar_chart_race_confirmed.html")