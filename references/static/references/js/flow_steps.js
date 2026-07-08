// フローフォームの共通JS

console.log("flow_steps loaded");

document.addEventListener("DOMContentLoaded", function () {

    // step設定 ──────────────────────────────────────────────────
    const container = document.getElementById("step-container");
    const button = document.getElementById("add-step");

    // 他のページで誤って読み込んでも落ちない
    if (!container || !button) {
        return;
    }

    button.addEventListener("click", function () {

        // 最後のstepを取得
        const lastStep = container.lastElementChild;

        // 複製
        const newStep = lastStep.cloneNode(true);

        // step番号を更新
        const stepNumber = container.children.length + 1;
        newStep.querySelector("h3").textContent = `Step${stepNumber}`;

        // 選択をリセット
        newStep.querySelector("select").selectedIndex = 0;

        // 追加
        container.appendChild(newStep);
    });
    // ───────────────────────────────────────────────────────────


    // 削除ボタン ─────────────────────────────────────────────────
    document.addEventListener("click", function (e) {

        const btn = e.target.closest(".step-delete");
        if (!btn) return;

        const steps = document.querySelectorAll(".step-item");

        if (steps.length === 1) {
            return;
        }

        btn.closest(".step-item").remove();

        renumberSteps();

    });
    // ───────────────────────────────────────────────────────────


    // ↑ボタン ────────────────────────────────────────────────────
    document.addEventListener("click", function (e) {

        const btn = e.target.closest(".step-up");
        if (!btn) return;

        const step = btn.closest(".step-item");
        const prev = step.previousElementSibling;

        if (prev) {
            container.insertBefore(step, prev);
            renumberSteps();
        }
    });
    // ───────────────────────────────────────────────────────────


    // ↓ボタン ────────────────────────────────────────────────────
    document.addEventListener("click", function (e) {

        const btn = e.target.closest(".step-down");
        if (!btn) return;

        const step = btn.closest(".step-item");
        const next = step.nextElementSibling;

        if (next) {
            container.insertBefore(next, step);
            renumberSteps();
        }
    });
    // ───────────────────────────────────────────────────────────


    // stepの番号を振り直す────────────────────────────────────────
    function renumberSteps() {
        container.querySelectorAll(".step-item h3")
            .forEach((h3, index) => {
                h3.textContent = `Step${index + 1}`;
            });
    }
    // ───────────────────────────────────────────────────────────

});