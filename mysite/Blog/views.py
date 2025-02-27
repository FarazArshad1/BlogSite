
from django.shortcuts import get_object_or_404, render
import sys
from .models import Post

def printError(e):
    error_type = type(e).__name__
    line_number = sys.exc_info()[-1].tb_lineno
    error_name = e.args[0] if e.args else "No additional information available"
    error_msg = f"Error Type: {error_type}\nError Name: {error_name}\nLine where error occurred: {line_number}"
    print(error_msg)

def post_list(request):
    try:
        posts = Post.published.all()
        return render(
            request,
            'Post\List.html',
            {'posts': posts}
        )
    except Exception as e:
        printError(e)
        return render(
            request,
            'Post\List.html',
            {'posts': posts}
        )

def post_detail(request, id):
    try:
        post = get_object_or_404(
            Post,
            id=id,
            status=Post.Status.PUBLISHED
        )
        return render(
            request,
            'Post\Detail.html',
            {'post': post}
        )
    except Exception as e:
        printError(e)
        return render(
            request,
            'Post\Detail.html',
            {'post': post}
        )

