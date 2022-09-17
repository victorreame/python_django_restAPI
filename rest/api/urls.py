from django.urls import path
from . import views

urlpatterns = [
    path('product/',views.getData),
    path('product/<int:pk>', views.item_detail),
    path('product/add/', views.postItem),
    path('product/update/<int:pk>', views.updateItem),
    path('product/delete/<int:pk>', views.deleteItem),
]
