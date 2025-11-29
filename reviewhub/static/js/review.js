document.addEventListener('DOMContentLoaded', function () {
  const stars = document.querySelectorAll('.rating span');
  const ratingInput = document.getElementById('rating-input');

  function setRating(value) {
    ratingInput.value = value;
    stars.forEach(s => {
      const v = parseInt(s.getAttribute('data-value'));
      if (v <= value) s.style.color = '#ffd166'; else s.style.color = 'rgba(255,255,255,0.35)';
    });
  }

  stars.forEach(s => {
    s.addEventListener('mouseenter', () => {
      const hoverVal = parseInt(s.getAttribute('data-value'));
      stars.forEach(ss => {
        const v = parseInt(ss.getAttribute('data-value'));
        ss.style.color = v <= hoverVal ? '#ffd166' : 'rgba(255,255,255,0.35)';
      });
    });

    s.addEventListener('mouseleave', () => {
      setRating(parseInt(ratingInput.value) || 0);
    });

    s.addEventListener('click', () => {
      setRating(parseInt(s.getAttribute('data-value')));
    });
  });

  // initialize
  setRating(parseInt(ratingInput.value) || 0);
});
