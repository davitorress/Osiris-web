const recipesItem = [...document.querySelectorAll(".recipe-item")];

for (const recipeItem of recipesItem) {
	recipeItem.addEventListener("click", (ev) => {
		const origin = window.location.origin;
		window.location.href = origin + "/receitas/" + ev.currentTarget.id;
	});
}
