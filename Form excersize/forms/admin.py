from django.contrib import admin
from .models import Question, Choice, User1s, User2s, UserProfileInfo

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(User1s)
admin.site.register(User2s)
#code below is new
admin.site.register(UserProfileInfo)
