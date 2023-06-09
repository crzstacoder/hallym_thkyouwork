from django.shortcuts import render, redirect
from .forms import PostForm


def write_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thankyoupost:post_list')
    else:
        form = PostForm()

    return render(request, 'write_post.html', {'form': form})
