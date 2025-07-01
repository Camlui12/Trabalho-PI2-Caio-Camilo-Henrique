import http from 'k6/http';
import { sleep } from 'k6';

export let options = {
    vus: 1,
    iterations: 100, // até 100 veículos
};

function randomStr(size = 3) {
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let result = '';
    for (let i = 0; i < size; i++) {
        result += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    return result;
}

function randomNum(size = 4) {
    let result = '';
    for (let i = 0; i < size; i++) {
        result += Math.floor(Math.random() * 10);
    }
    return result;
}

/**
 * Fluxo:
 * 1. Tenta registrar entrada -> se placa não existe vai para fluxo de cadastro de veículo.
 * 2. Cadastra veículo no /cadastrarVeiculo (após ser redirecionado do backend)
 * 3. Tenta registrar entrada novamente (agora veículo cadastrado)
 */

// Alterna entre Carro e Moto
function tipoVeiculo(i) {
    return i % 2 === 0 ? 'Carro' : 'Moto';
}

export default function () {
    const i = __ITER; // número da iteração (útil pra alternar)
    const placa = randomStr(3) + randomNum(4);
    const modelo = "Modelo_" + randomStr(2);
    const cor = "Cor_" + randomStr(2);
    const tipo = tipoVeiculo(i);

    // 1. Tenta registrar entrada – POST no confirmação
    let payload = `placa=${placa}`;
    let params = {
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        redirects: 0, // não segue redirect automaticamente
    };

    // Supõe que o formulário de registro-entrada faz POST para /confirmarEntrada (pelo HTML não estava explícito, ajuste se necessário)
    let res = http.post('http://127.0.0.1:5000/confirmarEntrada', payload, params);

    // Se resposta for 200, caiu direto no cadastro de veículo (placa não existe, renderizou form de cadastro)
    if (res.status === 200 && res.body && res.body.includes('Cadastrar Veículo')) {
        // 2. Submete cadastro em /cadastrarVeiculo
        let cadastroPayload =
            `placa=${placa}&modelo=${modelo}&cor=${cor}&tipo=${tipo}`;
        let cadastroRes = http.post(
            'http://127.0.0.1:5000/cadastrarVeiculo',
            cadastroPayload,
            {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                redirects: 1,
            }
        );
        sleep(1);

        // 3. REGISTRAR ENTRADA NOVAMENTE, agora o carro existe!
        let confirmRes = http.post(
            'http://127.0.0.1:5000/confirmarEntrada',
            `placa=${placa}`,
            params
        );
        sleep(1);
    } else if (res.status === 302) {
        // Se foi redirecionado, provavelmente já existe -- fluxo rudimentar, pode adaptar conforme frontend
        // (Opcional: seguir Location e incrementar lógica)
        sleep(1);
    } else {
        // Outro resultado, pode logar para investigar depois
        sleep(1);
    }
}
