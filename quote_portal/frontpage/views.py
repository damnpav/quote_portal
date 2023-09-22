from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import plotly.io
from . import quotes_data_update as qdu


def frontpage_start(request):
    symbols = ['EURUSD=X', 'GBPUSD=X']
    quotes_data_list = qdu.get_data(symbols)
    trace_list = []

    # Create a trace for each DataFrame in the list
    for idx, df in enumerate(quotes_data_list):
        trace = go.Scatter(x=df['Datetime'], y=df['Close'], name=f'{symbols[idx]}')
        trace_list.append(trace)

    # Define buttons for the dropdown menu, one for each DataFrame and one to show all
    buttons = [dict(label='All', method='update', args=[{'visible': [True] * len(quotes_data_list)}])]
    buttons += [
        dict(label=f'{symbols[idx]}', method='update',
             args=[{'visible': [idx == j for j in range(len(quotes_data_list))]}])
        for idx in range(len(quotes_data_list))]

    # Define layout with dropdown menu
    layout = go.Layout(
        title='Currencies Plot',
        updatemenus=[dict(buttons=buttons)]
    )

    # Create Figure and convert to HTML
    fig = go.Figure(data=trace_list, layout=layout)
    graph_html = plotly.io.to_html(fig, full_html=False)
    return render(request, 'frontpage.html', {'graph': graph_html})


# Create your views here.
