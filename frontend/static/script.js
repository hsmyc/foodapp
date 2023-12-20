const route = "http://127.0.0.1:8000/food";

document.getElementById("food_send").addEventListener("click", function (e) {
  e.preventDefault();
  const form = document.getElementById("food_form");
  const message = document.getElementById("food_create_message_text");
  const formData = {
    name: form.name.value,
    price: form.price.value,
    isHalal: form.Halal.checked,
    isVegan: form.Vegan.checked,
    isVegetarian: form.Vegetarian.checked,
    isGlutenFree: form["gluten"].checked,
    isPescatarian: form.Pescatarian.checked,
  };
  console.log(formData);
  fetch(route, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(formData),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Success:", data);
      message.innerText = "Food item created successfully";
      form.reset();
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});
