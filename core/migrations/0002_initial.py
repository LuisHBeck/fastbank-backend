# Generated by Django 4.2.5 on 2023-09-18 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LegalPerson',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('fantasy_name', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=14)),
                ('municipal_registration', models.CharField(max_length=11)),
                ('state_registration', models.CharField(max_length=9)),
                ('legal_nature', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'legal person',
                'verbose_name_plural': 'legal persons',
            },
            bases=('users.customuser',),
            managers=[
                ('objects', users.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='NaturalPerson',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
                ('cpf', models.CharField(max_length=11)),
                ('rg', models.CharField(max_length=8)),
                ('social_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'natural person',
                'verbose_name_plural': 'natural persons',
            },
            bases=('users.customuser',),
            managers=[
                ('objects', users.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(max_length=25)),
                ('timestamp', models.DateField()),
                ('operation', models.CharField(max_length=25)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('id_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.card')),
            ],
            options={
                'verbose_name': 'transaction',
                'verbose_name_plural': 'transactions',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('area_code', models.CharField(max_length=3)),
                ('prefix_number', models.CharField(max_length=3)),
                ('phone_number', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'phone',
                'verbose_name_plural': 'phones',
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('request_date', models.DateField()),
                ('amount_request', models.DecimalField(decimal_places=2, max_digits=7)),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=7)),
                ('is_approved', models.BooleanField(default=True)),
                ('approval_date', models.DateField(blank=True, null=True)),
                ('installment_amount', models.IntegerField()),
                ('observation', models.TextField()),
                ('id_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.account')),
            ],
            options={
                'verbose_name': 'loan',
                'verbose_name_plural': 'loans',
            },
        ),
        migrations.AddField(
            model_name='investment',
            name='id_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.account'),
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
            model_name='account',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
