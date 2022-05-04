from django.urls import path, re_path
from .views import CreateCategory, ListCategory, EditCategory, DeleteCategory, ListProject, ListTag, verify_project, verify_tag


urlpatterns = [
    path('category/', CreateCategory.as_view(), name='create_category'),
    path('categories/', ListCategory.as_view(), name='list_category'),
    path('categories/<pk>', EditCategory.as_view(), name='edit_category'),
    path('categories/delete/<pk>', DeleteCategory.as_view(), name='delete_category'),
    path('project/', ListProject.as_view(), name='list_project'),
    path('verifyProject/<int:project_id>',
         verify_project, name='verify_project'),
    path('tag/', ListTag.as_view(), name='list_tags'),
    path('verifyTag/<int:id>',
         verify_tag, name='verify_tag'),
]
