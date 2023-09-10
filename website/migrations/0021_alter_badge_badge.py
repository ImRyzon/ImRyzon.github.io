# Generated by Django 4.2.4 on 2023-09-10 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_alter_comment_replies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='badge',
            field=models.CharField(choices=[('HTML', 'HTML'), ('CSS', 'CSS'), ('Python', 'Python'), ('JavaScript', 'JavaScript'), ('Java', 'Java'), ('C++', 'C++'), ('C#', 'C#'), ('SQL', 'SQL'), ('PHP', 'PHP'), ('Flask', 'Flask'), ('Django', 'Django'), ('React.js', 'React.js'), ('Cybersecurity', 'Cybersecurity'), ('Algorithms', 'Algorithms'), ('Data Structures', 'Data Structures'), ('Competitive Programming', 'Competitive Programming'), ('CTF', 'CTF'), ('Web', 'Web'), ('CS50', 'CS50'), ('AI', 'AI'), ('GUI', 'GUI'), ('BOT', 'BOT')], default=None, max_length=32, unique=True),
        ),
    ]
