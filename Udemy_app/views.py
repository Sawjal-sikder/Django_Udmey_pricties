from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render


# Create your Chalengers.

monthly_chalengers = {
    "january" : "January is the 1st month of the year",
    "february" : "February is the 2nd month of the year",
    "march" : "March is the 3rd month of the year",
    "april" : "April is the 4th month of the year",
    "may" : "May is the first 5th of the year",
    "june" : "June is the 6th month of the year",
    "july" : "July is the 7th month of the year",
    "august" : "August is the 8th month of the year",
    "september" : "September is the 9th month of the year",
    "october" : "October is the 10th month of the year",
    "november" : "November is the 11 th month of the year",
    "december" : "December is the 12th month of the year",
}

# Create your views here.

def index(request):

    list_months = ""
    months = list(monthly_chalengers.keys())
    for month in months:
        month_path = reverse('monthly_chart', args=[month])
        list_months += f" <a href=\"{month_path}\">{month}</a> "
    response_data = f"<ul> {list_months} </ul> "
    return HttpResponse(response_data)

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
        return HttpResponse(chart_text)
    except:
        return HttpResponseNotFound(f"{month} is incorrect in chart")
