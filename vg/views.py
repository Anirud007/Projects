from django.shortcuts import render, redirect,HttpResponse
from .models import *

# Create your views here.
def recepies(request):
    if request.method == 'POST':
        data = request.POST
        r_name = data.get('receipe_name')
        r_des = data.get('receipe_description')
        r_image = request.FILES.get('recepie_image')
        
        Recepie.objects.create(r_name = r_name,
                            r_des = r_des,
                            r_image = r_image
                        )
    
        return redirect('/')
    queryset = Recepie.objects.all()
    context = {
        'recepies': queryset
    }   
    return render(request, 'recepies.html', context)

def update_r(request,id ):
    queryset = Recepie.objects.get(id = id)
    context = {'recepie': queryset}
    return render(request, 'update.html', context)

def delete_r(request,id):
    queryset = Recepie.objects.get(id = id)
    queryset.delete()
    return redirect("/")
