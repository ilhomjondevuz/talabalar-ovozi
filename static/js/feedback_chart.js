document.addEventListener("DOMContentLoaded", function () {
    const ctx = document.getElementById('ratingChart');

    const data = {
        labels: ['Yomon','O‘rtacha','Yaxshi','Zo‘r','A’lo'],
        datasets: [{
            label: 'Talabalar bahosi',
            data: window.ratingCounts,
            backgroundColor: ['#dc3545','#fd7e14','#ffc107','#0d6efd','#198754']
        }]
    };

    const options = {
        responsive: true,   // Mobil uchun moslashadi
        maintainAspectRatio: false, // Ekran o‘lchamiga moslashadi
        plugins: {
            legend: {
                position: 'bottom', // Mobil ekranda pastda ko‘rinadi
            }
        }
    };

    new Chart(ctx, { type: 'bar', data: data, options: options });
});
