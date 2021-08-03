
//Alles was mit drag und drop zu tun hat
var cocktailID;
var PlacedField;
var AusgewaehlteZutaten = [16];
var rows = 2;
var cols = 16;
var PlazierteZutaten= new Array(rows);
for (var i = 0; i < rows; i++) {
    PlazierteZutaten[i] = new Array(cols);
}
for (var i = 0; i < cols; i++) {
    var b = i + 1;
    PlazierteZutaten[0][i] = b;
    PlazierteZutaten[1][i] = -1;
}
function allowDrop(ev) {
    //Pass all parameters who are allowed to be dragged
   
        ev.preventDefault();
    
}

function drag(ev) {
    //Hier kann ich id abrufen
    //console.log(ev.target.id);
    //cocktailID = ev.targed.id;
    //console.log(cocktailID);
    foo(ev.target.id);
    ev.dataTransfer.setData("image", ev.target.id);
}
function foo(id) {
    cocktailID = id;
    //console.log(cocktailID);
}


function drop(ev, feld) {
    //hier feld
    //console.log(feld);
    //console.log(cocktailID);
    ev.preventDefault();
    PlacedField = feld;
    if (feld != 2) {
        if (PlazierteZutaten[1][feld] == -1) {
            PlazierteZutaten[1][feld] = cocktailID;
        } else {
            alert("Platz bereits belegt");
        }
    } else {
        alert("Dieser Platz darf nicht beschrieben werden");
    }
    var a = PlazierteZutaten[1][feld];
    console.log(a);
    console.log(PlacedField);
    //fillArray();
    var data = ev.dataTransfer.getData("image");
    ev.target.appendChild(document.getElementById(data));
    //erstelle Post Request
    data = "ArrID: " + feld + ", ID: " + cocktailID;
    sendJSON("KONF_ALK", data);
    //fetch('http://localhost:8000',
    //    {
    //        method: 'POST',
    //        body: JSON.stringify({
    //            if()
    //            BEFEHL: "KONF_ALK",
    //            belegteZelle: feld,
    //            ID: cocktailID
    //        }),
    //        headers: {
    //            "Content-type": "application/json; charset=UTF-8"
    //        }

    //    })
    //    .then((response) => response.json())
    //    .then((json)=>console.log(json));
    
}

function drop_nonAlk(ev, feld) {
    //hier feld
    //console.log(feld);
    //console.log(cocktailID);
    ev.preventDefault();
    if (PlazierteZutaten[1][feld] == -1) {
        PlazierteZutaten[1][feld] = cocktailID;
    } else {
        alert("Platz bereits belegt");
    }
    PlacedField = feld;
    var a = PlazierteZutaten[1][feld];
    console.log(a);
    console.log(PlacedField);
    //fillArray();
    var data = ev.dataTransfer.getData("image");
    ev.target.appendChild(document.getElementById(data));
    //erstelle Post Request
    data = "ArrID: " + feld + ", ID: " + cocktailID;
    sendJSON("KONF_KAN", data);
    

}

function sendJSON(befehl, data) {
    fetch('http://localhost:8000',
        {
            method: 'POST',
            body: JSON.stringify({
               
                Befehl: befehl,
               data
            }),
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }

        })
        .then((response) => response.json())
        .then((json) => console.log(json));
}
