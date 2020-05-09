from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from travello.models import Asset


from django.contrib import messages
# Create your views here.
def login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user= auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')

def register(request):

    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username exit')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Eamail Exist')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name,)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'password not matched')
            return redirect('register')
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


#def users(request):
 #   userlist=travello_pc_stock.objects.all()
 #   return render(request, 'index.html', {'Users': userlist})
def submit(request):
        users = User.objects.all()
        return render(request, 'submit.html', {'users':users})

def asset_register(request):
    if request.method == 'POST':
        center = request.POST["center"]
        building = request.POST["building"]
        floor = request.POST["floor"]
        dept = request.POST["dept"]
        location = request.POST["location"]
        belongs = request.POST["belongs"]
        enduser = request.POST["enduser"]
        remarks = request.POST["remarks"]
        CC_number = request.POST["CC_number"]

        assets = Asset(center=center, building=building,floor=floor, dept=dept,location=location,belongs=belongs,enduser=enduser,remarks=remarks,CC_number=CC_number)
        assets.save()
        return render(request, 'asset_list.html')
        #return redirect('asset_list.html')
    else:
        return render(request, 'asset_register.html')

    

def asset_list(request):
    assets = Asset.objects.all()
    return render(request, 'asset_list.html', {'assets':assets})
    #return render(request, 'asset_list.html')
   
        #assets = new Asset()
        