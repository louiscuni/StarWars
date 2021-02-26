function readfile(){
    document.querySelector("#read-button").addEventListener('click', function() {
        if(document.querySelector("#file-input").files.length == 0) {
            alert('Error : No file selected');
            return;
        }

        // fichier selectionne 
        let file = document.querySelector("#file-input").files[0];

        // new FileReader object
        let reader = new FileReader();

        // fichier charge
        reader.addEventListener('load', function(e) {
           // contenu
            let text = e.target.result;

            document.querySelector("#file-contents").textContent = text;
            console.log('file loaded', reader.result);
        });

        // event fired when file reading failed
        reader.addEventListener('error', function() {
            alert('Error : Failed to read file');
        });

        //read file as text file
        reader.readAsText(file);
    });
}
readfile();