import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Genestack RNA-Seq Dashboard'),

    html.Div(children='''
        A dashboard for RNA-Seq data analysis using Genestack ODM.
    '''),

    # Add more components here
])

if __name__ == '__main__':
    app.run_server(debug=True)
