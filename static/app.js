let allTestCases = [];

document.addEventListener("DOMContentLoaded", () => {
    fetchSummary();
});

async function fetchSummary() {
    try {
        const res = await fetch("/api/summary");
        const data = await res.json();

        if (data.status === "success") {
            const metrics = data.metrics;
            document.getElementById("clientName").innerText = data.client_name;
            document.getElementById("clientSystem").innerText = data.target_system;

            document.getElementById("passRateVal").innerText = metrics.pass_rate + "%";
            document.getElementById("totalTestsVal").innerText = metrics.total_tests;
            document.getElementById("passCount").innerText = metrics.passed + " Passed";
            document.getElementById("failCount").innerText = metrics.failed + " Failed";
            document.getElementById("latencyVal").innerText = metrics.avg_response_time_ms + "ms";
            
            if (metrics.last_executed) {
                document.getElementById("lastRunTime").innerText = "Last Run: " + metrics.last_executed;
            }

            allTestCases = metrics.test_cases || [];
            renderTable(allTestCases);
        }
    } catch (err) {
        console.error("Error fetching summary:", err);
    }
}

function renderTable(testCases) {
    const tbody = document.getElementById("testTableBody");
    tbody.innerHTML = "";

    testCases.forEach(tc => {
        const isPass = tc.status === "PASSED";
        const tagClass = isPass ? "status-tag passed" : "status-tag failed";

        const tr = document.createElement("tr");
        tr.innerHTML = `
            <td style="font-weight: 700; color: var(--accent-blue);">${tc.id}</td>
            <td style="font-weight: 600;">${tc.name}</td>
            <td><span style="color: var(--text-secondary); font-size: 0.85rem;">${tc.category}</span></td>
            <td><span class="${tagClass}">${tc.status}</span></td>
            <td style="font-weight: 600;">${tc.duration_ms} ms</td>
            <td style="color: var(--text-secondary); font-size: 0.85rem;">${tc.details}</td>
        `;
        tbody.appendChild(tr);
    });
}

function filterTests(status) {
    document.querySelectorAll(".filter-btn").forEach(btn => btn.classList.remove("active"));
    event.target.classList.add("active");

    if (status === "ALL") {
        renderTable(allTestCases);
    } else {
        const filtered = allTestCases.filter(tc => tc.status === status);
        renderTable(filtered);
    }
}

async function triggerTests() {
    const btn = document.getElementById("runBtn");
    btn.disabled = true;
    btn.innerHTML = `<span>⏳</span> Running Suite...`;

    try {
        const res = await fetch("/api/run-tests", { method: "POST" });
        const data = await res.json();
        await fetchSummary();
        alert("✅ Test Suite Executed Successfully!");
    } catch (err) {
        alert("Failed to run test suite.");
    } finally {
        btn.disabled = false;
        btn.innerHTML = `<span>▶</span> Trigger Test Suite`;
    }
}

function exportReport() {
    window.open("/api/report/html", "_blank");
}
