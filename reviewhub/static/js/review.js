document.addEventListener('DOMContentLoaded', () => {
    const stars = document.querySelectorAll('.star');
    const starContainer = document.getElementById('star-container');
    const hiddenInput = document.getElementById('rating-input');
    const ratingText = document.getElementById('rating-text');
    
    let currentRating = 0;

    stars.forEach((star) => {
        // Lógica de Mouse Move (Detecta metade ou cheia)
        star.addEventListener('mousemove', (e) => {
            const rect = star.getBoundingClientRect();
            const width = rect.width;
            const x = e.clientX - rect.left;
            
            // Mouse na esquerda (< 50%) = Meia estrela
            const isHalf = x < (width / 2);
            const starValue = parseInt(star.getAttribute('data-value'));
            
            const tempRating = isHalf ? starValue - 0.5 : starValue;
            updateStarsVisual(tempRating);
        });

        // Lógica de Clique (Confirma a nota)
        star.addEventListener('click', (e) => {
            const rect = star.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const isHalf = x < (rect.width / 2);
            const starValue = parseInt(star.getAttribute('data-value'));
            
            currentRating = isHalf ? starValue - 0.5 : starValue;
            
            hiddenInput.value = currentRating;
            updateRatingText(currentRating);
            
            // REMOVIDO: A parte que fazia a animação de "scale/zoom"
        });
    });

    // Saiu da área das estrelas? Volta para a nota confirmada
    starContainer.addEventListener('mouseleave', () => {
        updateStarsVisual(currentRating);
    });

    function updateStarsVisual(rating) {
        stars.forEach((star, index) => {
            const starValue = index + 1;

            // Limpa classes anteriores
            star.classList.remove('fa-solid', 'fa-star-half-stroke', 'fa-regular');
            
            if (rating >= starValue) {
                // Cheia
                star.classList.add('fa-solid', 'fa-star');
                star.style.color = 'var(--gold)';
            } else if (rating >= starValue - 0.5) {
                // Meia
                star.classList.add('fa-solid', 'fa-star-half-stroke');
                star.style.color = 'var(--gold)';
            } else {
                // Vazia
                star.classList.add('fa-regular', 'fa-star');
                star.style.color = 'var(--gray-star)';
            }
        });
    }

    function updateRatingText(rating) {
        if (rating > 0) {
            ratingText.textContent = rating.toFixed(1);
            ratingText.style.color = '#eab308';
            ratingText.style.fontWeight = 'bold';
        } else {
            ratingText.textContent = "Selecione uma nota";
            ratingText.style.color = 'var(--text-muted)';
            ratingText.style.fontWeight = 'normal';
        }
    }
});