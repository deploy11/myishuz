from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.views.generic import *
# Create your views here.
def home(request):
    category = Category.objects.all().order_by('-id')
    if 'q' in request.GET:
        q = request.GET['q']
        workers = Worker.objects.filter(Q(name__icontains=q)) 
        preum_worker = Worker.objects.filter(preum=True)
    else:
        workers = Worker.objects.all()
        preum_worker = Worker.objects.filter(preum=True)
    con = {'worker':workers,'pre_worker':preum_worker,'category':category}
    return render(request,'home.html',con)

def cate(request):
    qi = request.GET.get('category')
    category = Category.objects.all()
    if category == None:
             workers = Worker.objects.all()
    else:
            workers = Worker.objects.filter(category__name=qi)
    return render(request,'cate.html',{'worker':workers,'category':category,'qi':qi})

def about(request):
     return render(request,'about.html')

class new(CreateView):
    model = Worker
    template_name = 'new.html'
    fields = ['category','name','age','portfolio_website','telegram','instagram','more','image']