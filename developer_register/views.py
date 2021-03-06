from django.shortcuts import render,redirect
from .forms import DeveloperForm
from .models import Developer
from .filters import DeveloperFilter

# Create your views here.

def developer_list(request):
    developer_list =  Developer.objects.all()
    developerfilter = DeveloperFilter(request.GET, queryset=developer_list)
    developer_list = developerfilter.qs
    context = {'developer_list' : developer_list, 'developerfilter' : developerfilter}
    return render(request,"developer_register/developer_list.htm",context)

def developer_form(request,id=0):
    if request.method == "GET":
        if id == 0: 
            form = DeveloperForm()
        else:
            developer = Developer.objects.get(pk = id)
            form = DeveloperForm(instance = developer)
        return render(request, "developer_register/developer_form.htm", {'form': form})
    else:
        if id == 0:
            form = DeveloperForm(request.POST)
        else:
            developer = Developer.objects.get(pk=id)
            form = DeveloperForm(request.POST, instance = developer)
        if form.is_valid():
            form.save()
        return redirect('/developer/list')

def developer_delete(request, id):
    developer = Developer.objects.get(pk=id)
    developer.delete()
    return redirect('/developer/list')
        
