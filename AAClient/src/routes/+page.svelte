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

	let files:File [] = [];

    /*
     * When the user uploads a file this will 
     * place them in the files array.
     */
	function handleFileChange(event: Event) {
        const input = event.target as HTMLInputElement;
        if (!input.files) { return; }
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
		const response = await fetch('http://localhost:8000/api/upload-folder', {
			method: 'POST',
			body: formData
		});

		if (response.ok) {
			console.log('Folder uploaded successfully!');
		} else {
			console.error('Error uploading folder.');
		}
	}
</script>

<div class="h-screen w-full bg-[#C4DAD2] flex flex-col justify-center items-center text-[20px]">
	<h1 class="text-[#16423C] font-bold text-[48px] mb-12">Annotation Alchemist</h1>
    <div class="bg-[#16423C] text-white p-12 rounded-lg">
        <div class="flex my-4">
	        <input class="border-2 border-black" type="file" webkitdirectory on:change={handleFileChange} />
	        <button class="border-2 border-black" on:click={uploadFolder}>Convert!</button>
        </div>
    </div>
</div>

<style>
	/* Styles here ... */
    h1 {
        font-family: "Alice", serif;
    }
</style>
