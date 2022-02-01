from django.urls import path
from . import views
from .views import *

urlpatterns = [
	path('',views.search,name='search'),
	path('upload',ExportImportExcel.as_view()),
    ]