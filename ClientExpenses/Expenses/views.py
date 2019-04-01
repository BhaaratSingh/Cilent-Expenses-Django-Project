from django.shortcuts import render
from django.views import  generic
from django.db.models import  Count, Q, F
from .models import(Client,Expenses)


class ClientsListAPIView(generic.ListView):
    queryset = Client.objects.all
    template_name = 'All Templates/index.html'
    context_object_name = 'clients'

class ExpensesDetailsView(generic.ListView):
    #queryset = Expenses.objects.all
    model = Expenses
    template_name = 'All Templates/expenses.html'
    context_object_name = 'expenses'

    def get_queryset(self):
        c_id = self.request.GET.get('c_id')
        print("c_id",c_id)
        queryset = Expenses.objects.filter(client= c_id)
        return queryset

