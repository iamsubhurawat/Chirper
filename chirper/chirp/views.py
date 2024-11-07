from django.shortcuts import render, get_object_or_404, redirect
from .models import chirp
from .forms import chirpform, registrationform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
def chirp_list(request):
    chirps = chirp.objects.all().order_by('created_at')
    return render(request, 'chirp_list.html', {'chirps':chirps})

@login_required
def chirp_create(request):
    if request.method == "POST":
        form = chirpform(request.POST, request.FILES)
        if form.is_valid():
            chirp_data = form.save(commit=False)
            chirp_data.user = request.user
            chirp_data.save()
            return redirect('chirp_list')
    else:
        form = chirpform()
    return render(request, 'chirp_form.html', {'form': form})    

@login_required
def chirp_edit(request, chirp_id):
    chirp_data = get_object_or_404(chirp,pk=chirp_id, user=request.user)
    if request.method == "POST":
        form = chirpform(request.POST, request.FILES,instance=chirp_data)
        if form.is_valid():
            chirp_data = form.save(commit=False)
            chirp_data.user = request.user
            chirp_data.save()
            return redirect('chirp_list')
    else:
        form = chirpform(instance=chirp_data)
    return render(request, 'chirp_form.html', {'form': form})

@login_required
def chirp_delete(request, chirp_id):
    chirp_data = get_object_or_404(chirp, pk=chirp_id, user=request.user)
    if request.method == "POST":
        chirp_data.delete()
        return redirect('chirp_list')
    return render(request, 'chirp_confirm_delete.html',{'chirp_data': chirp_data})

def register(request):
    if request.method == "POST":
        form = registrationform(request.POST)
        if form.is_valid():
            user_data = form.save(commit=False)
            user_data.set_password(form.cleaned_data['password1'])
            user_data.save()
            login(request,user_data)
            return redirect('chirp_list')
    else:
        form = registrationform()
    return render(request, 'registration/register.html', {'form': form})