import http from 'k6/http';
import { sleep, check } from 'k6';

// Parâmetros do teste (ajuste conforme cenário)
export const options = {
    vus: 5, // Usuários virtuais simultâneos
    duration: '1m', // Duração total do teste
};

// Lista de placas (adicione/remova conforme seu cenário real)
const placas = [
    "ADN8231","AOD5371","AXX4682","AZV0209","BAJ0227","BCB4703","BHP9514",
    "BTT1674","CAX7027","CFH0392","CJR6472","CLG7034","DBQ7353","DED7144",
    "DJX2944","DLC9943","EBR5975","EKP9908","EMU3584","ENJ1394","EPZ1584",
    "ERK2345","ESA9035","FBR4057","FFM5013","FXD7718","FXS2177","GBE3943",
    "GHG8655","GKC5070","GOD0724","HBW4884","HCJ6505","HPE8830","HTJ6173",
    "IGO0336","ITA0886","IVF4131","IXX7485","JER5510","JQW4918","KGU8614",
    "KMY6419","KSN2113","KXC6618","KXO2639","KYB9363","KZI3791","LHT4037",
    "LIN6439","LPS5404","LWW7565","MDZ7490","MGU2837","MRI4233","MXF6111",
    "NDT0385","NGX4140","NQR9600","OHE7367","OXS4906","PAM9863","PTB2893",
    "PTZ3783","PUI2092","QFQ5492","QII6446","QNG5865","QOF8081","RCP3445",
    "RLZ8396","RSL9727","RVE7434","SCP4625","SLR2472","SQS5140","TCJ5423",
    "TLL4868","TMU8666","TNN3016","URD2748","UST6559","UUE1335","UUM8207",
    "VEM0647","VIT9073","WVI4143","XCA2337","XCY7831","XKQ9190","XLD0919",
    "YAM4918","YAZ4441","YBN8190","YGB5509","YKT3562","YLZ5936","YXU3384",
    "ZEF4061","ZNR1469"
];

// Função para selecionar placa aleatória
function placaAleatoria() {
    return placas[Math.floor(Math.random() * placas.length)];
}

export default function () {
    // 1) Usuário acessa página de registro de saída
    const pageRes = http.get('http://127.0.0.1:5000/registro-saida');
    check(pageRes, {
        'Acesso página registro-saida (200)': (r) => r.status === 200,
    });

    sleep(Math.random() * 2); // Simula tempo para preencher placa

    // 2) Usuário preenche campo "placa" e envia via POST para /confirmarSaida
    const placa = placaAleatoria();
    const payload = `placa=${encodeURIComponent(placa)}`;
    const headers = { 'Content-Type': 'application/x-www-form-urlencoded' };

    const postRes = http.post('http://127.0.0.1:5000/confirmarSaida', payload, { headers });
    check(postRes, {
        'Placa enviada (status 200 ou 302)': (r) => r.status === 200 || r.status === 302,
        'Resposta contem placa': (r) => r.body && r.body.includes(placa),
    });

    sleep(Math.random() * 2); // Simula usuário lendo a tela/botão "voltar"

    // 3) Usuário volta para o registro de saída
    const pageBack = http.get('http://127.0.0.1:5000/registro-saida');
    check(pageBack, {
        'Retornou à tela de registro-saida': (r) => r.status === 200,
    });

    // Pode repetir para simular novo veículo! (loop k6 faz automaticamente)
}