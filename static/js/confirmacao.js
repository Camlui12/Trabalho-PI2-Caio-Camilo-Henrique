document.addEventListener('DOMContentLoaded', function() {
    
    // Define o tempo de espera em segundos
    let countdownTime = 3; 
    
    // URL para onde o usuário será redirecionado
    const redirectUrl = '/'; // Altere para a página principal do seu sistema

    const countdownElement = document.getElementById('countdown');

    // Inicia a contagem regressiva na tela
    const interval = setInterval(() => {
        countdownTime--;
        if (countdownElement) {
            countdownElement.textContent = countdownTime;
        }
        if (countdownTime <= 0) {
            clearInterval(interval);
            window.location.href = redirectUrl;
        }
    }, 1000); // Atualiza a cada segundo

});