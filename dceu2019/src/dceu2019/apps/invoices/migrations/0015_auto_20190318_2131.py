# Generated by Django 2.1.4 on 2019-03-18 21:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0014_ticketbutlerticket_invited_when'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketbutlerticket',
            name='invoices',
            field=models.ManyToManyField(blank=True, related_name='tickets', to='invoices.Invoice'),
        ),
        migrations.AlterField(
            model_name='ticketbutlerticket',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='invoices.Invoice'),
        ),
    ]
