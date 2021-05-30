from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,authenticate
from .forms import applyloan,loanStatus
from django.contrib import messages
from .models import loan
# Create your views here.
def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')
def all_loan(request):
    loans = loan.objects.all()
    req = loanStatus()
    return render(request, 'all_loan.html',{'loans':loans,'req':req})

# def profileapply_loan(request):
#     profile = Profile.objects.all()
#     v =request.user.profile.Category
#     print("DDDDDDDDd",v)
    
#     return render(request, 'apply_loan.html',context)

def apply_loan(request):
    # if request.method == 'GET':
    #     u_form = applyloan()
    #     context ={
    #         'u_form': u_form,
    #         'active':'btn-primary'
    #     }
    #     print('gettttt--')
    #     return render(request,'apply_loan.html',context)
    if request.method =='POST':
            u_form = applyloan(request.POST)
            if u_form.is_valid():
                u_form.save()
                # username = form.cleaned_data.get('username')
                Amount = u_form.cleaned_data.get('Amount')
                print("saved")
    
                messages.success(request,f'Your Account Has Been Updated')
                print("valid")
                return redirect('apply_loan')

    else:
        u_form = applyloan()
    # context = {
    #             'u_form': u_form
    #             }
    return render(request, 'apply_loan.html',{'u_form':u_form})

# def apply_loan(request):
#     form = applyloan()
#     if request.method == 'GET':
#         form = applyloan()
#         context ={
#             'form': form,
#             'active':'btn-primary'
#         }
#         print('gettttt--')
#         return render(request,'apply_loan.html',context)
#     if request.method =='POST':
#             form = applyloan(request.POST,instance=request.user)
#             if form.is_valid():
#                 form.save()
#                 # messages.success(request,f'Your Account Has Been Updated')
#                 print("valid")
#                 return redirect('apply_loan')

#     else:
#         form = applyloan(instance=request.user)
#     context = {
#                 'form' : form,
#                 }
#     return render(request, 'apply_loan.html',{'context':context})
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



# def signup(request):
#     # profile_id = request.session.get('ref_profile')
#     # print('profile_id', profile_id)
#     form = UserCreationForm(request.POST or None)
#     if form.is_valid():
#         if profile_id is not None:
#             recomended_by_profile = profile.objects.get(id=profile_id)

#             instance = form.save()
#             register_user = User.objects.get(id=instance.id)
#             register_profile = profile.objects.get(user =register_user)
#             register_profile_recommended_by = recomended_by_profile.user
#             register_profile.save
#         else:
#             form.save()
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password1')
#         user = authenticate(username = username, password=password)
#         login(request,User)
#         return redirect('home.html')
#     context = {'form':form}
#     return render(request, 'signup.html',context)
