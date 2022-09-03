from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home,name="home"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.details,name="details")
]
