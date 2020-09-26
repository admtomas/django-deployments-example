from django.urls import path
from . import views

#*TEMPLATE TAGGING, see how it is used in relative _url_template.html
app_name = 'forms'

urlpatterns = [
    #*   path would be /forms/ ...and it is default
    path('first/', views.index, name='first_index_page'),
    #*...path below would be /.../index
    path('index/', views.form_view, name='index_page'),
    #*...path here would be /.../form
    path('form/', views.form_name_view, name='form_page'),
    #*...path here would be /.../form
    #!excersisez
    path('users/', views.users, name='users_page'),
    path('users2/', views.users2, name='models_form'),
    path('templateurl/', views.template_url, name='template_urls'),
    path('other/', views.other, name='other'),
    path('relatives/', views.relatives, name='relative_page'),
    #!user models and forms excersizes
    path('user_page/', views.user_page_index, name='user_index'),
    path('user_register/', views.user_register, name='user_register'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('special/', views.special, name='special'),
    #!to be tested
]