from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def index(request):
    projects=Project.objects.all()

    if 'item_name' in request.GET:
        item_name=request.GET['item_name']
        projects=projects.filter(title__icontains=item_name)
    else:
        projects=Project.objects.all()

    return render(request,'index.html',{'projects':projects})
def registeruser(request):
    title = 'Register - awwards'
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()