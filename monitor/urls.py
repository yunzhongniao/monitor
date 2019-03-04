"""monitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .source import monitor
from .source import DefaultView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', DefaultView.index),
    path('monitor/', monitor.mon),
    path('view/process/<int:process_id>', DefaultView.process_view),
    path('mon/<int:internal>/<int:count>/process/<int:process_id>', monitor.mon_process),
    path('mon/<int:internal>/<int:count>', monitor.mon_sys),
    path('mon/processes', monitor.list_process),
]
