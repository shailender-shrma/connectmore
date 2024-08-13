from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.CurrentUserCreateListView.as_view(),
         name="home"),
    path('delete/<int:id>/', views.currentuser_delete,
         name="delete-current-user"),
    path('update/<int:id>/', views.CurrentUserUpdateApiView,
         name="current-user-update"),
    path('pdfs/', views.PDFCreateListView.as_view(),
         name="add-pdf"),
    path('delete-pdf/<int:id>/', views.delete_pdf,
         name="delete-pdf"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
