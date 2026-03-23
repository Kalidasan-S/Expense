document.addEventListener("DOMContentLoaded", function () {

    const pieCtx = document.getElementById("expensePie");
    if (pieCtx && expenseLabels.length > 0) {
        new Chart(pieCtx, {
            type: "pie",
            data: {
                labels: expenseLabels,
                datasets: [{
                    data: expenseValues,
                    backgroundColor: [
                        "#0d6efd",
                        "#dc3545",
                        "#ffc107",
                        "#198754",
                        "#6f42c1"
                    ]
                }]
            }
        });
    }
});
