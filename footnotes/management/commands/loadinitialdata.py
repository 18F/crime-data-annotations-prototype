from django.core.management.base import BaseCommand, CommandError
from footnotes.models import Agency, Annotation, USState, Year

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        for year in Year.YEARS:
            try:
                y = Year.objects.get(year=year[0])
            except:
                y = Year()
                y.year = year[0]
                y.save()

        for state in USState.US_STATES:
            try:
                s = USState.objects.get(name=state[0])
            except:
                s = USState()
                s.name = state[0]
                s.save()
 
