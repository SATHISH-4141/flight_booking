from booking import views
from django.urls import path

urlpatterns = [
    path('',views.home,name = 'home'),
    path('signpage/',views.signpage,name = 'signpage'),
    path('enroll/',views.enrollment,name = 'enroll'),
    path('signup/',views.signup,name = 'signup'),

]