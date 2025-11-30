document.addEventListener('DOMContentLoaded', () => {
    const inputs = document.querySelectorAll('.stars input');
    const ratingText = document.getElementById('rating-text');

    if(inputs.length > 0) {
        inputs.forEach(input => {
            input.addEventListener('change', () => {
                const label = document.querySelector(`label[for="${input.id}"]`);
                if(label) {
                    ratingText.textContent = label.getAttribute('title');
                    ratingText.style.color = '#eab308'; // Amarelo escuro para leitura no branco
                }
            });
        });
    }
});