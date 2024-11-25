from datetime import timedelta
from django import forms
from django.utils import timezone
from events.models import Event  # Make sure you are importing from the correct path

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'name', 'description', 'event_time', 'location', 'capacity_limit',
            'registration_start', 'registration_end', 'activity_type', 'status', 
            'poster', 'language'
        ]
    
    event_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )
    registration_start = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )
    registration_end = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    def clean(self):
        cleaned_data = super().clean()
        event_time = cleaned_data.get("event_time")
        registration_start = cleaned_data.get("registration_start")
        registration_end = cleaned_data.get("registration_end")
        
        now = timezone.now()

        # Validate registration times
        if registration_start and registration_end:
            if registration_start >= registration_end:
                self.add_error("registration_start", "開始報名時間要在截止時間之前")
            if registration_start <= now or registration_end <= now:
                self.add_error("registration_start", "開始報名時間要在未來")
                self.add_error("registration_end", "截止報名時間要在未來")

        # Ensure event time is also in the future if needed
        if event_time and event_time <= now:
            self.add_error("event_time", "活動時間要在未來")
        
        return cleaned_data