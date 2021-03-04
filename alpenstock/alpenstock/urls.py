from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'AlpanStock'
admin.site.site_title = 'AlpenStock admin'
admin.site.site_url = 'http://127.0.0.1:8000/'
admin.site.index_title = 'AlpanStock World School'
admin.empty_value_display = '**Empty**'

urlpatterns = [
    path('main_admin/', admin.site.urls),
    path('admin/', include('admins.urls')),
    path('library/', include('library.urls')),
    path('', include('student.urls')),
    path('teacher/', include('teacher.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)