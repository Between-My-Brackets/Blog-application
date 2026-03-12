from .models import Post, Category

def sidebar_content(request):
    return {
        'recent_posts': Post.objects.all().order_by('-date_posted')[:5],
        'categories': Category.objects.all()
    }
