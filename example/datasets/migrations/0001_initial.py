# Generated by Django 4.1.5 on 2023-07-24 07:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="RADataSet",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="助研数据集ID",
                    ),
                ),
                ("number", models.IntegerField(unique=True, verbose_name="助研数据集编号")),
                ("title", models.CharField(max_length=100, verbose_name="助研数据集标题")),
                ("description", models.TextField(verbose_name="助研数据集描述")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="更新时间"),
                ),
            ],
            options={
                "verbose_name": "助研数据集",
            },
        ),
        migrations.CreateModel(
            name="RADataRecord",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="助研数据ID",
                    ),
                ),
                ("number", models.IntegerField(unique=True, verbose_name="助研数据编号")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="更新时间"),
                ),
                (
                    "dataset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="entries",
                        to="datasets.radataset",
                        verbose_name="关联数据集",
                    ),
                ),
            ],
            options={
                "verbose_name": "助研数据",
            },
        ),
    ]
