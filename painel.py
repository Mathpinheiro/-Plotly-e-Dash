import dash
from dash import dcc, html  # Importações atualizadas
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Crie uma instância do aplicativo Dash
app = dash.Dash(__name__)

# Exemplo de conjunto de dados
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "NYC", "NYC", "NYC"]
})

# Crie um gráfico usando Plotly Express
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# Definindo o layout do painel
app.layout = html.Div(children=[
    html.H1(children='Painel de Controle com Dash e Plotly'),

    html.Div(children='''
        Um exemplo simples de painel interativo.
    '''),

    # Adiciona o gráfico ao layout
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# Rodando o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
