# Generated by Django 4.1.7 on 2023-02-26 19:33

from django.db import migrations, models
import django.db.models.deletion
import ipam.fields
import taggit.managers
import utilities.json


class Migration(migrations.Migration):

    dependencies = [
        ('tenancy', '0009_standardize_description_comments'),
        ('extras', '0087_dashboard'),
        ('ipam', '0063_standardize_description_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='ASNRange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('start', ipam.fields.ASNField()),
                ('end', ipam.fields.ASNField()),
                ('rir', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='asn_ranges', to='ipam.rir')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='asn_ranges', to='tenancy.tenant')),
            ],
            options={
                'verbose_name': 'ASN range',
                'verbose_name_plural': 'ASN ranges',
                'ordering': ('name',),
            },
        ),
    ]
