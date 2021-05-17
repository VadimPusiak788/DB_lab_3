from django.views.generic import ListView, DetailView
from note.models import Note
from .utils import Calendar
from django.utils.safestring import mark_safe
from .calendar_data import get_date, prev_month, next_month
from django.contrib.auth.mixins import LoginRequiredMixin


class CalendarView(LoginRequiredMixin, ListView):

    model = Note
    template_name = 'collection/calendar.html'
    login_url = '../../login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        d = get_date(self.request.GET.get('month', None))
        user = self.request.user
        cal = Calendar(d.year, d.month, user)

        html_cal = cal.formatmonth()
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context




