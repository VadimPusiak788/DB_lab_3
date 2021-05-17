from django.urls import path
from .views import NoteDetail, NoteUpdate, NoteDelete, CreateNote, FavoriteNote, CreateCategory

app_name = 'note'

urlpatterns = [
    path('detail/<int:pk>/', NoteDetail.as_view(), name='detail'),
    path('update/<int:pk>/', NoteUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', NoteDelete.as_view(), name='delete'),
    path('create/', CreateNote.as_view(), name='create'),
    path('favorite/', FavoriteNote.as_view(), name='favorite'),
    path('create_category/', CreateCategory.as_view(), name='create_category')
]