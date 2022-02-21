from django.urls import path
from . import views

urlpatterns = [
	path('studentapi', views.student_api, name="index"),
	path('studentapi/<int:pk>/', views.student_api, name="index"),
	# path('post/<int:pk>', views.post_data, name="post"),
	# path('update/', views.update_data, name="update"),
	# path('delete/', views.delete_data, name="delete"),



]