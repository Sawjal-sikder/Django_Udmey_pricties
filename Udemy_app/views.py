from django.http import HttpResponse, HttpResponseNotFound

from django.shortcuts import render

# Create your views here.
def monthly_chart(request, month):
    chart_text = None
    if month == 'january':
        chart_text = 'January is the first month of the year'
    elif month == 'february':
        chart_text = 'February is the seceond month of the year'
    elif month == 'march':
        chart_text = 'March is the third month of the year'
    elif month == 'april':
        chart_text = 'April is the forth month of the year'
    else:
        return HttpResponseNotFound(f"{month} is incorrect in chart")

    return HttpResponse(chart_text)