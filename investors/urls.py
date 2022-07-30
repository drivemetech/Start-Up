from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home_Page'),
    path('feedback/', views.Feedback.as_view(), name='FeedBack'),
    path('Company<slug:slug>/', views.viewCompany, name='View_Company'),
    path('edit/<slug:slug>/', views.Edition.as_view(), name='Edit'),
    path('login', views.login, name='login'),
    path('sign-up/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='Dashboard'),
    path('ViewCompany/<slug:slug>/', views.viewForNonUser, name='Views'),
    path('Add/', views.AddCompany.as_view(), name='Add_Company'),
]