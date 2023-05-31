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

async function favRecipe(id, fav) {
	await fetch("/api/recipe/fav", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({ id, fav }),
	});
	window.location.reload();
}

async function likeRecipe(id) {
	await fetch("/api/recipe/like", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({ id }),
	});
	window.location.reload();
}
