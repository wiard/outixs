document.addEventListener("DOMContentLoaded", function () {
    // Relay Form Handling
    const form = document.getElementById("listener-form");
    const relayList = document.getElementById("relay-list");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        const relayUrl = document.getElementById("relay-url").value.trim();
        const tags = document.getElementById("tags").value.split(",").map(tag => tag.trim());

        if (relayUrl && tags.length > 0) {
            addRelayToUI(relayUrl, tags);
        } else {
            alert("Please provide a relay URL and at least one tag.");
        }

        form.reset();
    });

    function addRelayToUI(relayUrl, tags) {
        const relayItem = document.createElement("li");
        relayItem.dataset.relay = relayUrl;

        const tagSpan = document.createElement("span");
        tagSpan.className = "tags";
        tagSpan.textContent = `Tags: ${tags.join(", ")}`;

        relayItem.textContent = `Relay: ${relayUrl} `;
        relayItem.appendChild(tagSpan);
        relayList.appendChild(relayItem);

        simulateRelayStatus(relayUrl);
    }

    // Simulate Relay Updates
    function simulateRelayStatus(relayUrl) {
        const statuses = ["active", "inactive", "overloaded"];
        setInterval(() => {
            const randomStatus = statuses[Math.floor(Math.random() * statuses.length)];
            updateRelayStatus(relayUrl, randomStatus);
        }, 5000);
    }

    function updateRelayStatus(relayUrl, status) {
        const relayItem = document.querySelector(`li[data-relay="${relayUrl}"]`);
        if (relayItem) {
            relayItem.querySelector(".tags").textContent += ` | Status: ${status}`;
        }
    }

    // Dynamic Tagging and Searching
    const searchField = document.getElementById("search-tags");
    searchField.addEventListener("input", function () {
        const searchValue = searchField.value.trim().toLowerCase();
        const relayItems = relayList.querySelectorAll("li");

        relayItems.forEach(item => {
            const tags = item.querySelector(".tags").textContent.toLowerCase();
            if (tags.includes(searchValue)) {
                item.style.display = "";
            } else {
                item.style.display = "none";
            }
        });
    });
});

