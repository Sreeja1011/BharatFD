from django.urls import path
from .views import FAQListView
from . import views 
from .views import add_faq 
urlpatterns = [
    path("faqs/", FAQListView.as_view(), name="faq-list"),
    path("add/", add_faq, name="add_faq"),
]
