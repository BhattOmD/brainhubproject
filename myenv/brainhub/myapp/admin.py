from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(user)
admin.site.register(adminuser)
admin.site.register(learners)
admin.site.register(category)
admin.site.register(course)
admin.site.register(company)
admin.site.register(enrollcourse)
