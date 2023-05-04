from django.urls import path
from . import views

urlpatterns = [
    # Diğer url kalıpları...
    path('<int:pk>/', views.book_detail, name='book_detail'),
    path("demo/", views.demo, name="demo"),
]



