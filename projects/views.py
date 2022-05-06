from django.shortcuts import render


from .forms import ProjectForm
from .models import ProjectImage, Tag, Project
from users.models import User

# Create your views here.


def get_projects(request):
    return render(request, 'projects/projects.html')


def get_project(request, project_id):
    project = Project.objects.get(id=project_id)
    user = User.objects.get(id=project.user.id)
    images = ProjectImage.objects.filter(project_id=project.id)
    num_of_Projects = user.project_set.count()

    print(project)
    print(user)
    for img in images:
        print(img)
    return render(request, 'projects/project.html', {'project': project, 'user': user, 'images': images, "num_of_Projects": num_of_Projects})


def create_project(request):
    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        # fetching Images
        images = request.FILES.getlist('images')
        # Adding New Tags
        retags = request.POST.getlist('tags[]')
        for tag in retags:
            if not Tag.objects.filter(name=tag).exists():
                Tag.objects.create(name=tag, is_verified=False)
        # Creating new Project
        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.user = request.user
            project.save()
            # saving tages
            for tag in retags:
                project.tags.add(Tag.objects.get(name=tag))
            project.save()
            # saving images
            for img in images:
                ProjectImage.objects.create(image=img, project=project)

    project_form = ProjectForm()
    verifiedTags = Tag.objects.filter(is_verified=True)
    context = {'project_form': project_form, 'tags': verifiedTags}

    return render(request, "projects/project_create.html", context)
