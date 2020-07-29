from django.urls import path
from item import views

app_name = 'item'

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('item/create/', views.item_create, name='item_create'),
    path('item/<int:pk>/edit', views.item_edit, name='item_edit'),
    path('item/<int:pk>/delete', views.item_delete, name='item_delete'),

    path('account/',views.account_list, name='account_list'),
    path('account/<int:pk>/', views.account_detail, name='account_detail'),
    path('account/create/', views.account_create, name='account_create'),
    path('account/<int:pk>/edit', views.account_edit, name='account_edit'),
    path('account/<int:pk>/delete', views.item_delete, name='account_delete'),
]