from django.urls import path
from .views import SingleUserReport, SheetReport

urlpatterns = [
    path('single/',SingleUserReport,name='single-report'),
    path('sheet/',SheetReport,name='sheet-report')
]