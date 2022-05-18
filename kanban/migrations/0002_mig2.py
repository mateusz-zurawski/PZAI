import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-date_modified']},
        ),
        migrations.AlterField(
            model_name='task',
            name='author',
            field=models.CharField(default='No Author', max_length=200),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 23, 19, 5, 296844)),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 23, 19, 5, 296844)),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('TODO', 'To Do'), ('TEST', 'In Testing'), ('PROG', 'In Progress'), ('DONE', 'Done')], default='TODO', max_length=4),
        ),
        migrations.AlterField(
            model_name='task',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('da6ac494-1366-42d4-9874-5a617fc3a5d0'), editable=False, primary_key=True, serialize=False),
        ),
    ]