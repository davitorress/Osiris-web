const pancsItems = [...document.querySelectorAll(".panc-item")];

for (const pancItem of pancsItems) {
	pancItem.addEventListener("click", (ev) => {
		const origin = window.location.origin;
		window.location.href = origin + "/pancs/" + ev.currentTarget.id;
	});
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
