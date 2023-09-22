from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import plotly.express as px
import plotly.io as pio


def frontpage_start(request):
    fig = px.line(x=[1, 2, 3, 4], y=[10, 11, 12, 13])
    graph_html = pio.to_html(fig, full_html=False)
    return render(request, 'frontpage/frontpage.html', {'graph': graph_html})


# Create your views here.
