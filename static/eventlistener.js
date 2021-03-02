function controller_front(){
    //read file-input, call backend and print res
    if(document.querySelector("#file-input").files.length == 0) {
        alert('Error : No file selected');
        return;
    }

    let file = document.querySelector("#file-input").files[0];
    let reader = new FileReader();

    // event fired when file loaded
    reader.addEventListener('load', function(e) {
        let text = e.target.result;
        $("#print_file").text(formatFileEmpire(text));

        $.getJSON('/back_end', 
        {
        data : text,
        }, 
        function(res) {
            $("#result").text("C3PO : la probabilité d'atteindre notre destination est de " + res.result[0] + '%');
            $('#answer').text(getAnswer(res.result[0]));
            $('#road').text(formatRoad(res.result[1]));
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
    //print text when file loaded
       $("#loader").text("C3PO : j'intercepte de nouveaux fichiers de la resistance");
}

function formatFileEmpire(str){
    //change str format for printing
    var res = str.replace(/\n/g , "");
    res = res.replace(/{/g, "\n");
    res = res.replace(/,/g, "\n");
    res = res.replace(/}/g, "");
    return res;
}

function formatRoad(road){
    //change str format for printing
    var res = road.toString();
    console.log(typeof(res));
    res = res.replace(/,\d,/g, "  ");
    res = res.replace(/,\d\d,/g, "  ");
    res = res.replace(/,\d\d\d,/g, "  ");
    res = res.replace(/,\d\d/g, "");
    return res;
}

function getAnswer(proba){
    //print answer based on sucess probability
    switch (true){
        case (proba > 90):
            return "HAN : C'est vraiment trop facile";
        case (proba > 50):
            return "LEIA : Il faut toujours garder espoir";
        case (proba > 30):
            return "HAN : je crois qu'on va tous maigir d'un coup";
        default:
            return "CHEWE : heeeennnnnww !!!"
    }
}