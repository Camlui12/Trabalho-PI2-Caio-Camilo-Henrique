const inputs = document.querySelectorAll('.valor');

  inputs.forEach(function(input) {
    input.addEventListener('input', function(e) {
      let valor = e.target.value.replace(/\D/g, '');
      valor = (valor / 100).toFixed(2) + '';
      valor = valor.replace('.', ',');
      valor = valor.replace(/\B(?=(\d{3})+(?!\d))/g, '.');
      e.target.value = 'R$ ' + valor;
    });
  });


const inputTolerancia = document.getElementById('tolerancia');

  // Quando o campo ganha foco, remove o 'min' (para facilitar edição)
  inputTolerancia.addEventListener('focus', function(e) {
    e.target.value = e.target.value.replace(/\s*min$/, '').trim();
  });

  // Quando o campo perde o foco, adiciona o 'min'
  inputTolerancia.addEventListener('blur', function(e) {
    let valor = e.target.value.replace(/\D/g, '');
    if (valor !== '') {
      e.target.value = valor + ' min';
    } else {
      e.target.value = '';
    }
  });