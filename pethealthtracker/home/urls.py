from django.urls import path
from . import views


urlpatterns = [

    # landing/main home page:
    path('', views.index, name='home'),

    # features page:
    path('features/', views.features, name='features'),

    # how it works page:
    path('howitworks/', views.how_it_works, name='how_it_works'),

    # contact us page:
    path('contact/', views.contact, name='contact'),
    
    # register page:
    path('register/', views.register_view, name='register'),

    # login page:
    path("login/", views.login_view, name="login"),

    # logout page:
    path('logout/', views.logout_view, name='logout'),

]
