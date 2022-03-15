""" Users URLs. """

# Django
from django import views
from django.urls import path

# View
from user.views import Index, LoginRender_view, LoginView, SignupRender_view ,SignupView, LogoutView

urlpatterns = [
    
    # Index 
    path('index/', Index, name='index'),
    
    # Login Render
    path('index/login_render/', LoginRender_view, name='login_render'),
    
    # Login
    path('index/login/', LoginView, name='login'),
    
    # Signup render
    path('index/signup_render/', SignupRender_view, name='signup_render'),
    
    # Signup
    path('index/signup/', SignupView, name='signup'),
    
    path(route='logout/', view=LogoutView.as_view(), name='logout')

]

