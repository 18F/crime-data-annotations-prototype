from django.core.management.base import BaseCommand, CommandError
from footnotes.models import Agency, Annotation, USState, Year
from footnotes.agency_oris import AGENCIES

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
                print('Created year: %s' % year[0])

        for state in USState.US_STATES:
            try:
                s = USState.objects.get(name=state[0])
            except:
                s = USState()
                s.name = state[0]
                s.save()
                print('Created state: %s' % state[0])

        agencies = list(AGENCIES.items())
        for agency in agencies:
            try:
                a = Agency.objects.get(ori=agency[0])
            except:
                abbr = agency[0][0:2]
                a = Agency()
                a.ori = agency[0]
                a.name = agency[1]
                a.us_state = USState.objects.get(name=abbr)
                a.save()
                print('Created agency: %s' % agency[0])
