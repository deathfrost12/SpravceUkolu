from django.db import models

PRIORITY_CHOICES = [
    ('low', 'Nízká'),
    ('medium', 'Střední'),
    ('high', 'Vysoká'),
]

STATUS_CHOICES = [
    ('pending', 'Čekající'),
    ('in_progress', 'V proběhu'),
    ('completed', 'Dokončeno'),
]

class Category(models.Model):
    nazev = models.CharField(max_length=100, unique=True, verbose_name='Název kategorie')
    popis = models.TextField(blank=True, null=True, verbose_name='Popis kategorie')

    class Meta:
        ordering = ['nazev']
        verbose_name = 'Kategorie'
        verbose_name_plural = 'Kategorie'

    def __str__(self):
        return self.nazev


class Project(models.Model):
    nazev = models.CharField(max_length=200, verbose_name='Název projektu')
    popis = models.TextField(blank=True, null=True, verbose_name='Popis projektu')
    start_date = models.DateField(verbose_name='Datum zahájení')
    end_date = models.DateField(verbose_name='Datum ukončení', blank=True, null=True)

    class Meta:
        ordering = ['nazev']
        verbose_name = 'Projekt'
        verbose_name_plural = 'Projekty'

    def __str__(self):
        return self.nazev


class Task(models.Model):
    nazev = models.CharField(max_length=200, verbose_name='Název úkolu')
    popis = models.TextField(blank=True, null=True, verbose_name='Popis úkolu')
    due_date = models.DateField(verbose_name='Termín splnění', blank=True, null=True)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='medium', verbose_name='Priorita')
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='pending', verbose_name='Stav')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks', verbose_name='Projekt')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks', verbose_name='Kategorie')

    class Meta:
        ordering = ['due_date', 'priority']
        verbose_name = 'Úkol'
        verbose_name_plural = 'Úkoly'

    def __str__(self):
        return self.nazev
