document.addEventListener("DOMContentLoaded", function () {
  const formSupplier = document.getElementById("form-supplier");
  const tableBody = document.getElementById("supplier-table-body");

  function loadSuppliers() {
    const suppliers = JSON.parse(localStorage.getItem("suppliers")) || [];
    return suppliers;
  }

  function saveSuppliers(suppliers) {
    localStorage.setItem("suppliers", JSON.stringify(suppliers));
  }

  function updateTable() {
    if (tableBody) {
      const suppliers = loadSuppliers();
      tableBody.innerHTML = "";

      suppliers.forEach((supplier, index) => {
        const row = document.createElement("tr");

        row.innerHTML = `
                  <td>${index + 1}</td>
                  <td>${supplier.name}</td>
                  <td>${supplier.address}</td>
                  <td>${supplier.email}</td>
                  <td>${supplier.phone}</td>
                  <td>Aktif</td>
                  <td class="actions">
                      <button class="order">Order</button>
                      <button class="edit">Edit</button>
                      <button class="delete">Delete</button>
                  </td>
              `;

        tableBody.appendChild(row);
      });
    }
  }

  if (formSupplier) {
    formSupplier.addEventListener("submit", function (event) {
      event.preventDefault();

      const name = document.getElementById("name").value;
      const address = document.getElementById("address").value;
      const email = document.getElementById("email").value;
      const phone = document.getElementById("phone").value;

      const newSupplier = {
        name: name,
        address: address,
        email: email,
        phone: phone,
      };

      const suppliers = loadSuppliers();
      suppliers.push(newSupplier);
      saveSuppliers(suppliers);

      window.location.href = "index.html";
    });
  }

  updateTable();
});
