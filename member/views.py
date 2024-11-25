from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from events.models import Registration, Event
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver

from member.forms import EventForm
from .models import UserProfile
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('event_list')

# 注册视图
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# 用户资料视图
@login_required
def profile(request):
    user = request.user
    registrations = Registration.objects.filter(user=user).select_related('event')

    # 确保 UserProfile 存在
    try:
        profile = user.userprofile
    except UserProfile.DoesNotExist:
        profile = None

    if user.is_superuser:
        return admin_dashboard(request)
    else:
        return render(request, 'member/profile.html', {
            'user': user,
            'registrations': registrations,
            'qr_code': profile.qr_code.url if profile and profile.qr_code else None,
        })

# 管理员仪表板视图
@login_required
def admin_dashboard(request):
    events = Event.objects.all()  # 获取所有事件
    registrations = Registration.objects.all()  # 获取所有注册
    return render(request, 'member/admin_dashboard.html', {
        'events': events,
        'registrations': registrations
    })

# 创建事件视图
@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')  # 创建事件后跳转到管理员仪表板
    else:
        form = EventForm()
    return render(request, 'member/create_event.html', {'form': form})

# 信号处理器：自动创建 UserProfile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()
