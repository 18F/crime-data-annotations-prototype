from django.db import models

from .agency_oris import AGENCIES

class Offense(models.Model):
    code = models.TextField(max_length=10)

class USState(models.Model):
    US_STATES = (
        ('AK', 'Alaska'),
        ('CA', 'California'),
        ('ID', 'Idaho'),
        ('NY', 'New York'),
        ('WV', 'West Virginia')
    )
    name = models.TextField(choices=US_STATES, unique=True)

    def __str__(self):
        return "%s" % self.name

class Year(models.Model):
    YEARS = [(y,"%s" % y) for y in range(1996, 2017 + 1)]
    year = models.IntegerField(choices=YEARS, unique=True)

    def __str__(self):
        return "%s" % self.year


class Agency(models.Model):
    ORIS = [(a['ori'], a['ori']) for a in AGENCIES]
    TYPES = [
        ('city', 'city'),
        ('county', 'county'),
    ]
    ori = models.TextField('ORI', choices=ORIS, unique=True)
    name = models.TextField('Agency name')
    agency_type = models.TextField('Agency type', choices=TYPES)
    us_state = models.ForeignKey(USState, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.ori, self.name)

class Annotation(models.Model):
    ANNOTATION_TYPES = (
        ('caveat', 'Caveat'),
        ('footnote', 'Footnote')
    )

    DATA_TYPES = (
        ('all', 'all'),
        ('estimated', 'estimated'),
        ('raw', 'raw'),
    )

    agency_ori = models.ForeignKey(Agency, blank=True, null=True, on_delete=models.CASCADE)
    data_type = models.TextField(choices=DATA_TYPES)
    offense = models.ForeignKey(Offense, blank=True, null=True, on_delete=models.CASCADE)
    annontation_type = models.TextField(choices=ANNOTATION_TYPES)
    annotation_text = models.TextField(blank=True, null=True)
    us_state = models.ForeignKey(USState, blank=True, null=True, on_delete=models.CASCADE)
    years = models.ManyToManyField(Year, blank=True)
