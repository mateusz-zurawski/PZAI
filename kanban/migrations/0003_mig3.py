import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0002_mig2'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskComment',
            fields=[
                ('uuid', models.UUIDField(default=uuid.UUID('0f1686f3-4d53-47a9-8764-b7c26000d65f'), editable=False, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('date_created', models.DateTimeField(default=datetime.datetime(2022, 5, 31, 23, 22, 55, 9700))),
                ('date_modified', models.DateTimeField(default=datetime.datetime(2022, 5, 31, 23, 22, 55, 9700))),
                ('author', models.CharField(default='No Author', max_length=200)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.AlterField(
            model_name='task',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 23, 22, 55, 8699)),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 23, 22, 55, 8699)),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('DONE', 'Done'), ('TEST', 'In Testing'), ('PROG', 'In Progress'), ('TODO', 'To Do')], default='TODO', max_length=4),
        ),
        migrations.AlterField(
            model_name='task',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('90d86e56-77e6-4b36-8e6b-af224012319e'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='taskcomment',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kanban.Task'),
        ),
    ]
