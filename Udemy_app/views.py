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
    "december" : "December is the seceond month of the year",
}

# Create your views here.

def index(request):
    list_of_months = ""
    months = monthly_chalengers.keys()
    for month in months:
        month_path = reverse("monthly_chart", args=[month])
        list_of_months += f"<a href=\'{month_path}\'> <li> {month.capitalize()} </li> </a>"
    data_response = f'<ul class="list-group">{list_of_months}</ul>'
    return HttpResponse(data_response)

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
