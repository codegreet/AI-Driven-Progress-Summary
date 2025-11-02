async function loadData() {
  const response = await fetch("/get_progress");
  const data = await response.json();

  document.getElementById("summary").textContent = data.summary;

  const ctx = document.getElementById("progressChart").getContext("2d");
  const labels = data.week_data.map(d => d.day);
  const values = data.week_data.map(d => d.hours_studied);

  new Chart(ctx, {
    type: "line",
    data: {
      labels: labels,
      datasets: [{
        label: "Hours Studied per Day",
        data: values,
        borderWidth: 3
      }]
    }
  });
}

loadData();
