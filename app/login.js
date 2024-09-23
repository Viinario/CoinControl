async function handleLogin(event) {
    event.preventDefault(); // Previne o comportamento padrão do form (recarregar a página)

    // Captura os valores dos inputs
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Define o payload para enviar ao microserviço
    const payload = {
        email: email,
        password: password
    };

    try {
        // Faz a requisição para o microserviço (API Gateway)
        const response = await fetch('http://localhost:5000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        // Verifica a resposta
        if (response.ok) {
            const data = await response.json();
            alert('Login realizado com sucesso!');
            // Redireciona para a página index.html
            window.location.href = 'index.html'; // Coloque o caminho correto para a sua página
        } else {
            alert('Falha no login, verifique suas credenciais.');
        }
    } catch (error) {
        console.error('Erro ao realizar o login:', error);
        alert('Ocorreu um erro ao tentar realizar o login.');
    }
}
