from django.shortcuts import render, redirect
from  django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.views.generic.base import TemplateView
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

from .forms import employer_registrationForm
from .forms import employee_registrationForm
from .forms import jobForm
from .models import employer_registration
from .models import employee_registration
from .models import job
from .models import acknowledgement
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def userreg(request):
    if request.method=="POST":
        username=request.POST.get('username')
        phone=request.POST.get('phone')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        location=request.POST.get('location')
        email=request.POST.get('email')
        image=request.FILES['image']
        f=FileSystemStorage()
        fs=f.save(image.name,image)
        password=request.POST.get('password')
        registration=employer_registration(username=username,phone=phone,age=age,gender=gender,location=location,email=email,image=image,password=password)
        registration.save()
        return render(request, 'userregistrationconfirmation.html')

    return render(request,'userreg.html')

def userregistrationconfirmation(request):
    return render(request,'userregistrationconfirmation.html')

#user info edit
def userregedit(request):
    return render(request,'userregedit.html')

def updateuser(request,id):
    upt = employer_registration.objects.get(id=id)
    return render(request,'userregedit.html',{'result':upt}) 

def useredt(request,id):
    if request.method=="POST":
        username=request.POST.get('username')
        phone=request.POST.get('phone')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        location=request.POST.get('location')
        email=request.POST.get('email')
        image=request.FILES['image']
        imgf=FileSystemStorage()
        imgfs=imgf.save(image.name,image)
        password=request.POST.get('password')
        usersave=employer_registration(username=username,phone=phone,age=age,gender=gender,location=location,email=email,image=image,password=password,id=id)
        usersave.save()

    return redirect(employerprofile)

#user delete
def userselfdelete(request,id):
    member = employer_registration.objects.get(id=id)
    member.delete()
    return redirect(userreg)

#worker registration
def workerreg(request):
    if request.method=="POST":
        workername=request.POST.get('workername')
        phone=request.POST.get('phone')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        occupation=request.POST.get('occupation')
        location=request.POST.get('location')
        email=request.POST.get('email')
        image=request.FILES['image']
        f=FileSystemStorage()
        fs=f.save(image.name,image)
        password=request.POST.get('password')
        registration=employee_registration(workername=workername,phone=phone,age=age,gender=gender,occupation=occupation,location=location,email=email,image=image,password=password)
        registration.save()
        return render(request, 'workerregistrationconfirmation.html')

    return render(request,'workerreg.html')

def workerregistrationconfirmation(request):
    return render(request,'workerregistrationconfirmation.html')

#worker info edit
def workerregedit(request):
    return render(request,'workerregedit.html')

def updateworker(request,id):
    upt = employee_registration.objects.get(id=id)
    return render(request,'workerregedit.html',{'result':upt}) 

def workeredt(request,id):
    if request.method=="POST":
        workername=request.POST.get('workername')
        phone=request.POST.get('phone')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        occupation=request.POST.get('occupation')
        location=request.POST.get('location')
        email=request.POST.get('email')
        image=request.FILES['image']
        imgf=FileSystemStorage()
        imgfs=imgf.save(image.name,image)
        password=request.POST.get('password')
        workersave=employee_registration(workername=workername,phone=phone,age=age,gender=gender,occupation=occupation,location=location,email=email,image=image,password=password,id=id)
        workersave.save()

    return redirect(workersprofile)

#worker delete
def workerselfdelete(request,id):
    member = employee_registration.objects.get(id=id)
    member.delete()
    return redirect(workerreg)

#login and logout
def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    if employer_registration.objects.filter(email=email,password=password).exists():
        employerdetls=employer_registration.objects.get(email=request.POST['email'], password=password)
        if employerdetls.password == request.POST['password']:
            request.session['uid'] = employerdetls.id
            request.session['uname'] = employerdetls.username

            request.session['phone'] = employerdetls.phone

            request.session['email'] = email

            request.session['employer'] = 'employer'

            return render(request,'index.html')
        
    elif employee_registration.objects.filter(email=email,password=password).exists():
        employeedetls=employee_registration.objects.get(email=request.POST['email'], password=password)
        if employeedetls.password == request.POST['password']:
            request.session['wid'] = employeedetls.id
            request.session['wname'] = employeedetls.workername

            request.session['phone'] = employeedetls.phone

            request.session['email'] = email

            request.session['employee'] = 'employee'

            return render(request,'index.html')

    else:
        return render(request, 'login.html', {'status': 'Invalid Username or Password'})
    
def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(index)

def workerslist(request):
    dict_pc={
        'pc': employee_registration.objects.all()
    }
    return render(request,'workerslist.html', dict_pc)

def workersprofile(request):
    tem=request.session['wid']
    vpro=employee_registration.objects.get(id=tem)
    return render(request,'workersprofile.html',{'result':vpro})

def employerprofile(request):
    tem=request.session['uid']
    vpro=employer_registration.objects.get(id=tem)
    return render(request,'employerprofile.html',{'result':vpro})

def occupationrequests(request):
    return render(request,'occupationrequest.html')

def occupationrequest(request,id):
    tem=request.session['uid']
    upt=employer_registration.objects.get(id=tem)
    vpro=employee_registration.objects.get(id=id)
    return render(request,'occupationrequest.html',{'result':upt,'res':vpro})
 
def occupationreq(request,id): 
    tem=request.session['uid']
    if request.method=="POST":
        # username=request.POST.get('username')
        # workername=request.POST.get('workername')
        employer_instance = employer_registration.objects.get(id=tem)
        employee_instance = employee_registration.objects.get(id=id)
        job_description=request.POST.get('job_description')
        job_location=request.POST.get('job_location')
        job_date=request.POST.get('job_date')
        jobsave=job(username=employer_instance,workername=employee_instance,job_description=job_description,job_location=job_location,job_date=job_date,job_review='pending',id=id)
        jobsave.save()
        # return render(workerslist)
    return render(request,'jobrequestconfirmation.html',{'success':'registered successfully'})

def jobrequestconfirmation(request):
    return render(request,'jobrequestconfirmation.html')

#jobs seen by workers
def occupationreqview(request):
    tem=request.session['wid']
    employee_instance = employee_registration.objects.get(id=tem)
    iusers=job.objects.filter(workername=employee_instance)
    return render(request,'occupationreqview.html',{'res':iusers})
    # return render(request,'occupationreqview.html')

#jobs request seen by users
def occupationreqemployerview(request):
    tem=request.session['uid']
    employer_instance = employer_registration.objects.get(id=tem)
    iusers=job.objects.filter(username=employer_instance)
    return render(request,'occupationreqemployerview.html',{'rest':iusers})

def deleterequest(request,id):
    employee_instance = employee_registration.objects.get(id=id)
    member = job.objects.get(workername=employee_instance)
    member.delete()
    return redirect(occupationreqview)

#worker replying to job request
def workeracknowledgements(request):
    return render(request,'workeracknowledgement.html')

def workeracknowledgement(request,id):
    tem=request.session['wid']
    upt=employee_registration.objects.get(id=tem)
    wusers=job.objects.get(id=id)
    return render(request,'workeracknowledgement.html',{'res':wusers,'result':upt})

def workeracknowledgementsave(request,id):
    tem=request.session['wid']
    if request.method=="POST":
        job_instance = job.objects.get(id=id)
        employer_instance = job_instance.username 
        employee_instance = employee_registration.objects.get(id=tem)  
        wphone=request.POST.get('wphone')
        ackmesg=request.POST.get('ackmesg')
        acknowledgementsave=acknowledgement(username=employer_instance,workername=employee_instance,wphone=wphone,ackmesg=ackmesg,id=id)
        acknowledgementsave.save() 
        return redirect(occupationreqview)
    
#user acknowledgement viewing section
def useracknowledgementview(request):
    tem=request.session['uid']
    employer_instance=employer_registration.objects.get(id=tem)
    acknowledgement_instance=acknowledgement.objects.filter(username=employer_instance)
    return render(request,'useracknowledgementview.html',{'acknowledgements': acknowledgement_instance})
    # return render(request,'useracknowledgementview.html',{'acknowledgements': acknowledgement_instance})

class acknowledgementview(TemplateView):  # Update YourParentClass with the actual parent class
    template_name='useracknowledgementview.html'
    # Your view code

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context
    

def paying(request): #optional
    return render(request,'paying.html')

def paymentsuccess(request):  #1st option payment
    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_SECRET_KEY 
        paymentsuccess = stripe.Charge.create(
            amount=500,
            currency='inr',
            description='Payment Gateway',
            source=request.POST['stripeToken']
        )
        return render(request,'paymentsuccess.html')

def paymentsuccesstwo(request): #optional
    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_SECRET_KEY 
        paymentsuccess = stripe.Charge.create(
            amount=1000,
            currency='inr',
            description='Payment Gateway',
            source=request.POST['stripeToken']
        )
        return render(request,'paymentsuccess.html')