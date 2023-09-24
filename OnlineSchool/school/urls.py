from django.urls import path
from . import views

urlpatterns = [
    path('ugtbp', views.user_get_tutorials_by_products),
    path('ugtbsp', views.user_get_tutorials_by_specific_product),
    path('gsbap', views.get_statistic_by_all_products),
    path('cu', views.create_user),
    path('cp', views.create_product),
    path('ct', views.create_tutorial),
    path('ugp', views.user_get_product),
    path('uwt', views.user_watch_tutorial),
]

