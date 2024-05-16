from django.urls import path
from . import views
urlpatterns = [
   path('<int:month>', views.monthly_chart_by_number, name='monthly_chart_by_number'),
   path('<str:month>', views.monthly_chart, name='monthly_chart'),
]
