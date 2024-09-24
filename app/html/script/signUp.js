async function handleRegister(event) {
    event.preventDefault(); // Previne o comportamento padrão do form (recarregar a página)

    // Captura os valores dos inputs
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm_password').value;

    // Validação simples de senha
    if (password !== confirmPassword) {
        alert('As senhas não coincidem!');
        return;
    }

    // Define o payload para enviar ao microserviço
    const payload = {
        name: name,
        email: email,
        password: password
    };

    try {
        // Faz a requisição para o microserviço através do API Gateway
        const response = await fetch('http://localhost:5000/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        // Verifica a resposta
        if (response.ok) {
            const data = await response.json();
            alert('Registro realizado com sucesso!');
            // Redireciona para a página de login
            window.location.href = 'login.html';
        } else {
            const errorData = await response.json();
            alert(`Erro ao registrar: ${errorData.message}`);
        }
    } catch (error) {
        console.error('Erro ao realizar o registro:', error);
        alert('Ocorreu um erro ao tentar realizar o registro.');
    }
}
