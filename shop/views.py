from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .utils import DataMixin
from .models import *
from .forms import FeedbackForm


class MainPage(DataMixin, FormView):
    template_name = 'main.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mix_context = self.get_mixin_context()
        context.update(mix_context)
        return context

    def form_valid(self, form: FeedbackForm):
        message = form.cleaned_data
        print('message>>>>>', str(message))
        # send_mail(subject='ЗАЯВКА С САЙТА',
        #           message=message,
        #           from_email='service@octonix.ru',
        #           recipient_list=['19bdp88@gmail.com',],
        #           fail_silently=False,
        #           auth_user='service@octonix.ru',
        #           auth_password='ry7IOjgnR%FVEg',
        #           html_message=None,
        #           )
        form.save()
        return super().form_valid(self)


class ProductPage(DataMixin, FormView, TemplateView):
    template_name = 'product.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('home')
    def get_context_data(self, tag, **kwargs):
        context = super().get_context_data(**kwargs)
        mix_context = self.get_mixin_context()
        context.update(mix_context)
        context['product'] = Product.objects.get(tag=tag)
        return context

    def form_valid(self, form: FeedbackForm):
        form.save()
        return super().form_valid(self)