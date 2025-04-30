from django.shortcuts import render, redirect
from berita.models import Kategori, Artikel
from berita.forms import Artikelform


# Create your views here.
def dashboard(request):
    template_name = "dashboard/index.html"
    context = {
        'title': 'Dashoard'
    }
    return render(request, template_name, context)


def kategori_list(request):
    template_name = "dashboard/snippet/kategori.html"
    kategori = Kategori.objects.all()
    context = {
        'title': 'Kategori',
        'kategori': kategori
    }
    return render(request, template_name, context)


def kategori_add(request):
    template_name = "dashboard/snippet/kategori_add.html"
    if request.method == "POST":
        nama_input = request.POST.get('nama_kategori')
        Kategori.objects.create(
            nama=nama_input)
        return redirect(kategori_list)
    context = {
        'title': 'Add',
    }
    return render(request, template_name, context)


def kategori_update(request, id_kategori):
    template_name = "dashboard/snippet/kategori_update.html"
    try:
        kategori = Kategori.objects.get(id=id_kategori)
    except:
        return redirect(kategori_list())
    if request.method == "POST":
        nama_input = request.POST.get('nama_kategori')
        kategori.nama = nama_input
        kategori.save()
        return redirect(kategori_list)
    context = {
        'title': 'Update',
        'kategori': kategori
    }
    return render(request, template_name, context)


def kategori_delete(request, id_kategori):
    try:
        Kategori.objects.get(id=id_kategori).delete()
    except:
        return redirect(kategori_list)


def artikel_list(request):
    template_name = "dashboard/snippet/artikel.html"
    artikel = Artikel.objects.all()
    context = {
        'title': 'Daftar Katalog',
        'artikel': artikel
    }
    return render(request, template_name, context)


def artikel_add(request):
    template_name = "dashboard/snippet/artikel_forms.html"
    if request.method == "POST":
        forms = Artikelform(request.POST, request.FILES)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.author = request.user
            pub.save()
            return redirect(artikel_list)
        else:
            print(forms.error_class)
    forms = Artikelform()
    context = {
        'title': 'Daftar Katalog',
        'form': forms
    }
    return render(request, template_name, context)


def artikel_detail(request, id_artikel):
    template_name = "dashboard/snippet/artikel_detail.html"
    artikel = Artikel.objects.get(id=id_artikel)
    context = {
        'title': artikel.nama,
        'artikel': artikel
    }
    return render(request, template_name, context)

def artikel_update(request, id_artikel):
    template_name = "dashboard/snippet/artikel_forms.html"
    artikel = Artikel.objects.get(id = id_artikel)
    if request.method == "POST":
        forms = Artikelform(request.POST, request.FILES, instance=artikel)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.author = request.user
            pub.save()
            return redirect(artikel)
    forms = Artikelform(instance=artikel)
    context = {
        'title': 'Tambah Artikel',
        'artikel': forms
    }
    return render(request, template_name, context)

def artikel_delete(request, id_artikel):
    try:
        Artikel.objects.get(id=id_artikel).delete()
    except:
        pass
        return redirect(artikel_list)