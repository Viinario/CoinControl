async function convertCripto() {
    const crypto_map = {
        'bitcoin': 'btc',
        'ethereum': 'eth',
        'litecoin': 'ltc',
        'ripple': 'xrp'
        // Adicione mais mapeamentos conforme necessário
    };
    const amount = document.getElementById("amount").value;
    const fromCurrency = document.getElementById("fromCurrency").value;
    const toCurrency = document.getElementById("toCurrency").value;

    if (amount === '' || amount <= 0) {
        alert("Por favor, insira um valor válido.");
        return;
    }

    // URL do API Gateway que será chamada
    const url = 'http://localhost:5000/convert-crypto'; // Aqui é o endpoint do API Gateway
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            amount: amount,
            from_currency: fromCurrency,
            to_currency: toCurrency
        })
    });

    const data = await response.json();
    document.getElementById("resultCripto").innerText = 
        `${data.converted_amount} ${crypto_map[toCurrency].toUpperCase()}`;
}

async function convertReal() {
    const amount = document.getElementById("amountReal").value;
    const fromCurrency = document.getElementById("fromCurrencyReal").value;
    const toCurrency = document.getElementById("toCurrencyReal").value;

    if (amount === '' || amount <= 0) {
        alert("Por favor, insira um valor válido.");
        return;
    }

    // URL do API Gateway que será chamada
    const url = 'http://localhost:5000/convert-real'; // Aqui é o endpoint do API Gateway
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            amount: amount,
            from_currency: fromCurrency,
            to_currency: toCurrency
        })
    });

    const data = await response.json();
    document.getElementById("resultReal").innerText = 
        `${data.converted_amount} ${toCurrency.toUpperCase()}`;
}

function openTab(evt, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

let portfolio = [];

function addHolding() {
    const cryptoType = document.getElementById("crypto-type").value;
    const cryptoAmount = parseFloat(document.getElementById("crypto-amount").value);

    if (cryptoAmount && cryptoAmount > 0) {
        const existingHolding = portfolio.find(holding => holding.type === cryptoType);

        if (existingHolding) {
            existingHolding.amount += cryptoAmount;
        } else {
            portfolio.push({ type: cryptoType, amount: cryptoAmount });
        }

        updatePortfolioDisplay();
    }
}

function removeHolding(index) {
    portfolio.splice(index, 1); // Remove o item do array
    updatePortfolioDisplay();
}

// Mapeamento dos símbolos para os nomes das criptomoedas
const crypto_map = {
    'btc': 'bitcoin',
    'eth': 'ethereum',
    'ltc': 'litecoin',
    'xrp': 'ripple',
    // Adicione mais mapeamentos conforme necessário
};

async function openConversionTab(cryptoType, amount, index) {
    // URL do API Gateway que será chamada para a conversão
    const url = 'http://localhost:5000/convert-crypto'; // Aqui é o endpoint do API Gateway

    // Mapeamento dos símbolos para os nomes das criptomoedas
    const crypto_map = {
        'btc': 'bitcoin',
        'eth': 'ethereum',
        'ltc': 'litecoin',
        'xrp': 'ripple',
        'dolar': 'usd',
        'euro': 'eur',
        'real': 'brl',
        'bitcoin': 'btc',
        'ethereum': 'eth',
        'litecoin': 'ltc',
        'ripple': 'xrp'
        // Adicione mais mapeamentos conforme necessário
    };

    // Moedas disponíveis (nomes completos)
    let currencies = ['bitcoin', 'ethereum', 'litecoin', 'ripple', 'dolar', 'euro', 'real'];  // Usando os nomes completos diretamente

    // Verifica se o símbolo da criptomoeda está no mapeamento
    const from_currency_name = crypto_map[cryptoType.toLowerCase()]; // Nome da criptomoeda de origem

    if (!from_currency_name) {
        alert('Criptomoeda não suportada.');
        return;
    }

    // Filtra a moeda de origem (remover ela da lista de moedas de destino)
    currencies = currencies.filter(currency => currency !== from_currency_name);

    try {
        // Faz uma requisição de conversão para cada moeda de destino (exceto a de origem)
        const promises = currencies.map(async (toCurrencyName) => {

            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    amount: amount,               // Quantidade a ser convertida
                    from_currency: from_currency_name,    // Usamos o nome completo, ex: 'bitcoin'
                    to_currency: toCurrencyName       // Moeda de destino também usando o nome completo (ex: 'ethereum')
                })
            });

            // Verifica se a requisição foi bem-sucedida
            if (!response.ok) {
                throw new Error(`Erro ao converter para ${toCurrencyName}.`);
            }

            // Retorna a resposta convertida
            const data = await response.json();
            return { toCurrencyName, converted_amount: data.converted_amount };
        });

        // Espera todas as requisições serem completadas
        const results = await Promise.all(promises);

        // Localiza o elemento onde os resultados serão exibidos
        const resultDiv = document.getElementById(`conversion-results-${index}`);
        resultDiv.innerHTML = `<h4>Conversão de ${amount} ${from_currency_name}:</h4>`;  // Título para os resultados

        // Itera pelos resultados e escreve cada conversão
        results.forEach(result => {
            const resultLine = document.createElement('p');
            resultLine.textContent = `${result.converted_amount} ${ crypto_map[result.toCurrencyName].toUpperCase()}`;
            resultDiv.appendChild(resultLine);
        });

    } catch (error) {
        // Exibe uma mensagem de erro caso a conversão falhe
        console.error('Erro:', error);
        alert('Erro ao realizar a conversão. Tente novamente.');
    }
}

function updatePortfolioDisplay() {
    const portfolioList = document.getElementById("portfolio-list");
    portfolioList.innerHTML = "";

    portfolio.forEach((holding, index) => {
        const item = document.createElement("div");
        item.classList.add("portfolio-item"); // Adiciona uma classe para estilizar
        item.innerHTML = `
            <span>${holding.type}: ${holding.amount}</span> 
            <div class="button-group">
                <button class="remove-btn" onclick="removeHolding(${index})">Remover</button>
                <button class="view-btn" onclick="openConversionTab('${holding.type}', ${holding.amount}, ${index})">Ver Conversão</button>
            </div>
            <div id="conversion-results-${index}" class="conversion-results"></div> <!-- Div para os resultados da conversão -->
        `;
        portfolioList.appendChild(item);
    });
}









