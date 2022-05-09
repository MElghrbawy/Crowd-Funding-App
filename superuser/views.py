from pyexpat import model
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from projects.models import Category, CommentReport, Donation, Project, Tag, ProjectReport
from re import template

from users.models import User

# Create your views here.


class CreateCategory(CreateView):
    model = Category
    template_name = 'superuser/create_category.html'
    fields = "__all__"
    success_url = reverse_lazy('list_category')


class ListCategory(ListView):
    model = Category
    context_object_name = 'Categories'
    template_name = 'superuser/list_category.html'


class EditCategory(UpdateView):
    model = Category
    template_name = 'superuser/create_category.html'
    queryset = Category.objects.all()
    fields = "__all__"
    success_url = reverse_lazy('list_category')


class DeleteCategory(DeleteView):
    model = Category
    pk_ur_kwargs = 'category.id'
    template_name = 'superuser/delete_category.html'
    success_url = reverse_lazy('list_category')


class ListProject(ListView):
    model = Project
    context_object_name = 'projects'
    queryset = Project.objects.select_related('category', 'user')
    template_name = 'superuser/list_projects.html'


def verify_project(req, project_id):
    Project.objects.filter(id=project_id).update(is_verified=True)
    return redirect(reverse('list_project'))


class ListTag(ListView):
    model = Tag
    context_object_name = 'tags'
    queryset = Tag.objects.select_related('project')
    template_name = 'superuser/list_tags.html'


def verify_tag(req, id):
    Tag.objects.filter(id=id).update(is_verified=True)
    return redirect(reverse('list_tags'))


class DeleteProject(DeleteView):
    model = Project
    pk_ur_kwargs = 'project.id'
    template_name = 'superuser/delete_category.html'
    success_url = reverse_lazy('list_project')

class ListUser(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'superuser/list_users.html'

class DeleteUser(DeleteView):
    model = User
    pk_ur_kwargs = 'user.id'
    template_name = 'superuser/delete_category.html'
    success_url = reverse_lazy('list_users')        

class ListProjectsReport(ListView):
    model = ProjectReport
    context_object_name = 'reports'
    template_name = 'superuser/list_reports.html'

class ListProjectsCommentReport(ListView):
    model=CommentReport
    context_object_name = 'commentReports'
    template_name = 'superuser/list_comment_reports.html'

class ListProjectsDonations(ListView):
    model=Donation
    context_object_name = 'donations'
    template_name = 'superuser/list_donations.html'

   
