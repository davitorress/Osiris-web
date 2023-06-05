function redirect(link) {
	const origin = window.location.origin;
	window.location.href = origin + link;
}

async function favPanc(id, fav) {
	await fetch("/api/panc/fav", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({ id, fav }),
	});
	window.location.reload();
}

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

async function likeRecipe(id, like) {
	await fetch("/api/recipe/like", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({ id, like }),
	});
	window.location.reload();
}
