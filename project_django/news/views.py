from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Article,Category
from .forms import ArticleForm
from django.urls import reverse_lazy

# A mixin to check if the user is a teacher
class CategoryArticleListView(ListView):
    model = Article
    template_name = 'news/article_list.html'  # We can reuse the same template
    context_object_name = 'articles'

    def get_queryset(self):
        # This is the core filtering logic. It gets the category from the URL
        # and filters the articles based on it.
        self.category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
        return Article.objects.filter(category=self.category).order_by('-created_at')

    def get_context_data(self, **kwargs):
        # This method passes the specific category object to the template
        # so you can display its name (e.g., "Articles in: Sports").
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context
class TeacherRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.role == 'teacher'

class ArticleListView(ListView):
    model = Article
    template_name = 'news/article_list.html'
    context_object_name = 'articles'
    ordering = ['-created_at']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all() 
        return context

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'news/article_detail.html'

class ArticleCreateView(LoginRequiredMixin, TeacherRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'news/article_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, TeacherRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'news/article_form.html'