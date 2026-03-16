from django.db import models


class BriefResponse(models.Model):
    PROJECT_TYPE_CHOICES = [
        ("landing", "Лендінг"),
        ("business_card", "Сайт-візитка"),
        ("corporate", "Корпоративний сайт"),
        ("catalog", "Каталог продукції"),
        ("store", "Інтернет-магазин"),
    ]

    DESIGN_STYLE_CHOICES = [
        ("minimal", "Мінімалістичний"),
        ("business", "Діловий"),
        ("bright", "Яскравий"),
        ("modern", "Сучасний"),
    ]

    full_name = models.CharField(max_length=255, verbose_name="ПІБ")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")
    company_name = models.CharField(max_length=255, verbose_name="Назва компанії")
    company_activity = models.CharField(max_length=255, verbose_name="Сфера діяльності")

    project_type = models.CharField(
        max_length=30,
        choices=PROJECT_TYPE_CHOICES,
        verbose_name="Тип проєкту"
    )
    project_description = models.TextField(verbose_name="Опис проєкту")
    target_audience = models.TextField(verbose_name="Цільова аудиторія")
    site_goals = models.TextField(verbose_name="Мета сайту")
    required_pages = models.TextField(verbose_name="Потрібні розділи сайту")
    required_features = models.TextField(verbose_name="Потрібні функції")
    design_style = models.CharField(
        max_length=30,
        choices=DESIGN_STYLE_CHOICES,
        verbose_name="Стиль дизайну"
    )
    color_preferences = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Побажання щодо кольорів"
    )
    content_ready = models.BooleanField(default=False, verbose_name="Чи готовий контент")
    deadline = models.CharField(max_length=100, blank=True, verbose_name="Терміни")
    budget = models.CharField(max_length=100, blank=True, verbose_name="Бюджет")
    additional_notes = models.TextField(blank=True, verbose_name="Додаткові побажання")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")

    class Meta:
        verbose_name = "Відповідь на бриф"
        verbose_name_plural = "Відповіді на бриф"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.company_name} — {self.full_name}"