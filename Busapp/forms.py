from django import forms 

class Ticket(forms.Form):
    Bus_No =forms.IntegerField()
    Destination = forms.CharField(max_length=500)
    No_of_Persons = forms.IntegerField()

