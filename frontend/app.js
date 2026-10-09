const API_URL = "http://localhost:5000/api/products";

fetch(API_URL)
  .then((res) => res.json())
  .then((data) => {
    if (data.error) throw new Error(data.error);
    document.getElementById("status").textContent = "Products loaded from the database:";
    const list = document.getElementById("products");
    data.forEach((p) => {
      const li = document.createElement("li");
      li.textContent = `${p.name} - Rs. ${p.price}`;
      list.appendChild(li);
    });
  })
  .catch((err) => {
    document.getElementById("status").textContent = "Could not load products: " + err.message;
  });
