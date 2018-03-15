from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, Http404, redirect

from .models import Tweet
from .forms import TweetModelForm

def list_view(request):

    objects = Tweet.objects.all()

    template="list.html"

    context = {
        "ibjects": objects
    }

    return render(request, template, context)


def detail_view(request, pk= None):

    objects = Tweet.objects.get(pk=pk)
    context = {
        "objects": objects
    }
    return render(request, "detail.html", context)


def create_view(request):
    form = TweetModelForm(request.POST, None)

    context = {

        "form": form
    }

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return redirect("home")

    return render(request, "ddfd.html", context)


def update_view(request, pk=None):

    objects = get_object_or_404(Tweet, pk=pk)
    form  = TweetModelForm(request.POST, None, instance=objects)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return  redirect("view")
    return render(request, "update.html", {"form": form})


def delete_view(request, pk=None):

    objects = get_object_or_404(Tweet, pk=pk)

    if request.method=="POST":
        objects.delete()
    else:
        raise Http404("Page Not Found")

    return render(request, "delete.html", {"obj": objects})