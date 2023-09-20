from django.shortcuts import render,HttpResponse,redirect
from .models import my_resume
from .form import myform ,register_form
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout


# # Create your views here.


# def myform(request):
#     if request.method=="POST":
#         name = request.POST['name']
#         linkedin_id=request.POST['linkdinid'] 
#         github_id = request.POST['githubid']
#         Email = request.POST['Email'] 
#         image  = request.POST['image'] 
#         skills = request.POST['skills']
#         address = request.POST['address']
#         mobile_no = request.POST['mobile_no']
#         years_degree=request.POST[' years_degree']
#         name_degree=request.POST['name_degree']
#         university_name=request.POST['university_name']
#         year12th=request.POST['year12th']
#         class_name12th=request.POST['class_name12th']
#         school_name12th=request.POST['school_name12th']
#         year10th=request.POST['year10th']
#         class_name10th=request.POST['class_name10th']
#         school_name10th=request.POST['school_name10th']
#         language_1=request.POST['language_1']
#         percentage_1=request.POST['percentage_1']
#         language_2=request.POST['language_2']
#         percentage_2=request.POST['percentage_2']
#         para_1=request.POST['para_1']
#         para_2=request.POST[' para_2']
#         working_years=request.POST[' working_years']
#         company_name=request.POST['company_name']
#         designation1=request.POST['designation1']
#         designation2=request.POST['designation2']
#         about=request.POST['about']
#         skill_1=request.POST['skill_1']
#         percent_1=request.POST['percent_1']
#         skill_2=request.POST[ 'skill_2']
#         percent_2=request.POST['percent_2']
#         skill_3=request.POST['skill_3']
#         percent_3=request.POST['percent_3']
#         skill_4=request.POST['skill_4']
#         percent_4=request.POST['percent_4']
#         skill_5=request.POST['skill_5']
#         percent_5=request.POST[' percent_5']
#         # skill_6=request.POST['skill_6']
#         # percent_6=request.POST['percent_6']
#         interest_1=request.POST['interest_1']
#         interest_2=request.POST['interest_2']
#         interest_3=request.POST['interest_3']
#         interest_4=request.POST['interest_4']
#         my_resume(name=name,Emrequestil=Email,image=image,interest_1=interest_1,interest_2=interest_2,interest_3=interest_3,about=about,percent_5=percent_5,percent_4=percent_4,percent_3=percent_3,percent_2=percent_2,percent_1=percent_1,skill_1=skill_1,skill_5=skill_5,skill_2=skill_2,skill_3=skill_3,skill_4=skill_4,company_name=company_name,designation1=designation1,designation2=designation2,para_2=para_2, working_years= working_years,percentage_2=percentage_2,para_1=para_1,language_2=language_2,address=address,language_1=language_1, percentage_1=percentage_1,year10th=year10th,school_name10th=school_name10th,class_name10th=class_name10th,class_name12th=class_name12th, school_name12th= school_name12th,year12th=year12th,skills=skills,mobile_no=mobile_no,university_name=university_name, years_degree= years_degree,name_degree= name_degree,linkedin_id=linkedin_id,github_id=github_id).save()
       
#     return render(request,'index.html')
def myforms(request):
    if request.method=="POST":
       a=myform(request.POST,request.FILES)
       print(a)
       if a.is_valid():
           a.save()
           return redirect('/get/')
    a=myform()
    context={
     'a':a
          }
    return render (request,'forms.html',context)

# def myresume(request):
#     data=my_resume.objects.all()
#     context={
#         'data':data

#     }
#     return render(request,'index.html',context)
             #x.saved()
            # return HttpResponse('data saved!!')
def get_data(request):
    data= my_resume.objects.filter(user=request.user)
    skill = []
    skill_per = []
    interest = []
    language = []
    
    for i in data[0].skill_1.split(','):
      skill.append(i)
      
    print(skill)
    
    for i in data[0].percent_1.split(','):
      skill_per.append(i)
      
     
    for i in data[0].interest_1.split(','):
      interest.append(i)
    
         
    for i in data[0].language_1.split(','):
      language.append(i)
      
    print(skill_per)
    
    context = {
      
       'data':data,
       'skill':skill,
       'skill_per':skill_per,
       'interest':interest,
       'language':language
    }

    return render(request,'resume.html',context)    


def create_account(request):
    if request.method == "POST":
        x=register_form(request.POST)
        if x.is_valid():
            x.saved()
            return HttpResponse('data saved!!')
    x=register_form()
    my_dict={
        'x':x
    }
    return render(request,'auth.html',my_dict)


def login_form(request):
    if request.method=="POST":
        x=AuthenticationForm(data = request.POST)
        print('>>>>x',x)
        if x.is_valid():
            uname=x.cleaned_data['username']
            paswd=x.cleaned_data['password']
            user=authenticate(username=uname,password=paswd)
            # print(user)
            
            if user is not None:
                login (request,user)
                #return HttpResponse('you are login')
                # return redirect('get/')
                return redirect('/myform/')
            
            
    x=AuthenticationForm()
    contact={
        'x':x
    }
    return render(request,'login.html',contact)

def get_out(request):
    logout(request)
    return redirect('/login/')




def creat_account(request):
    if request.method == "POST":
            uname = request.POST.get('username')
            email = request.POST.get('email')
            passw = request.POST.get('password')
            print(uname,email,passw)

            if User.objects.filter(username=uname).first():
                messages.success(request,'username is taken')

            if User.objects.filter(email=email).first():
                messages.success(request,'email is taken')
            
            else:
                user = User(username=uname,email=email)
                user.set_password(passw)
                user.save()
                messages.success(request,'Account created !!')
            
    return render(request, 'create_account.html')

def login_handle(request):
    
     if request.method == "POST":
            username = request.POST.get('username')
            password =request.POST.get('password')
            print(username,password)
           
            if not username or not password:
                messages.success(request,'Boths fields are required !')

            user_obj = User.objects.filter(username=username).first()
            user = authenticate(username=username,password=password)
            if user_obj is None:
                messages.success(request,'User Not found !')
            print(user_obj)

            if user is not None:
                login(request,user)
                return redirect('/')
            
            if user is None:
                messages.success(request,'Wrong Password !!')


     return render (request ,'login_account.html')
    
        
            
            
             
            
    











