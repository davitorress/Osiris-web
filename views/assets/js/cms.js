function redirect(link) {
	const origin = window.location.origin;
	window.location.href = origin + "/cms" + link;
}
