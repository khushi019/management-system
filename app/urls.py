from django.urls import path
from app.views import *

urlpatterns=[
    path('reg/',view_reg,name='reg'),
    path('td/',view_td,name='td'),
    path('',view_index,name='index'),
    path('<id>/delete/',delete_view,name='delete'),
    path('<id>/update/',update_view,name='update'),
]