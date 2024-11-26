from django.contrib import admin
from django.urls import path, include
from showcase_site.views import index, about, services, projects, team, testimonial, blog_grid, blog_detail, contact

urlpatterns = [
    path('', index, name="home"),
    path('about/', about, name="about"),
    path('services/', services, name="services"),
    path('projects/', projects, name="projects"),
    path('team/', team, name="team"),
    path('testimonial/', testimonial, name="testimonial"),
    path('blog/', blog_grid, name="blog"),
    path('detail/', blog_detail, name="detail"),
    path('contact/', contact, name="contact"),
]
