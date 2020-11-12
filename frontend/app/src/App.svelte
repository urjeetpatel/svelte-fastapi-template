<script>
	import { text } from "svelte/internal";

	export let name;
	async function getBackendData() {
		const response = await fetch("http://localhost:5001/");
		const text = await response.json();
		console.log(text);
		if (response.ok) {
			return text;
		} else {
			throw new Error(text);
		}
	}

	let promise = getBackendData();
</script>

<main class="text-center p-4 my-0">
	<h1 class="uppercase text-6xl font-hairline text-primary">Hello {name}!</h1>
	<p>
		Visit the
		<a href="https://svelte.dev/tutorial">Svelte tutorial</a>
		to learn how to build Svelte apps.
	</p>
	{#await promise}
		<div class="spinner">Spinner Here</div>
	{:then text}
		<div class="">Hello from the backend {text.Hello}</div>
	{:catch error}
		<div class="uppercase text-red-700">{error.message}</div>
	{/await}
</main>
