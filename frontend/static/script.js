const signupButton = document.querySelector("#signup-button");
const dataField = document.querySelector("#data-field");
signupButton.addEventListener("click", (e) => {
  e.preventDefault();
  getButton(dataField);
});

const getButton = async (d) => {
  const message = await fetch("http://127.0.0.1:8000/osman");
  const response = await message.json();
  d.innerHTML = response.message;
};
