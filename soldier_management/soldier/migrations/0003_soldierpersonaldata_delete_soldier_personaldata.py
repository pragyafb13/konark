# Generated by Django 4.2.2 on 2023-06-22 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soldier', '0002_rename_personaldata_soldier_personaldata_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoldierPersonalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('dob', models.CharField(max_length=10, null=True)),
                ('doe', models.CharField(max_length=10, null=True)),
                ('civ_edn', models.CharField(max_length=255, null=True)),
                ('blood_gp', models.CharField(max_length=10, null=True)),
                ('i_card_no', models.CharField(max_length=255, null=True)),
                ('indl_acct_no', models.CharField(max_length=255, null=True)),
                ('part_order', models.CharField(max_length=255, null=True)),
                ('jt_acct_no', models.CharField(max_length=255, null=True)),
                ('aadhar_card', models.CharField(max_length=255, null=True)),
                ('pan_card', models.CharField(max_length=255, null=True)),
                ('email_id', models.CharField(max_length=255, null=True)),
                ('mobile_no', models.CharField(max_length=20, null=True)),
                ('family_detail', models.CharField(max_length=255, null=True)),
                ('father', models.CharField(max_length=255, null=True)),
                ('mother', models.CharField(max_length=255, null=True)),
                ('son', models.CharField(max_length=255, null=True)),
                ('daughter', models.CharField(max_length=255, null=True)),
                ('home_address', models.CharField(max_length=255, null=True)),
                ('vill_house_no', models.CharField(max_length=255, null=True)),
                ('post_office', models.CharField(max_length=255, null=True)),
                ('teh', models.CharField(max_length=255, null=True)),
                ('police_stn', models.CharField(max_length=255, null=True)),
                ('dist', models.CharField(max_length=255, null=True)),
                ('state', models.CharField(max_length=255, null=True)),
                ('pin_code', models.CharField(max_length=10, null=True)),
                ('promotion_cadre', models.CharField(max_length=255, null=True)),
                ('upgradation_cadre', models.CharField(blank=True, max_length=255, null=True)),
                ('mil_edn', models.CharField(max_length=255, null=True)),
                ('course', models.CharField(max_length=255, null=True)),
                ('sports', models.CharField(max_length=255, null=True)),
                ('ere', models.CharField(max_length=255, null=True)),
                ('award', models.CharField(max_length=255, null=True)),
                ('med', models.CharField(max_length=255, null=True)),
                ('red_entry', models.CharField(max_length=255, null=True)),
                ('misc', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='soldier_personaldata',
        ),
    ]