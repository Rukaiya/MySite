from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('',views.HomeView.as_view(), name="home"),
    path('lists/', views.MyListView.as_view(), name= "mylist"),

    path('createlist/', views.CreateList.as_view(), name = "create"),
    path('<int:pk>/deletelist/', views.DeleteList.as_view(), name = "delete"),
    path('updatelist/<int:pk>', views.UpdateList.as_view(), name = "update"),
    path('list_detail/<int:pk>', views.DetailList.as_view(), name="detail")
]
