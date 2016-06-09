# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0013_auto_20160609_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(validators=[django.core.validators.RegexValidator(regex=b'^[A-Za-z]*$')], choices=[(b'CSE', 'CSE'), (b'EEE', 'EEE'), (b'ME', 'ME'), (b'EC', 'EC'), (b'BCA', 'BCA')], max_length=32, blank=True, null=True, verbose_name='Branch'),
        ),
        migrations.AlterField(
            model_name='student',
            name='curr_arrears',
            field=models.IntegerField(null=True, verbose_name='No of current arrears', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='hist_arrears',
            field=models.IntegerField(null=True, verbose_name='No of history arrears', blank=True),
        ),
    ]
