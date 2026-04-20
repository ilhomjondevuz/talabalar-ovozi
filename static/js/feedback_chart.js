document.addEventListener("DOMContentLoaded", function () {
    const ctx = document.getElementById('ratingChart');
    const data = {
        labels: ['Yomon','O‘rtacha','Yaxshi','Zo‘r','A’lo'],
        datasets: [{
            label: 'Talabalar bahosi',
            data: window.ratingCounts,   // Template’dan kelgan global o‘zgaruvchi
            backgroundColor: ['#dc3545','#fd7e14','#ffc107','#0d6efd','#198754']
        }]
    };
    new Chart(ctx, { type: 'bar', data: data });
});
