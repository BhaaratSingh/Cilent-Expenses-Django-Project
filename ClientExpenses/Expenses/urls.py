
from django.contrib import admin
from django.urls import path,re_path
from .views import (ClientsListAPIView,ExpensesDetailsView)

urlpatterns = [
    re_path(r'^index/$',ClientsListAPIView.as_view(), name="ClientsListAPIView"),
    re_path(r'^client/allexpenses/$',ExpensesDetailsView.as_view(), name="ExpensesDetailsView"),
]
