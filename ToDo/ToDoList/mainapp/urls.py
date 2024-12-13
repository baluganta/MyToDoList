from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CreateView.as_view(), name='todo-create'),
    path('list/', ListView.as_view(), name='todo-list'),
    path('<int:pk>/', DetailView.as_view(), name='todo-detail'),
    path('<int:pk>/update/', UpdateView.as_view(), name='todo-update'),
    path('<int:pk>/delete/', DeleteView.as_view(), name='todo-delete'),
]
