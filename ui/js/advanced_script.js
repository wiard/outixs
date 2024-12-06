document.addEventListener("DOMContentLoaded", () => {
    const relayList = document.getElementById("relay-list");
    const searchInput = document.getElementById("search-tags");

    searchInput.addEventListener("input", () => {
        const query = searchInput.value.toLowerCase();
        const items = relayList.querySelectorAll("li");
        items.forEach(item => {
            const tags = item.dataset.tags.toLowerCase();
            item.style.display = tags.includes(query) ? "block" : "none";
        });
    });
});

