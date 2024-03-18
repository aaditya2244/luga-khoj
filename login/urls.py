from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),

    path('register/', views.register, name='registration'), 
    path('login/', views.user_login, name='login'),
    path('admin-dash/', views.admin_page, name='admin_page'), 
    path('user/', views.user_page, name='user_page'),
    path('add_product/', views.add_product, name='add_product'),
    path('view-products/', views.view_products, name='view_products'),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)