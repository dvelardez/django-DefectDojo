# Generated by Django 2.2.4 on 2020-01-02 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0026_login_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jira_conf',
            name='default_issue_type',
            field=models.CharField(choices=[('Task', 'Task'), ('Story', 'Story'), ('Epic', 'Epic'), ('Spike', 'Spike'), ('Bug', 'Bug'), ('Security', 'Security')], default='Bug', help_text='You can define extra issue types in settings.py', max_length=15),
        ),
    ]
