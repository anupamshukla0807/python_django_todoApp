from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('add/', views.add_todo, name='add_todo'),
    path('view/<int:todo_id>/', views.view_todo, name='view_todo'), #url define view task
    path('edit/<int:todo_id>/', views.edit_todo, name='edit_todo'),  #url define  edit task
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),  # url  define delete task
    path('search/',views.search_todo,name='search_todo'),# url for search
    path('search-result/',views.search_todo,name='search-result')
    
]