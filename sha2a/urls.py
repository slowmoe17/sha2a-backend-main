from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Property.views import PropertyCreateView,PropertyListView,PropertyDetailView,FavoritesView

admin.site.site_header = "Sakeny Admin Panel"
admin.site.site_title = "Sakeny Admin Panel"
admin.site.index_title = "Sakeny Admin Panel"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("user/", include("users.urls")),
    path("property/", PropertyCreateView.as_view()),
    path("property/all/", PropertyListView.as_view()),
    path("property/<int:pk>/", PropertyDetailView.as_view()),
    path("favorites/", FavoritesView.as_view()),

]
urlpatterns += static(settings.STATIC_URL,
document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)









"""
create property >>> create with token not with id
add CRUD operations for property
get properties for user 
get favorite properties for user
get property by id


"""