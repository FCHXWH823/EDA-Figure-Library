const form = document.querySelector("#filters");
const query = document.querySelector("#query");
const category = document.querySelector("#category");
const resultCount = document.querySelector("#result-count");
const cards = [...document.querySelectorAll("#gallery .card")];

function filterAssets() {
  const terms = query.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
  let visible = 0;
  for (const card of cards) {
    const sameCategory = !category.value || card.dataset.category === category.value;
    const matchesTerms = terms.every((term) => card.dataset.search.includes(term));
    card.hidden = !(sameCategory && matchesTerms);
    if (!card.hidden) visible += 1;
  }
  resultCount.textContent = visible === 0
    ? "No matching figures. Try another term or category."
    : `Showing ${visible} of ${cards.length} figures`;
}

form.addEventListener("input", filterAssets);
form.addEventListener("submit", (event) => event.preventDefault());
form.addEventListener("reset", () => requestAnimationFrame(filterAssets));
form.hidden = false;
filterAssets();
