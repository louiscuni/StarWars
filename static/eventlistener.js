function readfile(){
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
        $("#print_file").text(formatFileEmpire(text));

        $.getJSON('/machine_a_laver', 
        {
        data : text,
        }, 
        function(res) {
            $("#result").text("C3PO : la probabilité d'atteindre notre destination est de " + res.result[0] + '%');
            $('#answer').text(getAnswer(res.result[0]));
            $('#road').text(formatRoad(res.result[1]));
            //$("#result").image($("#c3po"));
            
        });

    });

    // event fired when file reading failed
    reader.addEventListener('error', function() {
        alert('Error : Failed to read file');
    });

    //read file as text file
    reader.readAsText(file);
    return false;
}

function fileloaded(){
       $("#loader").text("C3PO : j'intercepte de nouveaux fichiers de la resistance");
}

function formatFileEmpire(str){
    var res = str.replace(/\n/g , "");
    res = res.replace(/{/g, "\n");
    res = res.replace(/,/g, "\n");
    res = res.replace(/}/g, "");
    return res;
}

function formatRoad(road){
    var res = road.toString();
    console.log(typeof(res));
    res = res.replace(/,\d,/g, "  ");
    res = res.replace(/,\d\d,/g, "  ");
    res = res.replace(/,\d\d\d,/g, "  ");
    res = res.replace(/,\d\d/g, "");
    return res;
}

function getAnswer(proba){
    switch (true){
        case (proba > 90):
            return "HAN : C'est vraiment trop facile";
        case (proba > 50):
            return "HAN : Si on reussi à eviter que les bonnes femmes s'en mèlent, on devrait pouvoir se tirer de là";
        case (proba > 30):
            return "HAN : je crois qu'on va tous maigir d'un coup";
        default:
            return "CHEWE : heeeennnnnww !!!"
    }
}