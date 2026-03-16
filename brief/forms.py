from django import forms
from .models import BriefResponse


class BriefResponseForm(forms.ModelForm):
    class Meta:
        model = BriefResponse
        fields = [
            "full_name",
            "email",
            "phone",
            "company_name",
            "company_activity",
            "project_type",
            "project_description",
            "target_audience",
            "site_goals",
            "required_pages",
            "required_features",
            "design_style",
            "color_preferences",
            "content_ready",
            "deadline",
            "budget",
            "additional_notes",
        ]
        widgets = {
            "project_description": forms.Textarea(attrs={"rows": 4}),
            "target_audience": forms.Textarea(attrs={"rows": 3}),
            "site_goals": forms.Textarea(attrs={"rows": 3}),
            "required_pages": forms.Textarea(attrs={"rows": 3}),
            "required_features": forms.Textarea(attrs={"rows": 3}),
            "additional_notes": forms.Textarea(attrs={"rows": 4}),
        }
        labels = {
            "full_name": "ПІБ",
            "email": "Email",
            "phone": "Телефон",
            "company_name": "Назва компанії",
            "company_activity": "Сфера діяльності",
            "project_type": "Тип проєкту",
            "project_description": "Коротко опишіть проєкт",
            "target_audience": "Цільова аудиторія",
            "site_goals": "Яка мета створення сайту?",
            "required_pages": "Які розділи повинні бути на сайті?",
            "required_features": "Які функції потрібні?",
            "design_style": "Бажаний стиль дизайну",
            "color_preferences": "Побажання щодо кольорів",
            "content_ready": "Чи є готовий контент?",
            "deadline": "Терміни виконання",
            "budget": "Орієнтовний бюджет",
            "additional_notes": "Додаткові побажання",
        }