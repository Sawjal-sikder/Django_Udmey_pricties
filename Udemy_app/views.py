from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render


# Create your Chalengers.

monthly_chalengers = {
    "january" : "January is the first month of the year",
    "february" : "February is the seceond month of the year",
    "march" : "March is the first month of the year",
    "april" : "April is the seceond month of the year",
    "may" : "May is the first month of the year",
    "june" : "June is the seceond month of the year",
    "july" : "July is the first month of the year",
    "august" : "August is the seceond month of the year",
    "september" : "September is the first month of the year",
    "october" : "October is the seceond month of the year",
    "november" : "November is the seceond month of the year",
    "december" : None
}

# Create your views here.

def index(request):

    months = monthly_chalengers.keys()

    return render(request, 'index.html', {'months': months})

def monthly_chart_by_number(request, month):
    months = list(monthly_chalengers.keys())
    if month  > len(months):
        return HttpResponseNotFound(f"{month} is incorrect in chart")
    else:
        redrect_month = months[month - 1]
        redrect_path = reverse("monthly_chart", args=[redrect_month])
        return HttpResponseRedirect(redrect_path)


def monthly_chart(request, month):
    try:
        chart_text = monthly_chalengers[month]
        return render(request, 'chalenge.html', {
            'chart_text': chart_text,
            'month_name': month,
        })
    except:
        return HttpResponseNotFound(f"{month} is incorrect in chart")
