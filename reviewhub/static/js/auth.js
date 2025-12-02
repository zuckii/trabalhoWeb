const input = document.getElementById("senha");
const btn = document.getElementsByClassName("toggle-btn")[0];
// Alterna a visibilidade da senha ao clicar no botão
btn.addEventListener("click", () => {
    if (input.type === "password") {
        input.type = "text";

        btn.classList.remove("fa-eye");
        btn.classList.add("fa-eye-slash");
    } else {
        input.type = "password";
        
        btn.classList.remove("fa-eye-slash");
        btn.classList.add("fa-eye");
    }
});