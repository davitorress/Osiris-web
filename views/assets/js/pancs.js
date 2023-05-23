const pancsItems = [...document.querySelectorAll(".panc-item")];
console.log(pancsItems);

for (pancItem of pancsItems) {
	pancItem.addEventListener("click", (ev) => {
		const origin = window.location.origin;
		window.location.href = origin + "/pancs/" + ev.currentTarget.id;
	});
}
