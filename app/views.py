from django.shortcuts import render,redirect,get_object_or_404
from app.models import Employee
from app.forms import empForm


# Create your views here.
def view_reg(request):
    if request.method=='POST':
        form = empForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/td/')
        
    else:
        form=empForm()

    return render(request, 'app/reg.html', {'form':form})

def view_td(request):
    if request.method=='GET':
        s=Employee.objects.all()
        d1={'emp':s}
        resp=render(request,'app/td.html',context=d1)
        return resp
    
def view_index(request):
    resp=render(request,'app/index.html')   
    return resp 
    

def delete_view(request,id):
    context={}
    obj=get_object_or_404(Employee,id=id)
    if request.method=='POST':
        obj.delete()
        return redirect('/td/')
    return render(request,'app/delete.html',context)

def update_view(request,id):
    context={}
    obj=get_object_or_404(Employee,id=id)
    form=empForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/td/')
    context['form']=form
    return render(request,'app/reg.html',context)

        

    
    



