from django.urls import path
from tracer import views
urlpatterns = [
    path('', views.home, name='home'),
    path ('about/',views.about,name='about'),
    path ('contact/',views.contact,name='contact'),
    path('feature/',views.feature,name='feature'),
    path('price/',views.price,name='price'),
    path('services/',views.services,name='services'),
    path('quote/',views.quote,name='quote'),
    path('team/',views.team,name='team'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('four/',views.four,name='404'),
    path('sea/',views.sea,name='sea'),
    path('air/',views.air,name='air'),
    path('road/',views.road,name='road'),
    path('terms',views.terms,name='terms'),
    path('logistics/',views.logistics,name='logistics'),
    path('support/',views.support,name='support')


]