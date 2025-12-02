document.addEventListener('DOMContentLoaded', () => {
    const stars = document.querySelectorAll('.star');
    const starContainer = document.getElementById('star-container');
    const hiddenInput = document.getElementById('rating-input');
    const ratingText = document.getElementById('rating-text');
    
    const textarea = document.getElementById('review-text');
    const counter = document.getElementById('char-counter');
    const form = document.getElementById('reviewForm');

    let currentRating = 0;

    const isEditMode = textarea.value.trim().length > 0;

    if (isEditMode) {
        const ratingValue = parseFloat(ratingText.textContent);
        if (!isNaN(ratingValue) && ratingValue > 0) {
            currentRating = ratingValue;
            hiddenInput.value = currentRating;
            updateStarsVisual(currentRating);
            ratingText.style.color = '#eab308';
            ratingText.style.fontWeight = 'bold';
        }
    }

    stars.forEach((star) => {
        star.addEventListener('mousemove', (e) => {
            const rect = star.getBoundingClientRect();
            const width = rect.width;
            const x = e.clientX - rect.left;
            
            const isHalf = x < (width / 2);
            const starValue = parseInt(star.getAttribute('data-value'));
            
            const tempRating = isHalf ? starValue - 0.5 : starValue;
            updateStarsVisual(tempRating);
        });

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

    if (starContainer) {
        starContainer.addEventListener('mouseleave', () => {
            updateStarsVisual(currentRating);
        });
    }

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

    if (form) {
        form.addEventListener('submit', function(e) {
            const ratingValue = parseFloat(hiddenInput.value);

            if (!ratingValue || ratingValue < 0.5) {
                e.preventDefault();

                ratingText.classList.remove('text-error');

                void ratingText.offsetWidth; 

                ratingText.textContent = "Por favor, selecione uma nota!";
                ratingText.classList.add('text-error');
                
                ratingText.scrollIntoView({ behavior: 'smooth', block: 'center' });
            } else if (isEditMode) {
                e.preventDefault();
                
                const movieId = window.location.pathname.split('/').pop();
                form.action = `/movies/update/${movieId}`;
                form.submit();
            }
        });
    }

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