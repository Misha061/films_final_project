from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from .forms import FilmForm, FilmCommentForm, FilmScoreForm , LoginForm, RegisterForm
from .models import Film, FilmScore, FilmComment
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin

def login_view(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {"form": form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Вітаємо {username}!")
                return redirect('film_catalog')
            else:
                messages.error(request, f"Неправильне ім'я користувача або пароль")
        return render(request, 'login.html', {"form": form})

def register_view(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, 'register.html', {"form": form})
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Реєстрація успішна!")
            return redirect('film_catalog')
        return render(request, 'register.html', {"form": form})

def logout_view(request):
    logout(request)
    messages.success(request, "Ви успішно вийшли із системи!")
    return redirect('login')

class FilmListView(ListView):
    model = Film
    form_class = FilmForm
    template_name = 'film_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        genre = self.request.GET.get('genre')
        title = self.request.GET.get('title')
        if genre:
            queryset = queryset.filter(genre__icontains=genre)

        if title:
            queryset = queryset.filter(title__icontains=title)

        return queryset

class FilmDetailView(DetailView):
    model = Film
    form_class = FilmForm
    template_name = 'film_detail.html'

class FilmCreateView(LoginRequiredMixin,CreateView):
    model = Film
    form_class = FilmForm
    template_name = "film_form.html"
    success_url = reverse_lazy("film_catalog")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class FilmUpdateView(UserPassesTestMixin,UpdateView):
    model = Film
    form_class = FilmForm
    template_name = "film_form.html"
    success_url = reverse_lazy("film_catalog")

    def get_success_url(self):

        return reverse_lazy('film_detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        film = self.get_object()
        return film.user == self.request.user

class FilmDeleteView(UserPassesTestMixin,DeleteView):
    model = Film
    template_name = "film_delete.html"
    success_url = reverse_lazy("film_catalog")

    def test_func(self):
        film = self.get_object()
        return film.user == self.request.user

class FilmCommentCreateView(LoginRequiredMixin,CreateView):
    model = FilmComment
    form_class = FilmCommentForm
    template_name = "film_form.html"

    def get_success_url(self):
        return reverse_lazy('film_detail', kwargs={'pk': self.object.film.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        film_id = self.kwargs['pk']
        film = get_object_or_404(Film, pk=film_id)
        form.instance.film = film
        return super().form_valid(form)

class FilmCommentDeleteView(UserPassesTestMixin,DeleteView):
    model = FilmComment
    template_name = "comment_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy('film_detail', kwargs={'pk': self.object.film.pk})


    def test_func(self):
        comment = self.get_object()
        return comment.user == self.request.user

class FilmUpdateCommentView(UserPassesTestMixin,CreateView):
    model = FilmComment
    form_class = FilmCommentForm
    template_name = "film_form.html"

    def get_success_url(self):
        return reverse_lazy('film_detail', kwargs={'pk': self.object.film.pk})

    def test_func(self):
        comment = self.get_object()
        return comment.user == self.request.user

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class FilmCreateScoreView(UserPassesTestMixin,UpdateView):
    model = FilmScore
    form_class = FilmScoreForm
    template_name = "film_form.html"
    def get_success_url(self):
        return reverse_lazy('film_detail', kwargs={'pk': self.object.film.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        film_id = self.kwargs['pk']
        film = get_object_or_404(Film, pk=film_id)
        form.instance.film = film
        return super().form_valid(form)

class FilmUpdateScoreView(UserPassesTestMixin,UpdateView):
    model = FilmScore
    form_class = FilmScoreForm
    template_name = "film_form.html"

    def get_success_url(self):
        return reverse_lazy('film_detail', kwargs={'pk': self.object.film.pk})

    def test_func(self):
        comment = self.get_object()
        return comment.user == self.request.user

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class FilmDeleteScoreView(UserPassesTestMixin,DeleteView):
    model = FilmScore
    template_name = "score_delete.html"

    def get_success_url(self):
        return reverse_lazy('film_detail', kwargs={'pk': self.object.film.pk})

    def test_func(self):
        comment = self.get_object()
        return comment.user == self.request.user