from django.urls import path
from . import views

app_name = 'basic_app'
urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'), 
    path('create/', views.SchoolCreateView.as_view(), name='create'),
    path('<str:pk>', views.SchoolDetailView.as_view(), name='detail'), 
    path('update/<str:pk>', views.SchoolUpdateView.as_view(), name='update'), 
    path('delete/<str:pk>', views.SchoolDeleteView.as_view(), name="delete")
]
