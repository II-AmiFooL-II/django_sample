from django.shortcuts import render
from basic_1.models import tb_1 
# Create your views here.

def home(request):
    if request.method=='GET':
        print(request)
        return render(request, 'home.html')
    

def submit_form(request):
    if request.method=='POST':
        print(request.POST['age'])
        objs = tb_1.objects.all().filter(name=request.POST['name'])
        data = {}
        print(len(objs))
        if len(objs) > 0:
            data['exists'] = 1
        else:
            b = tb_1(name=request.POST['name'], age=request.POST['age'])
            b.save()
            data['exists'] = 0
        print(data)
        return render(request, 'success.html', data)

def view_all(request):
    objs = tb_1.objects.all()
    data = {}
    entries = []
    length = len(objs)
    for i in objs:
        entries.append({'name':i.name,'age':i.age})
    data['entries'] = entries
    data['length'] = length
    return render(request,'view_all.html',data)
