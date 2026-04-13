from django.db import models


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('language',  'Programming Languages'),
        ('framework', 'Backend Frameworks'),
        ('database',  'Databases'),
        ('web',       'Web Technologies'),
        ('tool',      'Tools & Version Control'),
        ('practice',  'Dev Practices'),
    ]
    name     = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    order    = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Service(models.Model):
    ICON_CHOICES = [
        ('fa-server',      'Server / Backend'),
        ('fa-plug',        'API'),
        ('fa-database',    'Database'),
        ('fa-shield-alt',  'Security'),
        ('fa-code',        'Code'),
        ('fa-cogs',        'Settings / DevOps'),
        ('fa-globe',       'Web'),
        ('fa-vial',        'Testing'),
    ]
    title       = models.CharField(max_length=200)
    description = models.TextField()
    icon        = models.CharField(max_length=50, choices=ICON_CHOICES, default='fa-code')
    order       = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    ICON_CHOICES = [
        ('fa-hospital',   'Hospital'),
        ('fa-briefcase',  'Briefcase'),
        ('fa-share-alt',  'Social Media'),
        ('fa-apple-alt',  'Food/Health'),
        ('fa-wallet',     'Finance'),
        ('fa-code',       'Code'),
        ('fa-globe',      'Web'),
        ('fa-database',   'Database'),
    ]
    title        = models.CharField(max_length=200)
    description  = models.TextField()
    icon         = models.CharField(max_length=50, choices=ICON_CHOICES, default='fa-code')
    technologies = models.CharField(max_length=300, help_text="Comma separated: Django, MySQL, Bootstrap")
    github_url   = models.URLField(blank=True, null=True)
    live_url     = models.URLField(blank=True, null=True)
    order        = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def get_tech_list(self):
        return [t.strip() for t in self.technologies.split(',')]


class Experience(models.Model):
    title       = models.CharField(max_length=200)
    company     = models.CharField(max_length=200)
    location    = models.CharField(max_length=100, blank=True)
    start_date  = models.CharField(max_length=50)
    end_date    = models.CharField(max_length=50, default='Present')
    description = models.TextField(help_text="Each bullet on a new line")
    order       = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} at {self.company}"

    def get_points(self):
        return [l.strip() for l in self.description.split('\n') if l.strip()]


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree      = models.CharField(max_length=200)
    location    = models.CharField(max_length=100, blank=True)
    start_year  = models.CharField(max_length=20)
    end_year    = models.CharField(max_length=20)
    cgpa        = models.CharField(max_length=20, blank=True)
    icon        = models.CharField(max_length=50, default='fa-university')
    order       = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.degree} — {self.institution}"


class Contact(models.Model):
    name       = models.CharField(max_length=200)
    email      = models.EmailField()
    subject    = models.CharField(max_length=300, blank=True)
    message    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read    = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name}"
