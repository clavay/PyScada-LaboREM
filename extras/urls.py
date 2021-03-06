"""PyScadaServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

try:
    import pyscada.laborem
    urlpatterns += [
        url(r'^', include('pyscada.laborem.urls')),
    ]
except ImportError:
    pass

urlpatterns += [
    url(r'^', include('pyscada.hmi.urls')),
]

try:
    import django_cas_ng.views
    urlpatterns += [
        url(r'^accounts/CASlogin/$', django_cas_ng.views.LoginView.as_view(), name='cas_ng_login'),
        url(r'^accounts/logout$', django_cas_ng.views.LogoutView.as_view(), name='cas_ng_logout'),
        url(r'^accounts/callback$', django_cas_ng.views.CallbackView.as_view(), name='cas_ng_proxy_callback'),
    ]
except ImportError:
    pass
