from import path
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
]