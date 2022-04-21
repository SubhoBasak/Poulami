const socket = io("https://poulami.herokuapp.com/");

const form = document.getElementById("send-contaner");
const messageImput = document.getElementById("messageImp");
const messageContainer = document.querySelector(".contaner");

const append = (message, position) => {
  const messageElement = document.createElement("div");
  messageElement.innerText = message;
  messageElement.classList.add("message");
  messageElement.classList.add(position);
  messageContainer.append(messageElement);
};
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const message = messageImput.value;
  append(`you: ${message}`, "right");
  socket.emit("send", message);
  messageImput.value = "";
});
const name = prompt("Enter your name to join ");
//console.log(name);
socket.emit("new-user-joined", name);
socket.on("user-joined", (name) => {
  append(`${name} joined`, "center");
});
socket.on("receive", (data) => {
  append(`${data.name}: ${data.message}`, "left");
});
socket.on("left", (name) => {
  append(`${name} left`, "left");
});
