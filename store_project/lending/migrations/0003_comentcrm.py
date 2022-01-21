# Generated by Django 4.0.1 on 2022-01-20 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lending', '0002_statuscrm_order_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComentCrm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coment_text', models.TextField(verbose_name='Текст комментария')),
                ('coment_dt', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('coment_binding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lending.order', verbose_name='Заявка')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Коментарии',
            },
        ),
    ]