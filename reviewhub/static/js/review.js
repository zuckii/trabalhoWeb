/* static/js/review.js */

document.addEventListener('DOMContentLoaded', () => {
    // --- Elementos ---
    const stars = document.querySelectorAll('.star');
    const starContainer = document.getElementById('star-container');
    const hiddenInput = document.getElementById('rating-input');
    const ratingText = document.getElementById('rating-text');
    
    const textarea = document.getElementById('review-text');
    const counter = document.getElementById('char-counter');
    const form = document.getElementById('reviewForm');

    let currentRating = 0;

    // =================================================================
    // 1. LÓGICA DAS ESTRELAS
    // =================================================================
    stars.forEach((star) => {
        // Mouse Move
        star.addEventListener('mousemove', (e) => {
            const rect = star.getBoundingClientRect();
            const width = rect.width;
            const x = e.clientX - rect.left;
            
            const isHalf = x < (width / 2);
            const starValue = parseInt(star.getAttribute('data-value'));
            
            const tempRating = isHalf ? starValue - 0.5 : starValue;
            updateStarsVisual(tempRating);
        });

        // Clique
        star.addEventListener('click', (e) => {
            const rect = star.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const isHalf = x < (rect.width / 2);
            const starValue = parseInt(star.getAttribute('data-value'));
            
            currentRating = isHalf ? starValue - 0.5 : starValue;
            
            hiddenInput.value = currentRating;
            updateRatingText(currentRating); // Atualiza texto e remove erro
        });
    });

    if (starContainer) {
        starContainer.addEventListener('mouseleave', () => {
            updateStarsVisual(currentRating);
        });
    }

    // =================================================================
    // 2. CONTADOR DE CARACTERES
    // =================================================================
    if (textarea && counter) {
        textarea.addEventListener('input', function() {
            const currentLength = this.value.length;
            const maxLength = 1000;
            counter.textContent = `${currentLength} / ${maxLength}`;
            
            if (currentLength >= maxLength) {
                counter.style.color = 'red';
            } else {
                counter.style.color = '';
            }
        });
    }

    // =================================================================
    // 3. VALIDAÇÃO DO FORMULÁRIO (COM REINÍCIO DE ANIMAÇÃO)
    // =================================================================
    if (form) {
        form.addEventListener('submit', function(e) {
            const ratingValue = parseFloat(hiddenInput.value);

            // Se a nota for inválida (0 ou menor que 0.5)
            if (!ratingValue || ratingValue < 0.5) {
                e.preventDefault(); // Bloqueia envio

                // --- MUDANÇA AQUI: Reiniciar a animação ---
                
                // 1. Remove a classe se ela já existir
                ratingText.classList.remove('text-error');

                // 2. Força um "reflow" (uma atualização de layout rápida do navegador).
                // Apenas ler uma propriedade de dimensão, como offsetWidth, força isso.
                // O 'void' é apenas para descartar o valor retornado, não afeta a lógica.
                void ratingText.offsetWidth; 

                // 3. Re-adiciona a classe para disparar a animação novamente
                ratingText.textContent = "Por favor, selecione uma nota!";
                ratingText.classList.add('text-error');
                
                // Rola a tela para garantir visualização
                ratingText.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        });
    }

    // =================================================================
    // 4. FUNÇÕES AUXILIARES
    // =================================================================
    function updateStarsVisual(rating) {
        stars.forEach((star, index) => {
            const starValue = index + 1;
            star.classList.remove('fa-solid', 'fa-star-half-stroke', 'fa-regular');
            
            if (rating >= starValue) {
                star.classList.add('fa-solid', 'fa-star');
                star.style.color = 'var(--gold)';
            } else if (rating >= starValue - 0.5) {
                star.classList.add('fa-solid', 'fa-star-half-stroke');
                star.style.color = 'var(--gold)';
            } else {
                star.classList.add('fa-regular', 'fa-star');
                star.style.color = 'var(--gray-star)';
            }
        });
    }

    function updateRatingText(rating) {
        // Remove a classe de erro ao selecionar uma nota válida
        ratingText.classList.remove('text-error');

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