from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)
cur = pd.DataFrame()

stat_df = pd.read_csv('new csv files/stat_df.csv')
maps = pd.read_csv('original csv files/match_map_stats_000000000000.csv')

maps = maps.rename(columns={"match_winner": "match_winner_team", "map_winner": "map_winner_team"})

stat_df = pd.merge(stat_df, maps, on=['match_id', 'map_name'])
stat_df = stat_df.drop_duplicates(subset=['match_id', 'map_name', 'player', 'Eliminations'])

vals = stat_df.stage.unique().tolist()
playoffs = []
for i in vals:
    valid = ['Title', 'Playoffs', 'Championship', 'Postseason', 'Summer', 'Countdown', 'May', 'June']
    for j in valid:
        if j in i and not('Knockouts' in i or 'Qualifiers' in i):
            playoffs.append(i)

app.layout = html.Div([
    html.H4('Average Stat by Player, Hero, and Stage'),
    dcc.Dropdown(
        id="dropdown",
        options=stat_df.player.unique(),
        clearable=False,
    ),
    dcc.Dropdown(
        id="dropdown2",
        clearable=False,
    ),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("dropdown2", "options"),
    Input("dropdown", "value"))

def set_hero_options(player):
    cur = stat_df[stat_df['player'] == player]
    vals = ['All']
    vals.extend(cur.hero.unique())
    return vals

@app.callback(
    Output("dropdown2", "value"),
    Input("dropdown2", "options"))

def set_hero_value(heroes):
    return 'All'


@app.callback(
    Output("graph", "figure"),
    Input("dropdown", "value"),
    Input("dropdown2", "value"))


def update_bar_chart(player, hero):
    cur = stat_df[stat_df['player'] == player]
    if hero != 'All':
        cur = cur[cur['hero'] == hero] 
    cur = cur.groupby(['stage'])['Stat'].mean().reset_index()
    fig = px.bar(cur, x="stage", y="Stat", barmode='group')
    return fig


app.run_server(debug=True)