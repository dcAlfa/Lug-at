
from django.contrib import admin
from django.urls import path


from H_va_X_APP.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lugat),
]
