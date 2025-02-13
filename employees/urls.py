from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('add/', views.add_employee, name='add_employee'),
    path('update/<int:employee_id>/', views.update_employee, name='update_employee'),
    path('delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),
]

