import email
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from .models import User

 

def register_view(request):
    if request.method ==  'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('dashboard')
    else: 
      initial_data = { 'username':'','password1':'','password2':""}
      form = UserCreationForm(initial=initial_data)
    return render(request,'infopage/register.html',{'form':form})


def login_view(request):
    if request.method ==  'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
      initial_data = { 'username':'','password':''}
      form = AuthenticationForm(initial=initial_data)
    return render(request,'infopage/login.html',{'form':form})

def dashboard_view(request):
    return render(request,'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')
def index_view(request):
    return render(request,'infopage/index.html')

def user_input_view(request):
    return render(request,'infopage/user_input.html')





def user_input_view(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    email = request.POST.get('email')
    city = request.POST.get('city')
    phone_number = request.POST.get('phone_number')

  
    new_user = User(username=username, email=email, city=city, phone_number=phone_number)
    new_user.save()
    

  return render(request, 'infopage/user_input.html')
def user_details_view(request, user_input_view):
  try:
    user = User.objects.get(pk=user_input_view)
    context = {'user': user}
  except User.DoesNotExist:
    context = {'error_message': 'User not found'}
  return render(request, 'infopage/user_details.html', context)
     
          


     
      
        





