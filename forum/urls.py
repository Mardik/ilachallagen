from django.contrib import auth
from django.urls import path

from forum.models import Thread, Replie
from forum.views import ThreadListView,\
                        thread_detail_view, \
                        ThreadCreateView, \
                        ThreadUpdateView, \
                        ThreadDeleteView, \
                        ReplieDeleteView

urlpatterns = [
    path('', ThreadListView.as_view(), name='thread-list'),
    path('replie/<int:pk>/delete/', ReplieDeleteView.as_view(), name='replie-delete'),
    path('thread/<int:pk>/', thread_detail_view, name='thread-detail'),
    path('thread/add/', ThreadCreateView.as_view(), name='thread-add'),
    path('thread/<int:pk>/update/', ThreadUpdateView.as_view(), name='thread-update'),
    path('thread/<int:pk>/delete/', ThreadDeleteView.as_view(), name='thread-delete'),    
]