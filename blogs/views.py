from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog
from django.utils import timezone

class BlogListView(ListView):
    model = Blog
    template_name = 'blogs/blog_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(status='published', published_at__lte=timezone.now())

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogs/blog_detail.html'
    context_object_name = 'blogs'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save(update_fields=['views_count'])
        return obj

class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'content', 'preview', 'status']
    template_name = 'blogs/blog_form.html'
    success_url = reverse_lazy('blogs:blog_list')

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'preview', 'status']
    template_name = 'blogs/blog_form.html'

    def get_success_url(self):
        return reverse('blogs:blog_detail', kwargs={'pk': self.object.pk})

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blogs/blog_confirm_delete.html'
    success_url = reverse_lazy('blogs:blog_list')
