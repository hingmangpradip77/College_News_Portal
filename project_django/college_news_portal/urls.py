# In college_news_portal/urls.py

from django.contrib import admin
from django.urls import path, include
# Make sure you've imported this:
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # This specific logout URL must come BEFORE the generic include.
    # This line forces the redirect after logout.
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    
    # This line provides all other auth URLs (login, password reset, etc.)
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Your other app URLs
    path('accounts/', include('users.urls')),
    path('', include('news.urls')),
]