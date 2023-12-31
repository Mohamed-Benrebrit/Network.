# Generated by Django 4.0.4 on 2022-11-24 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_remove_following_followpfk'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='numoflikes',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likedpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likedpost', to='network.post')),
                ('userlike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userlike', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
