document.getElementById('modelBtn').addEventListener('click', function () {
    const inputJson = document.getElementById('inputJson').value;
    const outputJson = document.getElementById('outputJson');

    try {
        outputJson.style.color = "black";
        // Parse the input JSON
        const parsedJson = JSON.parse(inputJson);

        // Send the JSON to the server to generate the C# classes
        fetch('http://127.0.0.1:5000/generate-classes', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(parsedJson),
        })
        .then(response => response.json())
        .then(data => {
            // Add a "Download All" link at the top
            let outputContent = '<a href="http://127.0.0.1:5000/download-all" target="_blank">Download All</a><br><br>';
            // List all generated class files as links
            data.files.forEach(file => {
                outputContent += `<a href="http://127.0.0.1:5000/download/${file.name}" target="_blank">${file.name}</a><br>`;
            });
            outputJson.innerHTML = outputContent;
        })
        .catch(error => {
            console.error('Error:', error);
            outputJson.value = 'An error occurred while processing the JSON.';
        });

    } catch (error) {
        outputJson.value = "Invalid JSON: " + error.message;
        outputJson.style.color = "red";
    }
});
