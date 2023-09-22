from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import plotly.express as px
import plotly.io as pio
from quotes_data_update import get_data


def frontpage_start(request):
    quote_data = get_data('EURUSD=X')
    fig = px.line(quote_data, x='Datetime', y='Close')
    graph_html = pio.to_html(fig, full_html=False)
    return render(request, 'frontpage.html', {'graph': graph_html})


# Create your views here.
