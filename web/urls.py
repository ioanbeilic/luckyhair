from django.urls import path
from .views import HomeView, AboutView, ServicesView, ArticlesView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('nosotrons', AboutView.as_view(), name='about'),
    path('servicios', ServicesView.as_view(), name='services'),
    path('articulos', ArticlesView.as_view(), name='articles'),
    path('contacto', ContactView.as_view(), name='contact')

]
