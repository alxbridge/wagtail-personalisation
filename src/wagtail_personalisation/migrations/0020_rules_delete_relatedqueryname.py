# Generated by Django 2.0.5 on 2018-05-30 18:51

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_personalisation', '0019_auto_20180526_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayrule',
            name='segment',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='wagtail_personalisation_dayrules', to='wagtail_personalisation.Segment'),
        ),
        migrations.AlterField(
            model_name='devicerule',
            name='segment',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='wagtail_personalisation_devicerules', to='wagtail_personalisation.Segment'),
        ),
        migrations.AlterField(
            model_name='queryrule',
            name='segment',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='wagtail_personalisation_queryrules', to='wagtail_personalisation.Segment'),
        ),
        migrations.AlterField(
            model_name='referralrule',
            name='segment',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='wagtail_personalisation_referralrules', to='wagtail_personalisation.Segment'),
        ),
        migrations.AlterField(
            model_name='timerule',
            name='segment',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='wagtail_personalisation_timerules', to='wagtail_personalisation.Segment'),
        ),
        migrations.AlterField(
            model_name='userisloggedinrule',
            name='segment',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='wagtail_personalisation_userisloggedinrules', to='wagtail_personalisation.Segment'),
        ),
        migrations.AlterField(
            model_name='visitcountrule',
            name='segment',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='wagtail_personalisation_visitcountrules', to='wagtail_personalisation.Segment'),
        ),
    ]
