document.addEventListener('DOMContentLoaded', () => {
    const stars = document.querySelectorAll('.star');
    const ratingInput = document.getElementById('rating-input');

    stars.forEach(star => {
        star.addEventListener('click', () => {
            const rating = star.getAttribute('data-value');
            ratingInput.value = rating;

            stars.forEach(s => {
                s.classList.toggle('selected', s.getAttribute('data-value') <= rating);
            });
        });
    });
});
