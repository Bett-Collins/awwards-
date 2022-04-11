from awwards.models import Profile,Project
from django.shortcuts import render,redirect
from .forms import CreateUserForm,ProfileForm,ProjectForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout as dj_login
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Myprofile,Myprojects
from .serializer import MerchSerializer




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

			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username or password is incorrect')

		context = {}
		return render(request, 'registration/login.html', context)



def logoutuser(request):
    
    return redirect(reverse('login'))

def create_profile(request):
    current_user = request.user
    
    if request.method=='POST':
        form = ProfileForm(request.POST,request.FILES)
        if request.current_user.is_authenticated:
            form.instance.user = request.user
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user

            profile.save()
        return redirect('index')
    else:
        form=ProfileForm()

    return render(request,'create-profile.html',{"form":form})

def profile(request):
    current_user = request.user
    profile =Profile.objects.get(user=current_user)
    projects=Project.objects.filter(user=current_user)

    return render(request,'profile.html',{"projects":projects,"profile":profile})

def new_project(request):
    current_user = request.user
    profile =Profile.objects.get(user=current_user)
    if request.method =='POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.username = current_user
            project.avatar = profile.avatar

            project.save()
    else:
        form = ProjectForm()

    return render(request,'project.html',{"form":form})

class MerchList(APIView):
    def get(self, request, format=None):
        all_merch = Myprojects.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)

class MerchList(APIView):
    def get(self, request, format=None):
        all_merch = Myprofile.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)




