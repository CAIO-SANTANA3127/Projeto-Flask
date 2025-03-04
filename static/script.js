console.log("JavaScript carregado com sucesso!");

document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');

    loginForm.addEventListener('submit', (event) => {
        event.preventDefault(); // Evita o envio do formulário para fins de demonstração

        const username = document.getElementById('username').value.trim();
        const password = document.getElementById('password').value.trim();

        if (!username || !password) {
            alert('Por favor, preencha todos os campos.');
        } else {
            alert(`Bem-vindo, ${username}!`);
            // Aqui você pode enviar os dados para o servidor
        }
    });
});

//TELA CADAstro 
//------------------BOTAO DE VOLAR/backButton-------------------------
document.addEventListener('DOMContentLoaded', () => {
    const backButton = document.getElementById('backButton');

    // Adiciona o evento de clique ao botão
    backButton.addEventListener('click', () => {
        window.history.back(); 
     // Volta para a página anterior no histórico do navegador
    });
});


document.getElementById('cadastroForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Limpar mensagens de erro
    document.getElementById('nomeError').textContent = '';
    document.getElementById('emailError').textContent = '';
    document.getElementById('senhaError').textContent = '';

    const nome = document.getElementById('nome').value.trim();
    const email = document.getElementById('email').value.trim();
    const senha = document.getElementById('senha').value.trim();

    let isValid = true;

    if (!nome) {
        document.getElementById('nomeError').textContent = 'O nome é obrigatório.';
        isValid = false;
    }

    if (!email) {
        document.getElementById('emailError').textContent = 'O e-mail é obrigatório.';
        isValid = false;
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        document.getElementById('emailError').textContent = 'E-mail inválido.';
        isValid = false;
    }

    if (!senha) {
        document.getElementById('senhaError').textContent = 'A senha é obrigatória.';
        isValid = false;
    } else if (senha.length < 6) {
        document.getElementById('senhaError').textContent = 'A senha deve ter pelo menos 6 caracteres.';
        isValid = false;
    }

    if (isValid) {
        alert('Cadastro realizado com sucesso!');
        document.getElementById('cadastroForm').reset();
    }
});