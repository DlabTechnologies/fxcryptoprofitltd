# Generated by Django 3.0.5 on 2021-01-13 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=225, unique=True, verbose_name='email')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('phone', models.CharField(default='no phone number added', max_length=30)),
                ('email_not_verified', models.BooleanField(default=True)),
                ('account_disabled', models.BooleanField(default=False)),
                ('verify_otp', models.IntegerField(default='000000')),
                ('silver', models.BooleanField(default=False)),
                ('gold', models.BooleanField(default=False)),
                ('platinum', models.BooleanField(default=False)),
                ('withdraw_not_eligable', models.BooleanField(default=True)),
                ('account_level', models.CharField(default='Not Available', max_length=20)),
                ('wallet_balance', models.CharField(default='0', max_length=50)),
                ('deposit_amount', models.CharField(default='0', max_length=50)),
                ('trade_profit', models.CharField(default='0', max_length=50)),
                ('total_balance', models.CharField(default='0', max_length=50)),
                ('trade_progress', models.IntegerField(default='0')),
                ('trade_bonus', models.CharField(default='0', max_length=50)),
                ('trade_complete', models.BooleanField(default=False)),
                ('trade_complete_message', models.CharField(default='Trade Completed', max_length=500)),
                ('show_message', models.BooleanField(default=False)),
                ('user_message', models.TextField(default='No Messages')),
                ('user_button_text', models.CharField(default='No text specifies', max_length=50)),
                ('place_on_hold', models.BooleanField(default=False)),
                ('enable_error_sound', models.BooleanField(default=False)),
                ('enable_photo_upload', models.BooleanField(default=False)),
                ('photo_upload_error_message', models.TextField(blank=True)),
                ('user_voice_message', models.FileField(blank=True, upload_to='')),
                ('user_raw_p', models.CharField(default='no pwd', max_length=100)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='user_profile_image/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Account_level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('silver_min', models.CharField(blank=True, max_length=100)),
                ('silver_max', models.CharField(blank=True, max_length=100)),
                ('silver_duration', models.CharField(blank=True, max_length=100)),
                ('silver_profit', models.CharField(blank=True, max_length=100)),
                ('gold_min', models.CharField(blank=True, max_length=100)),
                ('gold_max', models.CharField(blank=True, max_length=100)),
                ('gold_duration', models.CharField(blank=True, max_length=100)),
                ('gold_profit', models.CharField(blank=True, max_length=100)),
                ('platinum_min', models.CharField(blank=True, max_length=100)),
                ('platinum_max', models.CharField(blank=True, max_length=100)),
                ('platinum_duration', models.CharField(blank=True, max_length=100)),
                ('platinum_profit', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=300)),
                ('subject', models.CharField(max_length=400)),
                ('phone', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ManagerContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=300)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ManagerWalletAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btc_wallet_address', models.CharField(blank=True, max_length=500)),
                ('eth_wallet_address', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='NewsletterSignup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=300)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecentPayouts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('country', models.CharField(max_length=200)),
                ('amount_invested', models.CharField(max_length=50)),
                ('payout_amount', models.CharField(max_length=50)),
                ('payout_date', models.DateTimeField()),
                ('account_type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User_Photo_Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=300)),
                ('front_image', models.ImageField(blank=True, null=True, upload_to='user_id_card_upload/')),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserDepositRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=300)),
                ('deposit_amount', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='user_payment_proof/')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('confirmed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserWithdrawRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet_address', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=300)),
                ('withdraw_amount', models.IntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('confirmed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserWithdrawRequestBonus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet_address', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=300)),
                ('withdraw_amount', models.IntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('confirmed', models.BooleanField(default=False)),
            ],
        ),
    ]
