from django.shortcuts import render, redirect
from django.views import View
from .models import Slider, Service
from django.contrib import messages
from validate_email import validate_email
from django.core.mail import EmailMessage
from django.conf import settings
import os


class HomeView(View):
    sliders = Slider.objects.all()
    services = Service.objects.all()

    def create_service_group(services):
        group = []
        el = []
        for i in range(len(services)):

            if i % 2 == 0 or i == 0:
                el.append(services[i])

                if i == len(services)-1:
                    group.append(el)
                    el = []

            else:
                el.append(services[i])
                group.append(el)
                el = []

        return group

    services_group = create_service_group(services)
    print(os.environ.get('EMAIL_HOST'))

    context = {
        'sliders': sliders,
        'services_group': services_group,
        'activate': 'home'
    }

    def get(self, request):
        return render(request, 'home.html', context=self.context)

    def post(self, request):

        context = {
            'sliders': self.sliders,
            'services_group': self.services_group,
            'activate': 'home',
            "data": request.POST,
            'has_error': False
        }

        email = request.POST.get('email')
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if len(message) < 6:
            messages.add_message(request, messages.ERROR,
                                 'Message demasisdo corto')
            context['has_error'] = True

        if not validate_email(email):
            messages.add_message(request, messages.ERROR,
                                 'Correo electonico invalido')
            context['has_error'] = True

        if not name:
            messages.add_message(request, messages.ERROR,
                                 'El nombre es requerido')
            context['has_error'] = True

        if context['has_error']:
            return render(request, 'home.html', context, status=400)

        email_content = EmailMessage(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email]
        )

        email_content.send()

        messages.add_message(request, messages.SUCCESS,
                             'Messaje enviado con exito')

        return redirect('home')

        # return render(request, 'home.html', context=self.context)


class AboutView(View):
    context = {
        'activate': 'about'
    }

    def get(self, request):
        return render(request, 'home.html', context=self.context)


class ServicesView(View):
    pass


class ArticlesView(View):
    pass


class ContactView(View):
    pass
