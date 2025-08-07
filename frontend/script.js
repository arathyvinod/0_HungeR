document.addEventListener("DOMContentLoaded", () => {
  const sendBtn = document.getElementById("send-btn");
  sendBtn.addEventListener("click", sendMessage);
});

function sendMessage() {
  const userInput = document.getElementById("user-input");
  const message = userInput.value.trim();

  if (message === "") return;

  appendMessage("You", message);
  userInput.value = "";

  fetch("http://127.0.0.1:8000/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ message })
  })
  .then(response => response.json())
  .then(data => {
    appendMessage("Bot", data.reply);
  })
  .catch(error => {
    console.error("Error:", error);
    appendMessage("Bot", "Sorry, something went wrong.");
  });
}

function appendMessage(sender, message) {
  const chatBox = document.getElementById("chat-box");
  const messageElement = document.createElement("div");
  messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
  chatBox.appendChild(messageElement);
  chatBox.scrollTop = chatBox.scrollHeight;
}



