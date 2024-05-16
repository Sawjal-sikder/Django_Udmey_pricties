from django.http import HttpResponse, HttpResponseNotFound


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

def monthly_chart_by_number(request, month):
    return HttpResponse(month)


def monthly_chart(request, month):
    try:
        chart_text = monthly_chalengers[month]
        return HttpResponse(chart_text)
    except:
        return HttpResponseNotFound(f"{month} is incorrect in chart")
