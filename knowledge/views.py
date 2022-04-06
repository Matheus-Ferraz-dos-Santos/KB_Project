from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import (TemplateView, ListView, DetailView,
                                    CreateView, UpdateView,
                                    DeleteView)
from knowledge.models import Manual, Article, Comments
from django.contrib.auth.mixins import LoginRequiredMixin
from knowledge.forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required


# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'knowledge/article_list.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all.order_by('-created_at')[0:3]
        context['manuals'] = Manual.objects.all()
        return context

    def get_queryset(self):
        return Article.objects.filter(status='published', published_at__lte=timezone.now())

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'knowledge/article_detail.html'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    login_url = '/login/'
    form_class = ArticleForm
    redirect_field_name = 'knowledge/article_detail.html'

    def form_valid(self, form):
        form.instance.author == self.request.user.author:
        form.save()
        return redirect(reverse('article_detail', kwargs={'slug': form.instance.slug}))
