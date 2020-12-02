from django.urls import path

from .views import *


urlpatterns = [
    path('', upload_db, name='home'),
    path('get_database', get_db, name='get_list_db'),
    path('get_database/<int:db_id>/', read_data, name='read_data'),
]

