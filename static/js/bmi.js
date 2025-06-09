document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("bmiForm");
  const resultBox = document.getElementById("resultBox");

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    const formData = new FormData(form);

    fetch("/bmi_ajax", {
      method: "POST",
      body: formData,
      headers: {
        "X-Requested-With": "XMLHttpRequest"
      }
    })
      .then((response) => response.json())
      .then((data) => {
        resultBox.textContent = data.result;
      })
      .catch((error) => {
        resultBox.textContent = "计算失败，请稍后再试";
        console.error("Error:", error);
      });
  });
});
