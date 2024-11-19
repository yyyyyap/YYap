from django.urls import path
from . import views
urlpatterns=[
    path('foodhome',views.foodhome,name='foodhome'),
    path('<int:food_id>', views.fooddetail, name='fooddetail'),
    path('<int:food_id>/createfoodreview', views.createfoodreview, name='createfoodreview'),
    path('review/<int:review_id>', views.updatefoodreview, name='updatefoodreview'),
    path('review/<int:review_id>/delete', views.deletefoodreview, name='deletefoodreview'),
]