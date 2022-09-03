from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/shuttle/', include('shuttle.urls')),

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