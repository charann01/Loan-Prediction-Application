from django.urls import path
from .views import SingleUserReport

urlpatterns = [
    path('single/',SingleUserReport,name='single-report')
]