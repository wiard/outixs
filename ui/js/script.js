// Update network status dynamically
const networkStatus = document.getElementById('network-status');
function updateNetworkStatus(status) {
    networkStatus.className = status;
    networkStatus.textContent =
        status === 'connected' ? 'Connected' :
        status === 'syncing' ? 'Syncing...' :
        'Disconnected';
}

// Example usage
updateNetworkStatus('connected');

// Add interactivity to tiles
const tiles = document.querySelectorAll('.tile');
tiles.forEach(tile => {
    tile.addEventListener('click', () => {
        alert('Tile clicked!');
    });
});

// Add interactivity to side panel buttons
const toolButtons = document.querySelectorAll('.tool-btn');
toolButtons.forEach(button => {
    button.addEventListener('click', () => {
        alert(`${button.textContent} selected!`);
    });
});

