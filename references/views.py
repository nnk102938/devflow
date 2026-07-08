from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Reference,Flow,FlowStep
from .forms import ReferenceForm,FlowForm
from django.contrib import messages


# ───────────────────────────────────────────────────────────
# 共通処理
# ───────────────────────────────────────────────────────────
def save_flow_steps(flow, step_ids):
    for i, ref_id in enumerate(step_ids):
        if ref_id:
            FlowStep.objects.create(
                flow=flow,
                reference_id=ref_id,
                order=i + 1,
            )
# ───────────────────────────────────────────────────────────


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

            save_flow_steps(
                flow,
                request.POST.getlist("step_reference")
            )

            messages.success(request,"フローを作成しました。")
            return redirect("flow", pk=flow.pk)
        
    else:
        form = FlowForm()


    references= Reference.objects.all()

    return render(
        request, 
        "references/flow_create.html",
        {
            "form": form,
            "references":references,
            "steps":[None],
            }
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

            save_flow_steps(
                flow,
                request.POST.getlist("step_reference")
            )

            messages.success(request, "フローを更新しました。")
            return redirect("flow", pk=flow.pk)
        
    else:
        steps = FlowStep.objects.filter(
            flow=flow
        ).order_by("order")

        form = FlowForm(
            instance=flow,
        )

    return render(
        request,
        "references/flow_update.html",
        {
            "form": form,
            "steps": steps,
            "references": Reference.objects.all(),
            },
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
        messages.success(request, "フローを削除しました。")
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
        pk = pk  #モデルのpkフィールド = URLから来たpkの値
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
            messages.success(request,"リファレンスを作成しました。")
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
            messages.success(request, "リファレンスを更新しました。")
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
        messages.success(request, "リファレンスを削除しました。")
        return redirect("top")

    return render(
        request,
        "references/delete.html",
        {"reference":reference}
        )
# ───────────────────────────────────────────────────────────
