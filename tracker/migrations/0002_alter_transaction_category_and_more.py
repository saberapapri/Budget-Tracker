# Generated by Django 5.1.1 on 2024-09-28 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.CharField(choices=[('food', 'Food'), ('transport', 'Transport'), ('utilities', 'Utilities')], max_length=20),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('income', 'Income'), ('expense', 'Expense')], max_length=10),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
