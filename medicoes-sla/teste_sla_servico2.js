import http from 'k6/http';
import { sleep, check } from 'k6';

// Parâmetros do teste (ajuste conforme cenário)
export const options = {
    vus: 5, // Usuários virtuais simultâneos
    duration: '1m', // Duração total do teste
};

// Lista de placas (adicione/remova conforme seu cenário real)
const placas = [
    "CXZ4805","KWR6136","ZDB9490","QLK7375","DZD4958","LNF4833",
    "WVA4105","VSC8202","MWH5022","VSM2823","EUK1004","TYR5333",
    "DBY5288","ENH5140","MDV0609","BQL9266","DGF0665","TOC6030",
    "DKT1978","JLE5001","FPX4145","BJI9047","BAP7227","ETR7065",
    "PLX4876","HHY3796","HRP5411","XTG1373","WGC2951","EIQ3192",
    "HVV4943","YIT0345","LFS6439","GKR4391","GSB7108","DYD9347",
    "QUR1336","VUE1283","NKJ3404","AYC0571","AGX2071","WWR1375",
    "WFR2285","OZX8752","LVM6969","RXP9102","XTH2817","PLK9017",
    "GLF5636","HND2723","RVT6410","REI5753","EFQ1409"
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
        'Resposta contem placa':    (r) => r.body && r.body.includes(placa),
    });

    sleep(Math.random() * 2); // Simula usuário lendo a tela/botão "voltar"

    // 3) Usuário volta para o registro de saída
    const pageBack = http.get('http://127.0.0.1:5000/registro-saida');
    check(pageBack, {
        'Retornou à tela de registro-saida': (r) => r.status === 200,
    });

    // Pode repetir para simular novo veículo! (loop k6 faz automaticamente)
}