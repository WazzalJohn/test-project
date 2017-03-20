from django.conf.urls import url
from first_app import views

#This bit is for template tagging / URLs.
app_name = 'first_app'

urlpatterns = [
    #url(r'^sign_in/$', views.user_login, name='sign_in'),
    # Be careful setting the name to just /login use userlogin instead!
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^share_screen/$', views.share_screen, name='share_screen'),
    url(r'^test_simplepage/$', views.test_simplepage, name='test_simplepage'),
    # url(r'^settings/$', views.settings, name='settings'),
]
