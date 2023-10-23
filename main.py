import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample data for demonstration
data = pd.DataFrame({'X': [1, 2, 3, 4, 5], 'Y': [2, 4, 5, 4, 5]})

# Create a Dash web app
app = dash.Dash(__name__)

# Define the layout of the web app
app.layout = html.Div([
    html.H1("Simple Linear Regression Web App"),
    dcc.Input(id='input-x', type='number', placeholder='Enter X value'),
    html.Button('Predict', id='predict-button'),
    html.Div(id='output-prediction')
])

# Define a callback function for making predictions
@app.callback(
    Output('output-prediction', 'children'),
    [Input('predict-button', 'n_clicks')],
    [dash.dependencies.State('input-x', 'value')]
)
def predict(n_clicks, input_x):
    if n_clicks is None:
        return 'Enter an X value and click "Predict"'
    else:
        # Fit a simple linear regression model on the sample data
        model = LinearRegression()
        model.fit(data[['X']], data['Y'])

        # Make a prediction
        prediction = model.predict([[input_x]])[0]

        return f'Prediction for X={input_x}: Y={prediction:.2f}'

if __name__ == '__main__':
    app.run_server(debug=True)
