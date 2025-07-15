document.addEventListener('DOMContentLoaded', function() {
    
    // Define o tempo de espera em segundos
    let countdownTime = 5; 
    
    // URL para onde o usuário será redirecionado (pode ser a página anterior ou a principal)
    const redirectUrl = '/'; // Altere para a página que fizer mais sentido

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