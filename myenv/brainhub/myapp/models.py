from django.db import models

# Create your models here.

class user(models.Model):
    email=models.EmailField(max_length=30,unique=True)
    password=models.CharField(max_length=30)
    otp=models.IntegerField(default=456)
    role=models.CharField(max_length=30)
    created_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.email

class adminuser(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    user_name=models.CharField(max_length=30)
    contact_no=models.CharField(max_length=15)
    pic=models.FileField(upload_to="media/images/",default="media/admin.png")
    
    def __str__(self):
        return self.user_name+" ("+self.user_id.email+")"

class learners(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    user_name=models.CharField(max_length=30)
    contact_no=models.CharField(max_length=15)
    city=models.CharField(max_length=45,blank=True,null=True)
    gender=models.CharField(max_length=10,blank=True,null=True)
    qualification=models.CharField(max_length=30,blank=True,null=True)
    primary_language=models.CharField(max_length=(30),blank=True,null=True)
    status=models.BooleanField(default=False)
    pic=models.FileField(upload_to="media/images/",default="media/student.png")
    
    def save(self, *args, **kwargs):
        if not self.pic or self.pic == "media/student.png":  # Default image logic
            if self.gender == "female":
                self.pic = "media/studentgirl.png"
            else:  
                self.pic = "media/student.png"
        super().save(*args, **kwargs)  # Save to the database
    
    def __str__(self):
       return self.user_name+" ("+self.user_id.email+")"

class category(models.Model):
    user_id = models.ForeignKey(user,on_delete=models.CASCADE)
    category_name=models.CharField(max_length=30)
    category_pic=models.FileField(upload_to="media/images/",default="media/category.png")
    def __str__(self):
       return self.category_name

class course(models.Model):
       user_id=models.ForeignKey(user,on_delete=models.CASCADE)
       category_name=models.ForeignKey(category,on_delete=models.CASCADE)
       course_duration=models.CharField(max_length=30)
       course_name=models.CharField(max_length=30)
       fees=models.CharField(max_length=30)
       course_descriptions=models.TextField()
       course_lecture_flow=models.FileField(upload_to="media/lectureflow/")
       course_heandbook=models.FileField(upload_to="media/heandbook/")
       course_interview_qustion=models.FileField(upload_to="media/interviewpreperation/")
       course_assignment=models.FileField(upload_to="media/assignment/")
       course_pic=models.FileField(upload_to="media/images/",default="media/category.png")
       course_tutor_name=models.CharField(max_length=30)
       
       def __str__(self):
           return self.course_name
       
class company(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    company_name=models.CharField(max_length=50)
    company_logo=models.FileField(upload_to="media/image/",default="media/company")
    company_descriptions=models.TextField()
    company_email=models.CharField(max_length=20)
    company_phone_no=models.CharField(max_length=11) 
    company_website=models.CharField(max_length=50)
    company_address=models.CharField(max_length=100)     
    
    def __str__(self):
           return self.company_name
       
class enrollcourse(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    learner_id=models.ForeignKey(learners,on_delete=models.CASCADE)
    cour_id=models.ForeignKey(course,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=30,default="PENDING")
    fees_status=models.CharField(max_length=30)
    paid_fees=models.IntegerField(default=0)
    
    