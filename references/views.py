from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Reference,Flow,FlowStep
from .forms import ReferenceForm,FlowForm


# ───────────────────────────────────────────────────────────
# 一覧表示
# ───────────────────────────────────────────────────────────
def top(request):

    # 各モデルに保存されている全データを取得
    references = Reference.objects.all()
    flows = Flow.objects.all()

    return render(
        request,
        "references/top.html",
        {
            "references": references,
            "flows":flows,
            }
        )
# ───────────────────────────────────────────────────────────


# ───────────────────────────────────────────────────────────
# フロー詳細
# ───────────────────────────────────────────────────────────
def flow(request, pk):

    flow = get_object_or_404(
        Flow,
        pk=pk
    )

    steps = FlowStep.objects.filter(
        flow=flow
    ).select_related("reference")

    return render(
        request,
        "references/flow.html",
        {
            "flow":flow,
            "steps":steps,
            }
    )

# ───────────────────────────────────────────────────────────
# フロー登録
# ───────────────────────────────────────────────────────────
def flow_create(request):
    
    if request.method == "POST":
        form = FlowForm(request.POST)
        
        if form.is_valid():
            flow = form.save()

            steps = [
                form.cleaned_data["step1"],
                form.cleaned_data["step2"],
                form.cleaned_data["step3"],
            ]

            order = 1

            for ref in steps:
                if ref:
                    FlowStep.objects.create(
                        flow=flow,
                        reference=ref,
                        order=order,
                    )
                    order += 1

            return redirect("flow", pk=flow.pk)
        
    else:
        form = FlowForm()

    return render(
        request, 
        "references/flow_create.html",
        {"form": form}
        )

# ───────────────────────────────────────────────────────────
# フロー編集
# ───────────────────────────────────────────────────────────
def flow_update(request,pk):

    flow = get_object_or_404(
        Flow,
        pk=pk
        )
    
    if request.method == "POST":
        form = FlowForm(
            request.POST,
            instance=flow # 既存データを編集
            )
        
        if form.is_valid():
            flow = form.save()

            FlowStep.objects.filter(flow=flow).delete()

            steps = [
                form.cleaned_data["step1"],
                form.cleaned_data["step2"],
                form.cleaned_data["step3"],
            ]

            order = 1

            for ref in steps:
                if ref:
                    FlowStep.objects.create(
                        flow=flow,
                        reference=ref,
                        order=order,
                    )
                    order += 1

            return redirect("flow", pk=flow.pk)
        
    else:
        steps = FlowStep.objects.filter(
            flow=flow
        ).order_by("order")

        initial = {}

        if len(steps) > 0:
            initial["step1"] = steps[0].reference

        if len(steps) > 1:
            initial["step2"] = steps[1].reference
        
        if len(steps) > 2:
            initial["step3"] = steps[2].reference

        form = FlowForm(
            instance=flow,
            initial=initial,
        )

    return render(
        request,
        "references/flow_update.html",
        {"form": form}
        )

# ───────────────────────────────────────────────────────────
# フロー削除
# ───────────────────────────────────────────────────────────
def flow_delete(request,pk):
    
    flow = get_object_or_404(
        Flow,
        pk=pk
        )
    
    # GET：確認画面、POST：削除実行
    
    if request.method == "POST":
        flow.delete()
        return redirect("top")

    return render(
        request,
        "references/flow_delete.html",
        {"flow":flow}
        )
# ───────────────────────────────────────────────────────────



# ───────────────────────────────────────────────────────────
# 検索
# ───────────────────────────────────────────────────────────
def search(request):
    query = request.GET.get("q")

    references = Reference.objects.all()

    if query:
        references = references.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(code__icontains=query)
        )

    return render(
        request,
        "references/search.html",
        {
            "references": references,
            "query": query,
        },
    )
# ───────────────────────────────────────────────────────────


# ───────────────────────────────────────────────────────────
# お気に入り
# ───────────────────────────────────────────────────────────
def favorites(request):

    references = Reference.objects.all()
        # Referenceモデルに保存されている全データを取得

    query = request.GET.get("q")

    return render(
        request,
        "references/favorites.html",
        {
            "references": references,
            }
        )
# ───────────────────────────────────────────────────────────



# ───────────────────────────────────────────────────────────
# リファレンス詳細
# ───────────────────────────────────────────────────────────
def detail(request,pk):

    reference = get_object_or_404(
        Reference,
        pk = pk  #モデルのpkフィールドにURLから来たpkの値を入れる
        )
    
    return render(
        request, 
        "references/detail.html",
        {"reference": reference}
        )

# ───────────────────────────────────────────────────────────
# リファレンス登録
# ───────────────────────────────────────────────────────────
def create(request):
    
    if request.method == "POST":
        form = ReferenceForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("top")
        
    else:
        form = ReferenceForm()

    return render(
        request, 
        "references/create.html",
        {"form": form}
        )

# ───────────────────────────────────────────────────────────
# リファレンス編集
# ───────────────────────────────────────────────────────────
def update(request,pk):

    reference = get_object_or_404(
        Reference,
        pk=pk
        )
    
    if request.method == "POST":
        form = ReferenceForm(
            request.POST,
            instance=reference # 既存データを編集
            )
        
        if form.is_valid():
            form.save()
            return redirect("detail", pk=reference.pk)
        
    else:
        form = ReferenceForm(instance=reference)

    return render(
        request,
        "references/update.html",
        {"form": form}
        )

# ───────────────────────────────────────────────────────────
# リファレンス削除
# ───────────────────────────────────────────────────────────
def delete(request,pk):
    
    reference = get_object_or_404(
        Reference,
        pk=pk
        )
    
    # GET：確認画面、POST：削除実行
    
    if request.method == "POST":
        reference.delete()
        return redirect("top")

    return render(
        request,
        "references/delete.html",
        {"reference":reference}
        )
# ───────────────────────────────────────────────────────────
