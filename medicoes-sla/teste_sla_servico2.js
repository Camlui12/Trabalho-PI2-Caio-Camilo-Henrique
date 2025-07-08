import http from 'k6/http';
import { sleep, check } from 'k6';

// Parâmetros do teste
export const options = {
    vus: 5, // Usuários virtuais simultâneos
    duration: '1m', // Duração total do teste
};

// Lista de placas
const placas = [
    'AVT3112', 'AYA6429', 'BAK5209', 'BHY8302', 'BPI5047', 'CCR1621', 'COA7990',
    'CQS9646', 'CYW2392', 'DYU5289', 'FNU5816', 'GKP3004', 'GPW5165', 'GSU0471',
    'GWN2032', 'HAF2164', 'HBR2549', 'HHN2102', 'HLU0543', 'HXX5330', 'IDT0662',
    'KIK3809', 'LAJ3307', 'LBT6729', 'LDI3446', 'LXN8866', 'NHP5355', 'OPY3394',
    'OQV2411', 'PMR5925', 'POH3726', 'PQL3006', 'PSR7131', 'PYP5954', 'QYD4751',
    'RGT6620', 'RLC9156', 'RUH4666', 'SOW8117', 'UFL9753', 'UHZ0772', 'UOU2231',
    'VBM8282', 'XNE6488', 'XOT7281', 'XXO2479', 'YJG3387', 'YXJ3274', 'ZOG9261',
    'ZTO5381', 'CFK7117', 'CQA9321', 'CTO8607', 'DFX3265', 'DLD3161', 'DRB5853',
    'EIR4063', 'EPU0539', 'EQQ6981', 'ERB1752', 'FWU9593', 'GOV7378', 'GTJ1021',
    'HLS9048', 'HMG1255', 'HRN4845', 'IEZ2649', 'IGK0187', 'IJG0204', 'ILS1923',
    'JXB8647', 'KBH1372', 'KZA2924', 'LIV2853', 'LYN1569', 'NJL7163', 'OEQ5373',
    'OEU5915', 'OEY8114', 'OSK8027', 'POJ8684', 'QIA6576', 'QWL9684', 'RCV0772',
    'RXM2664', 'RXY7247', 'SEZ8588', 'SPO6383', 'THO6502', 'TKH3361', 'TOE5049',
    'TTT7977', 'VJO0056', 'VQB8220', 'WDK6090', 'XTX9603', 'ZGC9908', 'ZQA7774',
    'ZQR2037', 'ZRA1632'
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

    sleep(Math.random() * 2);

    // 2) Envia POST simulando envio da placa
    const placa = placaAleatoria();
    const payload = `placa=${encodeURIComponent(placa)}`;
    const headers = { 'Content-Type': 'application/x-www-form-urlencoded' };

    const postRes = http.post('http://127.0.0.1:5000/confirmarSaida', payload, { headers });
    check(postRes, {
        'Placa enviada (status 200 ou 302)': (r) => r.status === 200 || r.status === 302,
        'Resposta contem placa': (r) => r.body && r.body.includes(placa),
    });

    sleep(Math.random() * 2);

    // 3) Usuário volta para a página de registro de saída
    const pageBack = http.get('http://127.0.0.1:5000/registro-saida');
    check(pageBack, {
        'Retornou à tela de registro-saida': (r) => r.status === 200,
    });
}