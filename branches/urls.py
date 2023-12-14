from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='obolon'),
    path('hub/', views.index, name='hub'),
    path('gagarina/', views.index, name='gagarina'),
    path('pechersk/', views.index, name='pechersk'),
    path('officenew/', views.index, name='officenew'),
    ]

urlpatterns += [
    path('routeros', views.index, name='routeros')
]

urlpatterns += [
    path('qa', views.qa, name='qa')
]
