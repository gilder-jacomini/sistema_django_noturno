const form = document.querySelector('form');
const maskcpf = document.querySelector('#cpf');
const masktelefone = document.querySelector('#telefone');

// maskcpf.addEventListener('input', function() {
//     this.value = this.value.replace(/\D/g, '')
//     .replace(/(\d{3})(\d)/, '$1.$2')
//     .replace(/(\d{3})(\d)/, '$1.$2')
//     .replace(/(\d{3})(\d{1,2})$/, '$1-$2');
// });

maskcpf.addEventListener('input', function(e) {
    e.target.value = e.target.value.replace(/\D/g, '')
    .replace(/(\d{3})(\d)/, '$1.$2')
    .replace(/(\d{3})(\d)/, '$1.$2')
    .replace(/(\d{3})(\d{1,2})$/, '$1-$2');
});


masktelefone.addEventListener('input', function() {
    this.value = this.value.replace(/\D/g, '')
    .replace(/(\d{2})(\d)/, '($1) $2')
    .replace(/(\d{4,5})(\d)/, '$1-$2')
    .replace(/(\d{4})\d+?$/, '$1');
});

