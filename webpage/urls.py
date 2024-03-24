from django.urls import path
from webpage import views


urlpatterns = [
    path('upload_file/', views.upload_file, name='upload'),
    path('check_table/<path:file_path>/', views.info_from_text, name='output'),
]
