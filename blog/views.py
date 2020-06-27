from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404, render
from .models import Post, Experience, Skill, Project, Involvement
from .forms import PostForm, ExperienceForm, SkillsForm, ProjectForm, InvolvementForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def bio_page(request):
    return render(request, 'blog/bio_page.html')

def cv_page(request):
    experiences = Experience.objects.order_by('published_date')
    skills = Skill.objects.order_by('level')
    projects = Project.objects.all()
    involvements = Involvement.objects.all()
    return render(request, 'blog/cv_page.html', {'experiences': experiences, 'skills': skills, 'projects': projects, 'involvements': involvements})

def experience_new(request):
    if request.method == "POST":
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.published_date = timezone.now()
            experience.save()
            return redirect('cv_page')
    else:
        form = ExperienceForm()
    return render(request, 'blog/experience_edit.html', {'form': form})

def experience_edit(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    if request.method == "POST":
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.save()
            return redirect('cv_page')
    else:
        form = ExperienceForm(instance=experience)
    return render(request, 'blog/experience_edit.html', {'form': form})

def skill_new(request):
    if request.method == "POST":
        form = SkillsForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.published_date = timezone.now()
            skill.save()
            return redirect('cv_page')
    else:
        form = SkillsForm()
    return render(request, 'blog/skill_edit.html', {'form': form})

def project_new(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect('cv_page')
    else:
        form = ProjectForm()
    return render(request, 'blog/project_edit.html', {'form': form})

def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect('cv_page')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'blog/project_edit.html', {'form': form})

def involvement_new(request):
    if request.method == "POST":
        form = InvolvementForm(request.POST)
        if form.is_valid():
            involvement = form.save(commit=False)
            involvement.save()
            return redirect('cv_page')
    else:
        form = InvolvementForm()
    return render(request, 'blog/involvement_edit.html', {'form': form})

def involvement_edit(request, pk):
    involvement = get_object_or_404(Involvement, pk=pk)
    if request.method == "POST":
        form = InvolvementForm(request.POST, instance=involvement)
        if form.is_valid():
            involvement = form.save(commit=False)
            involvement.save()
            return redirect('cv_page')
    else:
        form = InvolvementForm(instance=involvement)
    return render(request, 'blog/involvement_edit.html', {'form': form})