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
            
            
        messages.success(request, 'Account Created Successfully!. Check out our Email later :)')

            return redirect('login')
    else:
        form = CreateUserForm
    context = {
            'title':title,
            'form':form,
                        }
    return render(request, 'registration/register.html', context)

def loginpage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)
