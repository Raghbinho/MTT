"""mysite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as views_django
from polls import views, forms
from MTT import settings
from polls.forms import LoginForm
import os
urlpatterns = [
    # url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    # url(r'^adm$', views.admin, name='admin'),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'', include('polls.urls')),
    url(r'^home/$', views.home),
    url(r'^success/$', views.register_success, ),
    url(r'^register/$', views.register, {'template_name': 'register.html'}),
    url(r'^login/$', views_django.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', views_django.logout, {'next_page': '/login'}),
    url(r'^list$', views.listtree, {'template_name': 'list.html'},),

    url(r'^addProduct$', views.addProduct, {'template_name': 'listProduct.html'},),
    url(r'^create$', views.create, {'template_name': 'list.html'}),
    url(r'^folder/$', views.getName, ),
    url(r'^folder1/$', views.getNameF, ),
    url(r'^foldertest/$', views.getNameTest, ),

    url(r'^editTestCase/$', views.editTestCase, ),
    # url(r'^listattribute/$', views.showAttributes, ),



    url(r'^getAttributes/$', views.getAttributes, ),


    url(r'^parseXML/$', views.parseXML, ),
    # url(r'^createTemporary/$', views.createTemporary, {'template_name': 'list.html'}),
    url(r'^generateXML/', views.generateXML, ),
    url(r'^generate$', views.generate),
    url(r'^generateMethod$', views.generateMethod),
    url(r'^generateProduct$', views.generateProduct,{'template_name': 'listProduct.html'}),
    url(r'^generateTest', views.generateTest, {'template_name': 'DictionnaryObject.html'}),
    url(r'^getXML$', views.getXML, {'template_name': 'DictionnaryObject.html'},),
    url(r'^editProduct$', views.editProduct, {'template_name': 'listProduct.html'}),
    url(r'^editTest$', views.editTest, {'template_name': 'listTestCases.html'}),
    url(r'^treeListF$', views.treeListF, {'template_name': 'listProduct.html'}, ),
    url(r'^TestCasesTree$', views.TestCasesTree, {'template_name': 'listTestCases.html'}, ),
    url(r'^update/$', views.update, ),
    url(r'^dmtt/$', views.dmtt),
    url(r'^productName/$', views.productName, ),
    url(r'^DMTTExecution/$', views.DMTTExecution, ),
    url(r'^Tc_Firmware$', views.Tc_Firmware,{'template_name': 'welcome.html'}),


]

