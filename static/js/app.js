// OpenVault Front-end Interactions
document.addEventListener("DOMContentLoaded", () => {
    console.log("[OpenVault] Initializing client application...");

    const searchInput = document.getElementById("search-input");
    if (searchInput) {
        searchInput.addEventListener("input", (e) => {
            const term = e.target.value.toLowerCase();
            const rows = document.querySelectorAll("#entries-tbody tr");
            rows.forEach(row => {
                const text = row.innerText.toLowerCase();
                row.style.display = text.includes(term) ? "" : "none";
            });
        });
    }

    // Password visibility toggles
    document.addEventListener("click", (e) => {
        if (e.target.classList.contains("toggle-pw-btn")) {
            const input = e.target.previousElementSibling;
            if (input && input.type === "password") {
                input.type = "text";
                e.target.innerText = "Hide";
            } else if (input) {
                input.type = "password";
                e.target.innerText = "Show";
            }
        }
    });
});
