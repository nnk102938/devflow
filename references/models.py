from django.db import models


# ───────────────────────────────────────────────────────────
# カテゴリ
# ───────────────────────────────────────────────────────────
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 
        # Categoryを一覧表示したときにnameの値を表示
# ───────────────────────────────────────────────────────────


# ───────────────────────────────────────────────────────────
# リファレンス
# ───────────────────────────────────────────────────────────
class Reference(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    code = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE  
          # CASCADE:親(Category)が削除されたら子(Reference)も削除する
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
# ───────────────────────────────────────────────────────────
    

# ───────────────────────────────────────────────────────────
# フロー
# ───────────────────────────────────────────────────────────
class Flow(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
# ───────────────────────────────────────────────────────────


# ───────────────────────────────────────────────────────────
# フローステップ
# ───────────────────────────────────────────────────────────
class FlowStep(models.Model):
    flow = models.ForeignKey(
        Flow,
        on_delete=models.CASCADE,
        related_name="steps"
        )

    reference = models.ForeignKey(
        Reference,
        on_delete=models.CASCADE
        )
    
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ["order"]

        # 同じフロー内でStep番号を重複させない
        constraints = [
            models.UniqueConstraint(
                fields=["flow", "order"],
                name="unique_flow_order",
            )
        ]

    def __str__(self):
        return f"{self.flow.title} - Step{self.order}"
# ───────────────────────────────────────────────────────────
