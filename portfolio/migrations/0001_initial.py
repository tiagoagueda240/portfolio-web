# Generated by Django 4.0.5 on 2022-06-04 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadeira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('anoLectivo', models.CharField(choices=[('ano1', '1'), ('ano2', '2'), ('ano3', '3')], default='1', max_length=4)),
                ('semestre', models.CharField(choices=[('sem1', '1'), ('sem2', '2')], max_length=4)),
                ('ano', models.IntegerField(default=2021)),
                ('ects', models.IntegerField()),
                ('topicosAbordados', models.TextField(blank=True, max_length=1000)),
                ('ranking', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=2)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Formacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(max_length=50)),
                ('local', models.CharField(max_length=50)),
                ('inicio', models.CharField(max_length=50)),
                ('fim', models.CharField(max_length=50)),
                ('imagem', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Interesse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
                ('imagem', models.ImageField(upload_to='')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Lingua',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('nivel', models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1'), ('B2', 'B2'), ('C1', 'C1'), ('C2', 'C2')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=1000)),
                ('link', models.CharField(max_length=1000)),
                ('imagem', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64)),
                ('apelido', models.CharField(max_length=64)),
                ('funcao', models.CharField(blank=True, choices=[('aluno', 'aluno'), ('professor', 'professor')], max_length=20)),
                ('linkLusofona', models.URLField(blank=True)),
                ('linkLinkedin', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PontuacaoQuizz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('apelido', models.CharField(max_length=30)),
                ('pontuacao', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tecnologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('acronimo', models.CharField(blank=True, max_length=20)),
                ('ano', models.DateField()),
                ('criador', models.CharField(max_length=20)),
                ('logo', models.ImageField(upload_to='')),
                ('link', models.URLField()),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tfc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField(default=2021)),
                ('titulo', models.CharField(max_length=50)),
                ('resumo', models.CharField(max_length=1000)),
                ('imagem', models.ImageField(upload_to='')),
                ('relatorio', models.CharField(max_length=1000)),
                ('linkGithub', models.CharField(max_length=1000)),
                ('video', models.CharField(max_length=1000)),
                ('autor', models.ManyToManyField(related_name='autorTFC', to='portfolio.pessoa')),
                ('orientadores', models.ManyToManyField(related_name='orientadores', to='portfolio.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.TextField(max_length=5000)),
                ('imagem', models.ImageField(upload_to='projetos')),
                ('ano', models.DateField()),
                ('linkGithub', models.CharField(blank=True, max_length=1000)),
                ('linkYoutube', models.CharField(blank=True, max_length=1000)),
                ('participantes', models.ManyToManyField(to='portfolio.pessoa')),
                ('tecnologias', models.ManyToManyField(to='portfolio.tecnologia')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('descricao', models.CharField(max_length=1000)),
                ('link', models.CharField(blank=True, max_length=1000)),
                ('imagem', models.ImageField(upload_to='')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor', to='portfolio.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Competencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=1000)),
                ('disciplinas', models.ManyToManyField(to='portfolio.cadeira')),
                ('projetos', models.ManyToManyField(to='portfolio.projeto')),
            ],
        ),
        migrations.AddField(
            model_name='cadeira',
            name='docente_teorica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.pessoa'),
        ),
        migrations.AddField(
            model_name='cadeira',
            name='docentes_praticas',
            field=models.ManyToManyField(related_name='caderias', to='portfolio.pessoa'),
        ),
        migrations.AddField(
            model_name='cadeira',
            name='linguagens',
            field=models.ManyToManyField(blank=True, to='portfolio.tecnologia'),
        ),
        migrations.AddField(
            model_name='cadeira',
            name='projetos',
            field=models.ManyToManyField(blank=True, to='portfolio.projeto'),
        ),
    ]
