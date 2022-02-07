from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from solution.models import Branch, CustomUser, Member
from django.core.mail import send_mail
from .coding import encryption, decryption

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        address = request.POST['address']
        if CustomUser.objects.filter(email=email).exists():
            messages.info(request,"Email already exists")
            return redirect("signup")
        else:
            new_host = CustomUser.objects.create_user(username=email,email=email, password=password, address=address)
            new_host.save()
            user = auth.authenticate(username=email,email=email, password=password)
            auth.login(request,user)
            return redirect('host')
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email,email=email, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("host")
        else:
            messages.info(request,"Invalid credentials")
            return redirect("login")
    else:
        return render(request, 'login.html')

def forgot(request):
    if request.method == 'POST':
        email = request.POST['email']
        if CustomUser.objects.filter(email=email).exists():
            encrypted_email = encryption(email)
            link  = "http://127.0.0.1:8000/reset/"+ encrypted_email
            mail_msg = "Click on the link to reset your password \n" + link
            send_mail("Reset password",mail_msg,'om.surushe20@vit.edu',[email],fail_silently=False,html_message=mail_msg)
            messages.info(request,"Check your email for reset link")
            return redirect("login")
        else:
            messages.info(request,"Email does not exist")
            return redirect("forgot")
    else:
        return render(request, 'forgot.html')

def reset(request,hash):
    email = decryption(hash)
    if request.method == 'POST':
        u = CustomUser.objects.get(username=email)
        u.set_password(request.POST['password'])
        u.save()
        messages.info(request,"Password changed successfully")
        return redirect("login")
    else:
        return render(request, 'reset.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('host')


@login_required(login_url='login')
def host(request):
    return render(request, 'host.html')

def branch(request,hash):
    address = decryption(hash)
    current_user = CustomUser.objects.filter(address=address)
    current_user = current_user[0]
    queue_list = list(Branch.objects.filter(host=current_user))
    for qu in queue_list:
        qu.code = encryption(str(qu.id))
    return render(request,'branch.html',{'queue_list':queue_list})

def locations(request):
    address_list = list(CustomUser.objects.values_list("address",flat=True))
    if request.method == 'POST':
        address = request.POST['address']
        if address in address_list:
            hash_address = encryption(address)
            return redirect('branch',hash=hash_address)

        else:
            messages.info(request,"Please enter a valid address")
            return redirect("locations")
    else:
        return render(request,'locations.html',{'address_list':address_list})

def voter(request,hash):
    id = decryption(hash)
    if request.method == 'POST':
        voter_id = request.POST['voterID']
        if Member.objects.filter(voter_id=voter_id).exists():
            messages.info(request,"Voter id already exists")
            print("Voter id already exists")
            return HttpResponse("Voter id already exists")
        else:
            branch = Branch.objects.get(id=id)
            new_member = Member.objects.create(voter_id=voter_id,branch=branch)
            new_member.token = branch.total + 1
            new_member.save()
            return HttpResponse("Voter added successfully")
    else:
        return render(request,'voter.html')

def que(request,hash):
    id = decryption(hash)
    branch = Branch.objects.filter(id=id)
    return HttpResponse(branch)