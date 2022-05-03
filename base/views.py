from webbrowser import get
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from base.forms import myForm
from .models import Invoice
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def home(request):
    all_invoices = Invoice.objects.all()
    context = {'all_invoices': all_invoices}
    return render(request, 'base/templates/index.html', context)

def add(request):
    if request.method == "POST" or None:
        form = myForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            form = myForm()
            return render(request, 'base/templates/add.html', {'form': form})
    else:
        form = myForm()
        return render(request, 'base/templates/add.html')

def delete(request, id):
    invoice = Invoice.objects.get(id=id)
    invoice.delete()
    return HttpResponseRedirect(reverse('home'))

def invoice(request, id):
    invoice_detail = Invoice.objects.get(id=id)
    context = {'invoice_detail': invoice_detail}
    return render(request, 'base/templates/invoice.html', context)

def update(request, id): 
    invoice_update = Invoice.objects.get(id=id)
    form = myForm(instance=invoice_update)
    
    if request.method == 'POST':
        form = myForm(request.POST, instance=invoice_update)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form': form}
    return render(request, 'base/templates/update.html', context)

