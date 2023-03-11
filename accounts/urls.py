from django.urls import path

from accounts import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customer/<str:pk>', views.customers, name="customer"),

    path('create_order/', views.create_order, name="create-order"),
    path('update_order/<str:pk>', views.update_order, name="update-order"),
    path('delete_order/<str:pk>', views.delete_order, name="delete-order"),

    path('user_login/', views.user_login, name="login"),
    path('user_logout/', views.user_logout, name="logout"),
    path('user_register/', views.user_register, name="register"),

]
