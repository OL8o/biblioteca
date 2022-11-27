# Generated by Django 3.2.15 on 2022-11-26 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_auto_20221124_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='pages/')),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='content',
        ),
        migrations.AlterField(
            model_name='book',
            name='mp3_file',
            field=models.FileField(blank=True, null=True, upload_to='mp3_files/'),
        ),
        migrations.DeleteModel(
            name='Audio',
        ),
        migrations.AddField(
            model_name='page',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='books.book'),
        ),
    ]