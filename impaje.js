// Initialize the map with default zoom control
const map = L.map('map', {
    zoomControl: true // Keep zoom control enabled
}).setView([20.5937, 78.9629], 5); // Center on India

// Add OpenStreetMap tiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Fetch heritage sites data
fetch('sites.json')
    .then(response => response.json())
    .then(data => {
        data.forEach(site => {
            const marker = L.marker([site.lat, site.lng])
                .addTo(map)
                .bindTooltip(`<b>${site.name}</b><br>${site.info}`, {
                    permanent: false, // Tooltip only visible on hover
                    direction: 'top',
                    opacity: 0.8
                })
                .bindPopup(`<b>${site.name}</b><br>${site.info}`)
                .on('click', () => {
                    // Open the blog site in a new tab
                    window.open(`02_02blogSite.html#${site.name.toLowerCase().replace(/\s+/g, '-')}`, '_blank');
                });
        });
    })
    .catch(error => console.error('Error fetching data:', error));
