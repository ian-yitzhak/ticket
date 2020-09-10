from django.shortcuts import render


from . models import Ticket

def index(request):


    queryset = Ticket.objects.filter(user=request.user, accepted=True)


    return render (request , 'index.html'  , { 'queryset': queryset })
