from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import random
from .utils import *
#Create view here 

# def homepage(request):
#     if "email" in request.session:
#         uid=user.objects.get(email = request.session['email'])
#         if uid.role == "admin":
#             aid=adminuser.objects.get(user_id=uid)
#             context={
#                 'uid': uid,
#                 'aid': aid
#             }
            
#             return render(request,"myapp/index.html",context)
#     else:
#         return render(request,"myapp/login.html")

def homepage(request):
    if "email" in request.session:  
        uid = user.objects.get(email=request.session['email'])  
        if uid.role == "admin":  
            aid=adminuser.objects.get(user_id=uid)  

            # Fetch counts
            category_count = category.objects.count()
            course_count = course.objects.count()
            company_count = company.objects.count()
            
            # Fetch the last 5 records
            last_5_categories = category.objects.all().order_by('-id')[:5]
            last_5_courses = course.objects.all().order_by('-id')[:5]
            last_5_companies = company.objects.all().order_by('-id')[:5]

            context = {
                'uid': uid,
                'aid': aid,
                'category_count': category_count,
                'course_count': course_count,
                'company_count': company_count,
                'last_5_categories': last_5_categories,
                'last_5_courses': last_5_courses,
                'last_5_companies': last_5_companies,
            }
            print(f"Categories: {category_count}, Courses: {course_count}, Companies: {company_count}")
            return render(request, "myapp/index.html", context)  
        else:  
            return render(request, "myapp/login.html")  
    return render(request, "myapp/login.html")
    
#def aboutpage(request):
 #   return HttpResponse("<h1> hello wellcome to about page<h1>")

def loginpage(request):
    if "email" in request.session:
        uid=user.objects.get(email = request.session['email'])
        if uid.role == "admin":
            aid=adminuser.objects.get(user_id=uid)
            
            # Fetch counts
            category_count = category.objects.count()
            course_count = course.objects.count()
            company_count = company.objects.count()
            
            # Fetch the last 5 records
            last_5_categories = category.objects.all().order_by('-id')[:5]
            last_5_courses = course.objects.all().order_by('-id')[:5]
            last_5_companies = company.objects.all().order_by('-id')[:5]
            context={
                'uid': uid,
                'aid': aid,
                'category_count': category_count,
                'course_count': course_count,
                'company_count': company_count,
                'last_5_categories': last_5_categories,
                'last_5_courses': last_5_courses,
                'last_5_companies': last_5_companies,
            }
            return render(request,"myapp/index.html",context)
    if request.POST:
        try:
            print("submit button press")
            email=request.POST["email"]
            password=request.POST['password']
            
            uid= user.objects.get(email = email)
            if uid.password==password:
                if uid.role=="admin":
                    aid=adminuser.objects.get(user_id=uid)
                    context={
                        'uid': uid,
                        'aid': aid,  
                    }
                    
                    # Store data in session
                    request.session['email']= email
                    return render(request,"myapp/index.html",context)
                else:
                    lid=learners.objects.get(user_id=uid)
                    
                    # Fetch counts
                    category_count = category.objects.count()
                    course_count = course.objects.count()
                    company_count = company.objects.count()
                    
                    # Fetch the last 5 records
                    last_5_categories = category.objects.all().order_by('-id')[:5]
                    last_5_courses = course.objects.all().order_by('-id')[:5]
                    last_5_companies = company.objects.all().order_by('-id')[:5]
                    context={
                        'uid': uid,
                        'lid': lid,
                        'category_count': category_count,
                        'course_count': course_count,
                        'company_count': company_count,
                        'last_5_categories': last_5_categories,
                        'last_5_courses': last_5_courses,
                        'last_5_companies': last_5_companies,
                    }
                    
                    request.session['email']=email
                    return render(request,"myapp/learner_index.html",context)
            else:
                context ={
                    'e_msg': "invalid Password"
                }
                return render(request,"myapp/login.html",context)
            #print("somthing -------------->",uid)
            #return render(request,"myapp/index.html")
        except Exception as e:
            print("=======>",e)
            context ={
                'e_msg' : "invalid email or pasword"
            }
            return render(request,"myapp/login.html",context)
    else:
        print("======>>>> only  page refersh  is here")
        return render(request,"myapp/login.html") 
def logoutpage(request):
    if "email" in request.session:
        del request.session['email']
        return render(request,"myapp/login.html")
    else:
      return render(request,"myapp/login.html")
    
def newlearner(request):
    if request.POST:
        username=request.POST['user_name']
        email=request.POST['email']
        contactno=request.POST['contact_no']
        gender = request.POST['gender']
        

        l1=['892dasd','897sc4','sd8934','ds84fd','sdf9asd','8sd3ds','sd8345']
        password=email[2:5]+random.choice(l1)+contactno[2:5]
        context={
            'password':password
        }
        sendmail("learner_login_Password","learner_passwordemail",email,context)
        
        uid=user.objects.create(email=email,password=password,role="Learner")
        if uid:
            lid=learners.objects.create(user_id=uid,user_name=username,contact_no=contactno,gender=gender)
            if lid:
                context ={
                    's_msg' : "Successfully Account created!! check your mail box",
                    'gender': gender
                }
            return render(request,"myapp/login.html",context)
        else:
            context ={
                    'e_msg' : "Somthing went to wrong"
                }
            return render(request,"myapp/newlearner.html",context)
    else:    
        return render(request,"myapp/newlearner.html")
def profile(request):
    if "email" in request.session:
        if request.POST:
            uid=user.objects.get(email = request.session['email'])
            if uid.role == "admin":
                aid=adminuser.objects.get(user_id=uid)
                
                aid.user_name=request.POST['user_name']
                aid.contact_no=request.POST['contact_no']
                
                if "pic" in request.FILES:
                    aid.pic=request.FILES["pic"]
                    aid.save()
                aid.save()    
                context={
                    'uid': uid,
                    'aid': aid
                }
                return render(request,"myapp/profile.html",context)
        else:
            uid=user.objects.get(email = request.session['email'])
            if uid.role == "admin":
                aid=adminuser.objects.get(user_id=uid)
                
                context={
                    'uid': uid,
                    'aid': aid,
                    
                }
                return render(request,"myapp/profile.html",context)
    else:
        return render(request,"myapp/login.html")  
    
def all_learners(request):
    if "email" in request.session:
        uid=user.objects.get(email = request.session['email'])
        learners_all=learners.objects.all()
        if uid.role == "admin":
            aid=adminuser.objects.get(user_id=uid)
            context={
                'uid': uid,
                'aid': aid,
                'learners_all' : learners_all
            }
            return render(request,"myapp/learners.html",context)
    else:
        return render(request,"myapp/loin.html")                    
     
def learner_profile(request):
    if "email" in request.session:
        if request.POST:
            uid=user.objects.get(email = request.session['email'])
            if uid.role == "Learner":
                lid=learners.objects.get(user_id=uid)
                
                lid.user_name=request.POST['user_name']
                lid.contact_no=request.POST['contact_no']
                
                if "pic" in request.FILES:
                    lid.pic=request.FILES["pic"]
                    lid.save()
                lid.save()    
                context={
                    'uid': uid,
                    'lid': lid
                }
                return render(request,"myapp/learner_profile.html",context)
        else:
            uid=user.objects.get(email = request.session['email'])
            if uid.role == "Learner":
                lid=learners.objects.get(user_id=uid)
                context={
                    'uid': uid,
                    'lid': lid,
                    
                }
                return render(request,"myapp/learner_profile.html",context)
    else:
        return render(request,"myapp/login.html")

def add_category(request):
    if "email" in request.session:
        if request.POST:
            uid=user.objects.get(email = request.session['email'])
            if uid.role == "admin":
                    aid=adminuser.objects.get(user_id=uid)
                    
                    if "category_pic" in request.FILES:
                        cid=category.objects.create(user_id=uid, category_name=request.POST['category_name'],category_pic=request.FILES['category_pic'])
                    else:
                        cid=category.objects.create(user_id=uid, category_name=request.POST['category_name'])
                    context={
                        'uid': uid,
                        'aid': aid,
                        's_msg': "Successfully category added !!"
                    }
                    return render(request,"myapp/add_category.html",context)
        else:
            uid=user.objects.get(email = request.session['email'])
            if uid.role == "admin":
                aid=adminuser.objects.get(user_id=uid)
                context={
                    'uid': uid,
                    'aid': aid,
                    
                }
                return render(request,"myapp/add_category.html",context)

def all_category(request):
    if "email" in request.session:
        uid=user.objects.get(email = request.session['email'])
        if uid.role == "admin":
            aid=adminuser.objects.get(user_id=uid)
            call=category.objects.all()
            context={
                'uid': uid,
                'aid': aid,
                'call':call,
            }
            return render(request,"myapp/all_category.html",context)

def edit_category(request,pk):
    if "email" in request.session:
       uid=user.objects.get(email = request.session['email'])
       if uid.role == "admin":
            aid=adminuser.objects.get(user_id=uid)
            cid=category.objects.get(id=pk)
            context={
                'uid': uid,
                'aid': aid,
                'cid': cid,
            }
            return render(request,"myapp/edit_category.html",context)  
def update_category(request):
    if "email" in request.session:
       uid=user.objects.get(email = request.session['email'])
       if uid.role == "admin":
            aid=adminuser.objects.get(user_id=uid)
            category_id=request.POST['categoryid']
            cid=category.objects.get(id=category_id)
            
            cid.category_name=request.POST['category_name']
            cid.save()
            
            if "category_pic" in request.FILES:
                cid.category_pic=request.FILES['category_pic']
                cid.save()
            cid.save()
            call=category.objects.all()
            context={
                'uid': uid,
                'aid': aid,
                'call':call
            }
            return render(request,"myapp/all_category.html",context)  
def del_category(request,pk):
    if "email" in request.session:
       uid=user.objects.get(email = request.session['email'])
       if uid.role == "admin":
            aid=adminuser.objects.get(user_id=uid)
            cid=category.objects.get(id=pk)

            cid.delete()

            call=category.objects.all()
            context={
                'uid': uid,
                'aid': aid, 
                'call':call
            }
            return render(request,"myapp/all_category.html",context)

def add_course(request):
    if "email" in request.session:
        uid=user.objects.get(email = request.session['email'])
        if request.POST:
            print("---------->>>>> submit button presssed ")
            if uid.role == "admin":
                aid=adminuser.objects.get(user_id = uid)
                call=category.objects.all()
                lid=learners.objects.all()              
                category_name=request.POST['category']
                cid=category.objects.get(category_name=category_name)
                print("-----------------cid",cid)
                
                course_lecture_flow = request.FILES["course_lecture_flow"]
                
                course_id =course.objects.create(   user_id = uid,
                                                    category_name = cid,
                                                    course_name=request.POST['course_name'],
                                                    course_duration=request.POST['course_duration'],
                                                    fees=request.POST['fees'], 
                                                    course_descriptions=request.POST['course_descriptions'],
                                                    course_lecture_flow=course_lecture_flow,
                                                    course_heandbook=request.FILES['course_heandbook'],
                                                    course_interview_qustion=request.FILES['course_interview_qustion'],
                                                    course_assignment=request.FILES['course_assignment'],
                                                    course_pic=request.FILES['course_pic'], 
                                                    course_tutor_name=request.POST['course_tutor_name'],
                                                )
                if course_id:
                    s_msg="Succesfully Course Ditails add !!!!"
                                 
                    context={
                        'uid': uid,
                        'aid': aid, 
                        'call': call,
                        'lid': lid,
                        's_msg' : s_msg
                    }
                    
                    l_ed=learners.objects.values_list('user_id__email', flat=True)
                    c_name=course_id.course_name
                    context={
                        'c_name':c_name
                    }
                    for i in l_ed:
                        sendmail("new course added","new_courseadd",i,context)
                    
                    return render(request,"myapp/add_course.html",context)
                else:
                    e_msg="Somthing want to wrong !!"
                    context={
                        'uid': uid,
                        'aid': aid, 
                        'call': call,
                        'e_msg' : e_msg
                    }
                    return render(request,"myapp/add_course.html",context)
        else:  
            if uid.role == "admin":            
                aid=adminuser.objects.get(user_id = uid)
                call=category.objects.all()
                context={
                    'uid': uid,
                    'aid': aid, 
                    'call': call,
                }
                return render(request,"myapp/add_course.html",context)

def add_company(request):
    if "email" in request.session:
        uid=user.objects.get(email = request.session['email'])
        if request.POST:
            if uid.role == "admin":
                aid=adminuser.objects.get(user_id = uid)
                company_logo=request.FILES["company_logo"]
                # if request.FILES['company_logo']:
            cpid=company.objects.create(
                user_id=uid,
                company_name=request.POST['company_name'],
                company_email=request.POST['company_email'],
                company_phone_no=request.POST['company_phone_no'],
                company_address=request.POST['company_address'],
                company_website=request.POST['company_website'],
                company_logo=company_logo,
                company_descriptions=request.POST['company_descriptions'],
            )
            if cpid:
                s_msg="Succesfully Company added !!!!"
                context={
                    'uid':uid,
                    'aid':aid,
                    's_msg':s_msg
                }
                return render(request,"myapp/index.html",context)
            else:
                e_msg="Somthing want to wrong !!"
                context={
                    'uid':uid,
                    'aid':aid,
                    'e_msg':e_msg
                }
                return render(request,"myapp/add_company.html",context)
        else:
            uid=user.objects.get(email = request.session['email'])
            if uid.role == "admin":
                aid=adminuser.objects.get(user_id = uid)
                context={
                    'uid':uid,
                    'aid':aid
                }
                return render(request,"myapp/add_company.html",context)

def all_course_list(request):
     if "email" in request.session:
       uid=user.objects.get(email = request.session['email'])
       if uid.role == "admin":
            aid=adminuser.objects.get(user_id=uid)
            call=course.objects.all()
            context={
                'uid': uid,
                'aid': aid, 
                'call':call
            }
            return render(request,"myapp/all_course_list.html",context)

def all_company_list(request):
    if "email" in request.session:
       uid=user.objects.get(email = request.session['email'])
       if uid.role == "admin":
            aid=adminuser.objects.get(user_id=uid)
            company_all=company.objects.all()
            context={
                'uid': uid,
                'aid': aid, 
                'company_all':company_all
            }
            return render(request,"myapp/all_company_list.html",context)

def view_company(request):
    if "email" in request.session:
        if request.POST:
            uid=user.objects.get(email = request.session['email'])
            if uid.role == "Learner":   
                lid=learners.objects.get(user_id=uid)
                cpid=company.objects.all()
                context={
                 'uid': uid,
                 'lid': lid,
                 'cpid':cpid
                }
            return render(request,"myapp/view_company.html",context)
        else:
            uid=user.objects.get(email = request.session['email'])
            if uid.role == "Learner":
                lid=learners.objects.get(user_id=uid)
                cpid=company.objects.all()
                context={
                    'uid':uid,
                    'lid':lid,
                    'cpid':cpid
                }
                return render(request,"myapp/view_company.html",context)
def edit_course(request,pk):
    if "email" in request.session:
       uid=user.objects.get(email = request.session['email'])
       if uid.role == "admin":
            aid=adminuser.objects.get(user_id=uid)
            call=category.objects.all()
            course_id=course.objects.get(id=pk)
            context={
                'uid': uid,
                'aid': aid,
                'call': call,
                'course_id': course_id  
            }
            return render(request,"myapp/edit_course.html",context)

def update_course(request):
    if "email" in request.session:
        uid=user.objects.get(email = request.session['email'])
        call=category.objects.all()
        if uid.role == "admin":
            aid=adminuser.objects.get(user_id=uid)
            eid=request.POST['courseid']
            course_id=course.objects.get(id=eid)

            course_id.course_name=request.POST['course_name']
            print("-------> coursename",course_id.course_name)
                        
            course_id.course_duration=request.POST['course_duration']
            print("-------> course durations",course_id.course_duration)
            
            course_id.fees=request.POST['fees']
            print("-------> course fees",course_id.fees)
            
            course_id.course_descriptions=request.POST['course_descriptions']
            print("-------> course descriptions",course_id.course_descriptions)
            
            course_id.course_tutor_name=request.POST['course_tutor_name']
            print("-------> cours tutor name",course_id.course_tutor_name)
            
            if "course_lecture_flow" in request.FILES:
                course_id.course_pic=request.FILES['course_lecture_flow']
                course_id.save()
            course_id.save()
            
            if "course_heandbook" in request.FILES:
                course_id.course_heandbook=request.FILES['course_heandbook']
                course_id.save()
            course_id.save()
            
            
            if "course_interview_qustion" in request.FILES:
                course_id.course_pic=request.FILES['course_interview_qustion']
                course_id.save()
            course_id.save()
            
            
            
            if "course_assignment" in request.FILES:
                course_id.course_pic=request.FILES['course_assignment']
                course_id.save()
            course_id.save()
            
            
            if "course_pic" in request.FILES:
                course_id.course_pic=request.FILES['course_pic']
                course_id.save()
            course_id.save()
            
            if course_id:
                s_msg="Succesfully Course Ditails add !!!!"
                                
                context={
                    'uid': uid,
                    'aid': aid, 
                    'eid':eid,
                    'course_id':course_id,
                    's_msg' : s_msg
                }
                return render(request,"myapp/all_course_list.html",context)
            else:
                    e_msg="Somthing want to wrong !!"
                    context={
                        'uid': uid,
                        'aid': aid, 
                        'eid':eid,
                        'course_id':course_id,
                        'e_msg' : e_msg
                    }
                    return render(request,"myapp/all_course_list.html",context)
    
def del_course(request,pk):
    if "email" in request.session:
       uid=user.objects.get(email = request.session['email'])
       if uid.role == "admin":
            aid=adminuser.objects.get(user_id=uid)
            
            course_id=course.objects.get(id = pk)

            course_id.delete()

            call=category.objects.all()
            context={
                'uid': uid,
                'aid': aid, 
                'call':call,
                'course_id':course_id
            }
            return render(request,"myapp/all_course_list.html",context)
        
def edit_company(request,pk):
     if "email" in request.session:
       uid=user.objects.get(email = request.session['email'])
       if uid.role == "admin":
            aid=adminuser.objects.get(user_id=uid)
            cpid=company.objects.get(id=pk)
            context={
                'uid': uid,
                'aid': aid, 
                'cpid':cpid
            }
            return render(request,"myapp/edit_company.html",context)
        
def update_company(request):
     if "email" in request.session:
       uid=user.objects.get(email = request.session['email'])
       if uid.role == "admin":
            aid=adminuser.objects.get(user_id=uid)
            c_id=request.POST['companyid']
            cpid=company.objects.get(id=c_id)
            
            cpid.company_name=request.POST['company_name']
            cpid.company_descriptions=request.POST['company_descriptions']
            cpid.company_email=request.POST['company_email']
            cpid.company_phone_no=request.POST['company_phone_no']
            cpid.company_website=request.POST['company_website']
            cpid.company_address=request.POST['company_address']
            cpid.save()
            
            if "company_logo" in request.FILES:
                cpid.company_logo=request.FILES['company_logo']
                cpid.save()
            cpid.save()
            
            context={
                'uid': uid,
                'aid': aid, 
                'cpid':cpid
            }
            return render(request,"myapp/all_company_list.html",context)
        
        
    
def del_company(request,pk):
    if "email" in request.session:
       uid=user.objects.get(email = request.session['email'])
       if uid.role == "admin":
            aid=adminuser.objects.get(user_id=uid)
            cpid=company.objects.get(id=pk)

            cpid.delete()

            
            context={
                'uid': uid,
                'aid': aid, 
                'cpid':cpid
            }
            return render(request,"myapp/all_company_list.html",context)

def view_course(request):
    if "email" in request.session:
        if request.POST:
            uid=user.objects.get(email = request.session['email'])
            if uid.role == "Learner":   
                lid=learners.objects.get(user_id=uid)
                course_id=course.objects.all()
                context={
                 'uid': uid,
                 'lid': lid,
                 'course_id':course_id
                }
            return render(request,"myapp/view_course.html",context)
        else:
            uid=user.objects.get(email = request.session['email'])
            if uid.role == "Learner":
                lid=learners.objects.get(user_id=uid)
                course_id=course.objects.all()
                context={
                    'uid':uid,
                    'lid':lid,
                    'course_id':course_id
                }
                return render(request,"myapp/view_course.html",context)
            
def course_enroll(request,pk):
     if "email" in request.session:
       uid=user.objects.get(email = request.session['email'])
       if uid.role == "Learner":
            lid=learners.objects.get(user_id=uid)
            call=category.objects.all()
            course_id=course.objects.get(id=pk)
            context={
                'uid': uid,
                'lid': lid,
                'call': call,
                'course_id': course_id  
            }
            return render(request,"myapp/course_enroll.html",context)

def add_enroll_course(request,pk):
    if "email" in request.session:
       uid=user.objects.get(email = request.session['email'])
       if uid.role == "Learner":
        lid=learners.objects.get(user_id=uid)
        id=course.objects.get(id=pk)
        print("--------------------->pk=",pk)
        e_id=enrollcourse.objects.create(user_id=uid,
                                            learner_id=lid,
                                            cour_id=id,
                                            fees_status="PANDING"
                                        )
        if e_id:
            s_msg="Enrollment request send please wait!"
            context={
                'uid': uid,
                'lid': lid,
            }
            return render(request,"myapp/view_company.html",context)
        
def forgot_password(request):
    if request.POST:
        email =request.POST['email']
        try:
            uid =user.objects.get(email=email)
            if uid:
                
                otp = random.randint(1111,9999)
                uid.otp= otp
                uid.save()  
                context={
                    'otp':otp
                }
                sendmail("forgot_password","mail_template",email,context )
                context={
                    'email': email
                }
                return render(request,"myapp/reset_password.html",context)
        except:
            context={
                'e_msg':"invalid email address!"
            }
            return render(request,"myapp/forgot_password.html",context)
    else:
        return render(request,"myapp/forgot_password.html")
        
  
  
def reset_password(request):
    if request.POST:
        email=request.POST['email']
        uid=user.objects.get(email = email)
        otp=request.POST['otp']
        newpassword=request.POST['newpassword']
        conformpassword=request.POST['conformpassword']
        if str(uid.otp)==otp:
            if newpassword==conformpassword:
                uid.password=newpassword
                uid.save()
                s_msg="Successfully Password Reset !"
                context={
                    's_msg':s_msg
                }
                return render(request,"myapp/login.html",context)
            else:
                context={
                    'e_msg':"invalid otp",
                    'email': email
                }
                return render(request,"myapp/reset_password.html",context)
                
                 
  
  
 #===================================== All Request ===================================================================================       
def all_request(request):
    if "email" in request.session:
       uid=user.objects.get(email = request.session['email'])
       if uid.role == "admin":
            aid=adminuser.objects.get(user_id=uid)
            lid=learners.objects.all()
            e_id=enrollcourse.objects.all()
            course_id=course.objects.all()
            

            # all={
            #         'courseid':course_id,
            #         'learnername':[learners.user_name for learners in lid],
            #         'coursename':[course.course_name for course in course_id],
            #         'fees': [enrollcourse.fees_status for enrollcourse in e_id], 
            #     }
            
            all_data = {
                
                    1 : {
                        "name" : "anjli",
                    },    
                
                    2 : {
                        "name" : "Om",
                    },
            
            }
            
            
            
             # lid_data=list(learners.objects.values('user_name'))
            # course_data=list(course.objects.values('course_name'))
            # fees=list(enrollcourse.objects.values('fees_status'))
                
                
            context={
                'uid':uid,
                'aid':aid,
                'lid':lid,
                'e_id':e_id,
                'all_data':all_data,
                'course_id':course_id
            }    
            return render(request,"myapp/all_request.html",context)


def accept_request(request,pk):
   if "email" in request.session:
        uid=user.objects.get(email=request.session['email'])
        if uid.role == "admin":
            aid=adminuser.objects.get(user_id=uid)
            eid=enrollcourse.objects.get(id=pk)
            
            learner_name=eid.learner_id.user_name
            course=eid.cour_id.course_name
            learner_email=eid.learner_id.user_id.email
            eid.status="Accepted"
            eid.save()
            context={
                'e_msg':"your request is Accept ",
                'l_e' : learner_email,
                'learner_name':learner_name,
                'course':course
            }
            print("==========================> email",learner_email)
            print("========================>COURSE",course)
            sendmail("Conformation","new_courseadd copy",learner_email,context)

            context={
                'aid':aid,
                'eid':eid
            }
            return render(request,"myapp/all_request.html",context)
        
def reject_request(request,pk):
   if "email" in request.session:
        uid=user.objects.get(email=request.session['email'])
        if uid.role == "admin":
            aid=adminuser.objects.get(user_id=uid)
            eid=enrollcourse.objects.get(id=pk)
            
            learner_name=eid.learner_id.user_name
            course=eid.cour_id.course_name
            learner_email=eid.learner_id.user_id.email
            eid.status="Rejected"
            eid.save()
            context={
                'e_msg':"your request is Accept ",
                'l_e' : learner_email,
                'learner_name':learner_name,
                'course':course
            }
            print("==========================> email",learner_email)
            print("========================>COURSE",course)
            sendmail("Conformation","new_courseadd copy",learner_email,context)

            context={
                'aid':aid,
                'eid':eid
            }
            return render(request,"myapp/all_request.html",context)
            