const recipesItem = [...document.querySelectorAll(".recipe-item")];
const createRecipeBtn = document.querySelector("button.create-recipe");

for (const recipeItem of recipesItem) {
	recipeItem.addEventListener("click", (ev) => {
		const origin = window.location.origin;
		window.location.href = origin + "/receitas/" + ev.currentTarget.id;
	});
}

createRecipeBtn.addEventListener("click", () => {
	const origin = window.location.origin;
	window.location.href = origin + "/receitas/criar";
});
