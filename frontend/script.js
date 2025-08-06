async function sendMessage() {
    const input = document.getElementById("user-input").value;
    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<div class='user'>You: ${input}</div>`;

    let response = "I didn't understand that.";

    if (input.toLowerCase().includes("planting tips")) {
        const crop = prompt("Which crop? (e.g., Rice, Wheat, Tomato)");
        const res = await fetch(`/planting-tips?crop=${crop}`);
        const data = await res.json();
        response = data.tip;
    } else if (input.toLowerCase().includes("weather")) {
        const city = prompt("Enter your city:");
        const res = await fetch(`/weather?city=${city}`);
        const data = await res.json();
        response = data.error ? data.error : `Temperature: ${data.temperature}, ${data.description}`;
    } else if (input.toLowerCase().includes("suggest crop")) {
        const season = prompt("Which season? (Kharif, Rabi, Zaid)");
        const res = await fetch(`/crop-suggestion?season=${season}`);
        const data = await res.json();
        response = `Suggested Crops: ${data.suggested_crops}`;
    }

    chatBox.innerHTML += `<div class='bot'>Bot: ${response}</div>`;
    document.getElementById("user-input").value = "";
}
