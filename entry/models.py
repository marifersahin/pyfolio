from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(_('title'), max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s" % (self.title)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Entry(models.Model):
    category = models.ForeignKey(Category, verbose_name=_('category'))

    title = models.CharField(_('title'), max_length=100)
    content = models.TextField(_('content'))
    image = models.ImageField(_('image'), null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, verbose_name=_('user'),
        null=True, blank=True)


    def __unicode__(self):
        return "%s - [%s]" % (self.title, self.category)

    def get_absolute_url(self):
        return "/entry/%s" % (self.id)

    class Meta:
        verbose_name = _('Entry')
        verbose_name_plural = _('Entries')
