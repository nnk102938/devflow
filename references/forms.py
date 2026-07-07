from django import forms
from .models import Reference,Flow


# ───────────────────────────────────────────────────────────
# リファレンスフォーム
# ───────────────────────────────────────────────────────────
class ReferenceForm(forms.ModelForm):
    
    class Meta:
        model = Reference

        fields = [
            "title",
            "description",
            "code",
            "category",
        ]

        labels = {
            "title": "リファレンス名",
            "description": "説明",
            "code": "コード",
            "category": "カテゴリ",
        }

        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "リファレンス名を入力"
                }),
            
            "description": forms.Textarea(attrs={
                "rows": 5,
                "placeholder": "説明を入力"
                }),
            
            "code": forms.Textarea(attrs={
                "rows": 6,
                "placeholder": "コードを入力"
                }),
        }
# ───────────────────────────────────────────────────────────



# ───────────────────────────────────────────────────────────
# フローフォーム
# ───────────────────────────────────────────────────────────
class FlowForm(forms.ModelForm):    
    class Meta:
        model = Flow

        fields = [
            "title",
            "description",
        ]

        labels = {
            "title": "フロー名",
            "description": "概要",
        }

        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "フロー名を入力"
                }),
            
            "description": forms.Textarea(attrs={
                "rows": 6,
                "placeholder": "概要を入力"
                }),
        }
# ───────────────────────────────────────────────────────────
