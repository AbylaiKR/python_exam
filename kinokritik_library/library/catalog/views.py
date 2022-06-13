import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django import template
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from .models import Movie, Genre, Comment, Rating
from .forms import CommentForm, RatingForm

register = template.Library()


class MovieListView(generic.ListView):
    model = Movie
    paginate_by = 8


class MovieDetailView(FormMixin, generic.DetailView):
    model = Movie
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rating_form = RatingForm()
        comment_form = CommentForm()

        context['rating_form'] = rating_form
        context['comment_form'] = comment_form

        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('movie_detail', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        rating_form = RatingForm(request.POST, None)
        comment_form = CommentForm(request.POST, None)
        if rating_form.is_valid():
            return self.rating_form_valid(rating_form)
        elif comment_form.is_valid():
            return self.comment_form_valid(comment_form)

    def rating_form_valid(self, form):
        self.object = form.save(commit=False)
        rating = self.request.POST.get('rating', '')
        self.object.user = self.request.user
        self.object.movie = self.get_object()
        self.object.rating = rating
        self.object.save()
        return super().form_valid(form)

    def comment_form_valid(self, form):
        self.object = form.save(commit=False)
        comment = self.request.POST.get('comment_text', '')
        self.object.user = self.request.user
        self.object.movie = self.get_object()
        self.object.comment_text = comment
        self.object.comment_date = datetime.datetime.now()
        self.object.save()
        return super().form_valid(form)


class GenreMovieView(generic.ListView):
    model = Movie
    template_name = 'catalog/movie_list'
    paginate_by = 8

    def get_queryset(self):
        return Movie.objects.filter(genre__id=self.kwargs['pk'])


class CommentListView(generic.ListView):
    model = Comment

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)


class CommentDelete(DeleteView):
    model = Comment
    success_url = reverse_lazy('comment_list')


class CommentUpdate(UpdateView):
    model = Comment
    form_class = CommentForm
    success_url = reverse_lazy('comment_list')






