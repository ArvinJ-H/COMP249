function add_people(data) {
    var element = document.getElementById('people');
    var list = "<ul>";
    for (var i = 0; i < data.length; i++) {

        list += "<li>" + data[i].name + "<img src=" + data[i].picture + "</img>" + "</li>"
    }
    list += "<ul>"

    element.innerHTML = list;
}

window.onload = function () {
    add_people(people);
}