import json
import matplotlib.pyplot as plt

values = []
times = []

with open('/Users/caiodeluiz/Documents/GitHub/Trabalho-PI2-Caio-Camilo-Henrique/medicoes-sla/resultado.json') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        data = json.loads(line)
        # Só pega as linhas que são pontos da métrica 'vus'
        if data.get('metric') == 'http_req_duration' and data.get('type') == 'Point':
            values.append(data['data']['value'])
            times.append(data['data']['time'])

plt.figure(figsize=(12,6))
plt.plot(times, values, marker='o')
plt.xlabel('Tempo')
plt.ylabel('Valor VUs')
plt.title('Evolução dos VUs durante o teste')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()