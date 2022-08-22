from django.urls import path

from . import views

urlpatterns = [
    path('product', views.ProductList.as_view()),
    path('product/<int:uid>/', views.ProductDetails.as_view()),
    path('category', views.CategoryList.as_view()),
    path('category/<int:uid>/', views.CategoryDetails.as_view()),
    path('manufacturer', views.ManufacturerList.as_view()),
    path('manufacturer/<int:uid>/', views.ManufacturerDetails.as_view()),
]