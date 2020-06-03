from django.conf.urls import url,include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name='index'),
    url(r'^profile/(?P<user_id>(\d+))',views.profile,name='profile'),
    url('success',views.success, name = 'success'), 
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^new/image$',views.new_image,name='new_image'),
    url(r'^search/',views.searchuser ,name='searchuser'),
    url(r'^new/comment/(?P<images_id>(\d+))',views.new_comment,name='new_comment'),
    url(r'^follow/',views.usersimages,name='usersimages'),
    url(r'^comments/',views.index,name='comments'),
    url(r'^userprofile/(?P<user_id>(\d+))',views.userspublicprofile,name='userspublicprofile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)