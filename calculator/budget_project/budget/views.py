from django.shortcuts import render, redirect, get_object_or_404
from .models import budget
from .forms import ProjectDetails
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def cost_estimate(request):
    if request.method == 'POST':
        project_name = request.POST['project_name']
        time_of_completion = int(request.POST['time_of_completion'])
        require_hosting = request.POST.get('include_hosting', False)
        project_use = request.POST['project_use']
        require_it_maintenance = request.POST.get('require_it_maintenance', False)

        require_hosting = True if require_hosting == 'on' else False 

        require_it_maintenance = True if require_it_maintenance == 'on' else False 

        budgets = budget(
            project_name = project_name,
            time_of_completion = time_of_completion,
            require_hosting = require_hosting,
            project_use = project_use,
            require_it_maintenance = require_it_maintenance
        ) 
        estimated_cost = budgets.calculate_cost()

        budgets.save()

        return render (request, 'home.html', {'estimated_cost': estimated_cost})
    return render (request, 'home.html')

@login_required
def project_list(request):
    projects = budget.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

@login_required
def project_add(request):
    if request.method == 'POST':
        form = ProjectDetails(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect ('project_list')
    else:
        form = ProjectDetails()
    return render(request, 'projectform.html', {'form': form})

@login_required
def project_details(request, pk):
    project = get_object_or_404 (budget, pk=pk)
    estimated_cost = project.calculate_cost()
    return render (request, 'project_details.html', {'project': project, 'estimated_cost': estimated_cost})

@login_required
def project_edit(request, pk):
    project = get_object_or_404 (budget, pk=pk)
    if request.method == 'POST':
        form = ProjectDetails(request.POST, instance=project)
        if form.is_valid():
            project = form.save(commit=False)

            estimated_cost = project.calculate_cost()

            project.save()
        
            return redirect ('project_details', pk=pk)
    else:
        form = ProjectDetails(instance=project)
    return render(request, 'projectform.html', {'form': form, 'project': project})

@login_required
def delete(request, pk):
    project = get_object_or_404(budget, pk=pk )
    if request.method == 'POST':
        project.delete()
        return redirect ('project_list')
    return render (request, 'delete.html', {'project': project})
