async function convert() {
    const amount = document.getElementById("amount").value;
    const fromCurrency = document.getElementById("fromCurrency").value;
    const toCurrency = document.getElementById("toCurrency").value;

    if (amount === '' || amount <= 0) {
        alert("Por favor, insira um valor válido.");
        return;
    }

    // URL do API Gateway que será chamada
    const url = 'http://localhost:5000/convert-currency'; // Aqui é o endpoint do API Gateway
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
    document.getElementById("result").innerText = 
        `${amount} ${fromCurrency} = ${data.converted_amount} ${toCurrency}`;
}
