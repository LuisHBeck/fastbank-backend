# Generated by Django 4.2.6 on 2023-10-11 00:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='naturalperson',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='natural_person', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='loan',
            name='id_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.account'),
        ),
        migrations.AddField(
            model_name='legalperson',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='legal_person', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='installment',
            name='id_loan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.loan'),
        ),
        migrations.AddField(
            model_name='email',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_email', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cardtransaction',
            name='id_card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.card'),
        ),
        migrations.AddField(
            model_name='card',
            name='id_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.account'),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='accountinvestments',
            name='id_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.account'),
        ),
        migrations.AddField(
            model_name='accountinvestments',
            name='id_investment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.investment'),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
