from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('client/<int:id>', views.clientView, name='client-view'),  
    path('createClient/', views.createClient, name='create-client'),
    path('editClient/<int:id>', views.editClient, name='edit_client'), 
    path('deleteClient/<int:id>', views.deleteClient, name='delete-client'),   
]    