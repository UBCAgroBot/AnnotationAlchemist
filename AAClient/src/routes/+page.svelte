<!--
Color Theme:
Dark Green:  #16423C
Med Green:   #6A9C89
Light Green: #C4DAD2
Off White:   #E9EFEC
-->
<script lang="ts">
	// Without the line below the input will
	// have an unfixable error because of
	// it's webkitdirectory attribute.
	//@ts-nocheck

	let files: File[] = [];

	/*
	 * When the user uploads a file this will
	 * place them in the files array.
	 */
	function handleFileChange(event: Event) {
		const input = event.target as HTMLInputElement;
		if (!input.files) {
			return;
		}
		files = Array.from(input.files);
	}

	/*
	 * Queries the API with the files to
	 * have them processed.
	 */
	async function uploadFolder() {
		console.log(files);
		const formData = new FormData();
		files.forEach((file) => formData.append('files', file));
		formData.append('convert_from', convert_from);
		formData.append('convert_to', convert_to);
		const response = await fetch('http://localhost:8000/api/upload-folder', {
			method: 'POST',
			body: formData
		});

		if (response.ok) {
			console.log('Folder uploaded successfully!');
		} else {
			console.error('Error uploading folder.');
			console.log(response)
		}
	}

	/*
	 * ======================
	 * UI related TypeScript:
	 * ======================
	 */
	const categories = ['YOLO', 'YAML'];
	let convert_from = '';
	let convert_to = '';
</script>

<div class="h-screen w-full bg-[#C4DAD2] flex flex-col justify-center items-center text-[20px]">
	<h1 class="text-[#16423C] font-bold text-[48px] mb-12">Annotation Alchemist</h1>
	<div class="bg-[#16423C] text-white p-12 rounded-lg">
		<p class="mb-2">I would like to convert:</p>
		<div class="flex justify-between items-center mb-12">
			<select bind:value={convert_from} class="bg-[#6A9C89] p-2 mr-4 flex-grow rounded-lg">
				<option value="" disabled></option>
				{#each categories as category}
				  <option value={category}>{category}</option>
				{/each}
			</select>
			<p> to </p>
			<select bind:value={convert_to} class="bg-[#6A9C89] p-2 ml-4 flex-grow rounded-lg">
				<option value="" disabled></option>
				{#each categories as category}
				  <option value={category}>{category}</option>
				{/each}
			</select>
		</div>
		<div class="flex my-4 gap-x-4 flex-grow rounded-lg">
			<input
				class="bg-[#6A9C89]"
				type="file"
				webkitdirectory
				on:change={handleFileChange}
			/>
			<button class="bg-[#6A9C89] px-4 rounded-lg" on:click={uploadFolder}>Convert!</button>
		</div>
	</div>
</div>

<style>
	/* Styles here ... */
	h1 {
		font-family: 'Alice', serif;
	}
</style>
