document.addEventListener('DOMContentLoaded', () => {
    // Elementos principais
    const stars = document.querySelectorAll('.star');
    const starContainer = document.getElementById('star-container');
    const hiddenInput = document.getElementById('rating-input');
    const ratingText = document.getElementById('rating-text');
    
    const textarea = document.getElementById('review-text');
    const counter = document.getElementById('char-counter');
    const form = document.getElementById('reviewForm');

    let currentRating = 0;

    const isEditMode = textarea.value.trim().length > 0;

    // Se houver um review existente, carregar os valores
    if (isEditMode) {
        // Carregar a nota existente
        const ratingValue = parseFloat(ratingText.textContent);
        if (!isNaN(ratingValue) && ratingValue > 0) {
            currentRating = ratingValue;
            hiddenInput.value = currentRating;
            updateStarsVisual(currentRating);
            // Atualiza o texto da nota
            ratingText.style.color = '#eab308';
            ratingText.style.fontWeight = 'bold';
        }
    }
    // Eventos para cada estrela
    stars.forEach((star) => {
        // Passar o mouse
        star.addEventListener('mousemove', (e) => {
            const rect = star.getBoundingClientRect();
            const width = rect.width;
            const x = e.clientX - rect.left;
    
            const isHalf = x < (width / 2);
            const starValue = parseInt(star.getAttribute('data-value'));
            
            const tempRating = isHalf ? starValue - 0.5 : starValue;
            updateStarsVisual(tempRating);
        });

        // Clicar na estrela
        star.addEventListener('click', (e) => {
            const rect = star.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const isHalf = x < (rect.width / 2);
            const starValue = parseInt(star.getAttribute('data-value'));
            
            currentRating = isHalf ? starValue - 0.5 : starValue;
            
            hiddenInput.value = currentRating;
            updateRatingText(currentRating);
        });
    });
    // Ao sair do container das estrelas, restaurar a visualização da nota selecionada
    if (starContainer) {
        starContainer.addEventListener('mouseleave', () => {
            updateStarsVisual(currentRating);
        });
    }
    // Contador de caracteres do textarea
    if (textarea && counter) {
        // Inicializa o contador
        textarea.addEventListener('input', function() {
            const currentLength = this.value.length;
            const maxLength = 1000;
            counter.textContent = `${currentLength} / ${maxLength}`;
            // Muda a cor se atingir o limite
            if (currentLength >= maxLength) {
                counter.style.color = 'red';
            } else {
                counter.style.color = '';
            }
        });
    }
    // Validação do formulário
    if (form) {
        form.addEventListener('submit', function(e) {
            const ratingValue = parseFloat(hiddenInput.value);

            // Se a nota for inválida (0 ou menor que 0.5)
            if (!ratingValue || ratingValue < 0.5) {
                e.preventDefault(); // Bloqueia envio
                
                // Remove a classe de erro para reiniciar a animação
                ratingText.classList.remove('text-error');

                // Força o reflow para reiniciar a animação
                void ratingText.offsetWidth; 

                // Adiciona a classe de erro
                ratingText.textContent = "Por favor, selecione uma nota!";
                ratingText.classList.add('text-error');
                
                // Rola a tela para garantir visualização
                ratingText.scrollIntoView({ behavior: 'smooth', block: 'center' });
            } else if (isEditMode) {
                // Em modo de edição, ajustar a ação do formulário
                e.preventDefault();
                // Extrai o ID do filme da URL
                const movieId = window.location.pathname.split('/').pop();
                form.action = `/movies/update/${movieId}`;
                form.submit();
            }
            
        });
    }
    // Atualiza as classes CSS das estrelas (cheia, meia, vazia) baseada na nota
    function updateStarsVisual(rating) {
        stars.forEach((star, index) => {
            const starValue = index + 1;
            star.classList.remove('fa-solid', 'fa-star-half-stroke', 'fa-regular');
            // Estrela cheia
            if (rating >= starValue) {
                star.classList.add('fa-solid', 'fa-star');
                star.style.color = 'var(--gold)';
            // Meia estrela
            } else if (rating >= starValue - 0.5) {
                star.classList.add('fa-solid', 'fa-star-half-stroke');
                star.style.color = 'var(--gold)';
            // Estrela vazia
            } else {
                star.classList.add('fa-regular', 'fa-star');
                star.style.color = 'var(--gray-star)';
            }
        });
    }
    // Atualiza o texto da nota exibida
    function updateRatingText(rating) {
        // Remove a classe de erro ao selecionar uma nota válida
        ratingText.classList.remove('text-error');
        // Atualiza o texto e estilo
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