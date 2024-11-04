from django import forms
from django.contrib.auth.models import Group, User
from django.db.models import Q

from management.booking.models import Booking
from management.package.models import Package
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'start_Date': forms.DateInput(attrs={'type': 'date', 'class': 'datepicker', 'id': 'start_date'}),
            'end_Date': forms.DateInput(attrs={'type': 'date', 'class': 'datepicker', 'id': 'end_date'}),
        }

    def __init__(self, *args, **kwargs):
        package = kwargs.pop('package', None)
        super(BookingForm, self).__init__(*args, **kwargs)
        if package is not None:
            self.fields['Package'].initial = package
        agent_group = Group.objects.filter(name="Agent").first()

        # Filter users who are either in the 'Agent' group or are staff members
        if agent_group:
            self.fields['user'].queryset = User.objects.filter(
                Q(groups=agent_group) | Q(is_staff=True)
            )
        else:
            # If the 'Agent' group doesn't exist, fallback to filtering by staff status
            self.fields['user'].queryset = User.objects.filter(is_staff=True)