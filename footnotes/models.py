from django.db import models

from footnotes.agency_oris import AGENCIES

class Offense(models.Model):
    code = models.TextField(max_length=10)

class USState(models.Model):
    US_STATES = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DC', 'Washington, DC'),
        ('DE', 'Delaware'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('MA', 'Massachusetts'),
        ('MD', 'Maryland'),
        ('ME', 'Maine'),
        ('MI', 'Michigan'),
        ('MO', 'Missouri'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MT', 'Montana'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('NB', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WI', 'Wisconsin'),
        ('WV', 'West Virginia'),
        ('WY', 'Wyoming'),
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
    ORIS = [(ori, ori) for ori in AGENCIES.keys()]
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
    annotation_type = models.TextField(choices=ANNOTATION_TYPES)
    annotation_text = models.TextField(blank=True, null=True)
    us_state = models.ForeignKey(USState, blank=True, null=True, on_delete=models.CASCADE)
    years = models.ManyToManyField(Year, blank=True)

    def __str__(self):
        if self.agency_ori and self.us_state:
            loc = '%s and %s' % (self.agency_ori, self.us_state)
        else:
            loc = '%s' % self.agency_ori or self.us_state
        return '%s annotation for %s' % (self.annotation_type.title(), loc)
