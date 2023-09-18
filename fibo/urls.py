from django.urls import path
from . import views

urlpatterns = [
    path('fib', views.FibView.as_view())
]
