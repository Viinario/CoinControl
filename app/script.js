async function convertCripto() {
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
        `${amount} ${fromCurrency} = ${data.converted_amount} ${toCurrency}`;
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
        `${amount} ${fromCurrency} = ${data.converted_amount} ${toCurrency}`;
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
