from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import UserContactForm, SendEmailForm, UserNewsletterSignup
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from account.models import ManagerContactInfo, RecentPayouts, Account_level, NewsletterSignup
from django.contrib.auth.decorators import login_required



def home_page(request):

        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        

                
    

        info = ManagerContactInfo.objects.all()

        recent_payout = RecentPayouts.objects.all()

        form_contact = UserContactForm()
        if request.method == 'POST':
                form_contact = UserContactForm(request.POST)
                if form_contact.is_valid():
                        form_contact.save()
                        name = form_contact.cleaned_data.get('name')
                        email = form_contact.cleaned_data.get('email')
                        subject = form_contact.cleaned_data.get('subject')
                        phone = form_contact.cleaned_data.get('phone')
                        

                        message = "{0} has sent you a new message:\n\n{1} \n\n{2} \n\n{3}".format(name, subject, form_contact.cleaned_data.get('message'), phone )
                        send_mail('New Enquiry', message, email,['fxcryptoprofitltd24@gmail.com'])


                        messages.success(request, 'Message sent successfully')
                        return redirect('home_page')
        else:
                form_contact = UserContactForm()

        
        form_news = UserNewsletterSignup()
        if request.method == 'POST':
                form_news = UserNewsletterSignup(request.POST or None)
                if form_news.is_valid():
                        email_signup_qs = NewsletterSignup.objects.filter(email=form_news.instance.email)
                        if email_signup_qs.exists():
                                messages.info(request, "You are already subscribed to our newsletter updates")
                        else:
                                form_news.save()
                                messages.success(request, "You have successfully subscribe to our newsletter updates")

                                return redirect('home_page')
        else:
                form_news = UserNewsletterSignup()

        context={
                'form_contact': form_contact,
                'form_news': form_news,
                'info': info,
                'recent_payout': recent_payout
        }
        return render(request, 'index.html', context)


def contact_page(request):

        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        
        info = ManagerContactInfo.objects.all()

        form_news = UserNewsletterSignup()
        if request.method == 'POST':
                form_news = UserNewsletterSignup(request.POST or None)
                if form_news.is_valid():
                        email_signup_qs = NewsletterSignup.objects.filter(email=form_news.instance.email)
                        if email_signup_qs.exists():
                                messages.info(request, "You are already subscribed to our newsletter updates")
                        else:
                                form_news.save()
                                messages.success(request, "You have successfully subscribe to our newsletter updates")

                                return redirect('home_page')
        else:
                form_news = UserNewsletterSignup()


        context={
                'info': info,
                'form_news': form_news
        }
        return render(request, 'contact-us.html', context)


def mt4_page(request):
        
        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')

        info = ManagerContactInfo.objects.all()

        level = Account_level.objects.all()

        
        form_news = UserNewsletterSignup()
        if request.method == 'POST':
                form_news = UserNewsletterSignup(request.POST or None)
                if form_news.is_valid():
                        email_signup_qs = NewsletterSignup.objects.filter(email=form_news.instance.email)
                        if email_signup_qs.exists():
                                messages.info(request, "You are already subscribed to our newsletter updates")
                        else:
                                form_news.save()
                                messages.success(request, "You have successfully subscribe to our newsletter updates")

                                return redirect('home_page')
        else:
                form_news = UserNewsletterSignup()


        context = {
                'info': info,
                'level':level,
                'form_news': form_news
        }
        return render(request, 'metatrader4.html', context)


def mt5_page(request):
        
        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        info = ManagerContactInfo.objects.all()


        form = UserContactForm()
        if request.method == 'POST':
                form = UserContactForm(request.POST)
                if form.is_valid():
                        form.save()
                        name = form.cleaned_data.get('name')
                        email = form.cleaned_data.get('email')
                        subject = form.cleaned_data.get('subject')
                        phone = form.cleaned_data.get('phone')
                        

                        message = "{0} has sent you a new message:\n\n{1} \n\n{2} \n\n{3}".format(name, subject, form.cleaned_data.get('message'), phone )
                        send_mail('New Enquiry', message, email,['fxcryptoprofitltd24@gmail.com'])


                        messages.success(request, 'Message sent successfully')
                        return redirect('contact_page')
        else:
                form = UserContactForm()

        

        form_news = UserNewsletterSignup()
        if request.method == 'POST':
                form_news = UserNewsletterSignup(request.POST or None)
                if form_news.is_valid():
                        email_signup_qs = NewsletterSignup.objects.filter(email=form_news.instance.email)
                        if email_signup_qs.exists():
                                messages.info(request, "You are already subscribed to our newsletter updates")
                        else:
                                form_news.save()
                                messages.success(request, "You have successfully subscribe to our newsletter updates")

                                return redirect('home_page')
        else:
                form_news = UserNewsletterSignup()

        context = {
                'info': info,
                'form': form,
                'form_news': form_news
        }
        return render(request, 'metatrader5.html', context)



def pro_ecn_page(request):
        
        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')

        info = ManagerContactInfo.objects.all()

        level = Account_level.objects.all()

        
        form_news = UserNewsletterSignup()
        if request.method == 'POST':
                form_news = UserNewsletterSignup(request.POST or None)
                if form_news.is_valid():
                        email_signup_qs = NewsletterSignup.objects.filter(email=form_news.instance.email)
                        if email_signup_qs.exists():
                                messages.info(request, "You are already subscribed to our newsletter updates")
                        else:
                                form_news.save()
                                messages.success(request, "You have successfully subscribe to our newsletter updates")

                                return redirect('home_page')
        else:
                form_news = UserNewsletterSignup()


        context = {
                'info': info,
                'level':level,
                'form_news': form_news
        }
        return render(request, 'pro-ecn.html', context)



def raw_ecn_page(request):
        
        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')

        info = ManagerContactInfo.objects.all()

        level = Account_level.objects.all()

        
        form_news = UserNewsletterSignup()
        if request.method == 'POST':
                form_news = UserNewsletterSignup(request.POST or None)
                if form_news.is_valid():
                        email_signup_qs = NewsletterSignup.objects.filter(email=form_news.instance.email)
                        if email_signup_qs.exists():
                                messages.info(request, "You are already subscribed to our newsletter updates")
                        else:
                                form_news.save()
                                messages.success(request, "You have successfully subscribe to our newsletter updates")

                                return redirect('home_page')
        else:
                form_news = UserNewsletterSignup()


        context = {
                'info': info,
                'level':level,
                'form_news': form_news
        }
        return render(request, 'raw-ecn.html', context)



def standard_stp_page(request):
        
        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')

        info = ManagerContactInfo.objects.all()

        level = Account_level.objects.all()

        
        form_news = UserNewsletterSignup()
        if request.method == 'POST':
                form_news = UserNewsletterSignup(request.POST or None)
                if form_news.is_valid():
                        email_signup_qs = NewsletterSignup.objects.filter(email=form_news.instance.email)
                        if email_signup_qs.exists():
                                messages.info(request, "You are already subscribed to our newsletter updates")
                        else:
                                form_news.save()
                                messages.success(request, "You have successfully subscribe to our newsletter updates")

                                return redirect('home_page')
        else:
                form_news = UserNewsletterSignup()


        context = {
                'info': info,
                'level':level,
                'form_news': form_news
        }
        return render(request, 'standard-stp.html', context)



def webtrader_page(request):
        
        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')

        info = ManagerContactInfo.objects.all()

        level = Account_level.objects.all()

        
        form_news = UserNewsletterSignup()
        if request.method == 'POST':
                form_news = UserNewsletterSignup(request.POST or None)
                if form_news.is_valid():
                        email_signup_qs = NewsletterSignup.objects.filter(email=form_news.instance.email)
                        if email_signup_qs.exists():
                                messages.info(request, "You are already subscribed to our newsletter updates")
                        else:
                                form_news.save()
                                messages.success(request, "You have successfully subscribe to our newsletter updates")

                                return redirect('home_page')
        else:
                form_news = UserNewsletterSignup()


        context = {
                'info': info,
                'level':level,
                'form_news': form_news
        }
        return render(request, 'webtrader.html', context)




def who_we_are_page(request):
        
        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')

        info = ManagerContactInfo.objects.all()

        level = Account_level.objects.all()

        
        form_news = UserNewsletterSignup()
        if request.method == 'POST':
                form_news = UserNewsletterSignup(request.POST or None)
                if form_news.is_valid():
                        email_signup_qs = NewsletterSignup.objects.filter(email=form_news.instance.email)
                        if email_signup_qs.exists():
                                messages.info(request, "You are already subscribed to our newsletter updates")
                        else:
                                form_news.save()
                                messages.success(request, "You have successfully subscribe to our newsletter updates")

                                return redirect('home_page')
        else:
                form_news = UserNewsletterSignup()


        context = {
                'info': info,
                'level':level,
                'form_news': form_news
        }
        return render(request, 'who-we-are.html', context)



#@login_required(login_url='login')
#def SendEmail(request):
        
       # form = SendEmailForm()
       # if request.method == 'POST':
         #       form = SendEmailForm(request.POST)
           #     if form.is_valid():
                   #     to = form.cleaned_data.get('to')
            #            subject = form.cleaned_data.get('subject')
                  #      message = form.cleaned_data.get('message')
            
                        
                    #    recipient_list = [to,]    
                     #   send_mail( subject, message, 'FXCP noreply@fxcryptoprofitltd.com', recipient_list )    
                    #    messages.success(request, 'Message successfully sent to {}'.format(to))
                     #   return redirect('send_email')
            
      #  else:
       #         form = SendEmailForm()
       # context ={
        #        'form': form
       # }
       # return render (request, 'send_user_email.html', context)