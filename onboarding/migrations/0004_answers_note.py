# Generated by Django 3.0.5 on 2020-06-23 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onboarding', '0003_answers_exam_question_user_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='note',
            field=models.CharField(default='None', max_length=800),
            preserve_default=False,
        ),
    ]