// Select DOM elements
const knob = document.getElementById('knob');
const categoryDisplay = document.getElementById('category-display');

// Audio setup
const audio = new Audio('../assets/audio/beep.mp3');
audio.volume = 0.5; // Default volume (50%)

// Categories for the knob
const categories = ['Art', 'P2P', 'NFTs', 'Gaming'];

let isDragging = false; // Tracks whether the knob is being dragged

// Handle knob dragging for rotation
knob.addEventListener('mousedown', () => {
    isDragging = true; // Start dragging
});

document.addEventListener('mouseup', () => {
    isDragging = false; // Stop dragging
});

document.addEventListener('mousemove', (e) => {
    if (isDragging) {
        const rect = knob.getBoundingClientRect();
        const centerX = rect.left + rect.width / 2;
        const centerY = rect.top + rect.height / 2;

        // Calculate the angle of rotation
        const angle = Math.atan2(e.clientY - centerY, e.clientX - centerX) 
* (180 / Math.PI) + 180;
        knob.style.transform = `rotate(${angle}deg)`; // Rotate knob

        // Determine category based on angle
        const categoryIndex = Math.floor((angle / 360) * 
categories.length) % categories.length;
        categoryDisplay.innerText = `Category: 
${categories[categoryIndex]}`;
    }
});

// Play sound when knob is clicked
knob.addEventListener('click', () => {
    audio.play();
});

// Optional: Volume control slider
const volumeSlider = document.getElementById('volume-slider');
if (volumeSlider) {
    volumeSlider.addEventListener('input', (e) => {
        audio.volume = e.target.value / 100; // Adjust volume
    });
}

