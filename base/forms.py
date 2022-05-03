from django import forms
from base.models import Invoice

class myForm(forms.ModelForm):
    supplier = forms.CharField(error_messages={'required': 'Please enter Supplier'})
    invoiceNumber = forms.CharField(error_messages={'required': 'Please enter Invoice Number'})
    reason = forms.CharField(error_messages={'required': 'Please enter reason'})
    reportedTo = forms.CharField(error_messages={'required': 'Please enter reported to'})
    solved = forms.CharField(error_messages={'required': 'Please enter if this is solved or not'})

    class Meta:
        model = Invoice
        fields = ("supplier", "invoiceNumber", "reason", "reportedTo", "solved")

