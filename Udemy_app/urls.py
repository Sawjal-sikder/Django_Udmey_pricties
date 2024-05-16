from django.urls import path
from . import views
urlpatterns = [
    path('<str:month>', views.monthly_chart, name='monthly_chart'),
]
