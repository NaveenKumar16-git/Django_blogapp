from django.shortcuts import render
from datetime import datetime
from Busapp.models import BusDetails
from Busapp.forms import Ticket
from django.http import HttpResponseRedirect 
# Create your views here.
def display(request):
    bus_details = BusDetails.objects.all()
    return render(request,'display.html',{'bus_details':bus_details})

def home(request):
    if request.method == 'POST':
        form = Ticket(request.POST)
        if form.is_valid():
            bus_no = form.cleaned_data['Bus_No']
            bus = BusDetails.objects.get(Bus_No=bus_no)
            dest_list = eval(bus.Destinations)
            index=dest_list.index(form.cleaned_data['Destination'])
            cost_list = eval(bus.TicketsCosts)
            cost = int(cost_list[index])
            no_of_persons=int(form.cleaned_data['No_of_Persons'])
            if no_of_persons > bus.Seats_Available:
                 return render(request,'Invalid.html')
            ticket_amount = cost*no_of_persons
            return render(request,'Ticket.html',{'form':form,'Ticket_amount':ticket_amount})
        else:
            form = Ticket(request.POST)
            
            return render(request,'home.html',{'form':form})
    else:
            form = Ticket(request.POST)
            return render(request,'home.html',{'form':form})
        

        