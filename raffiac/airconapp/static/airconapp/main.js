var btn = document.getElementById('btn')
var container = document.getElementById('ourcontainer')
var url = 'http://127.0.0.1:8000/api/'

$.ajax({
    method: 'GET',
    url: url,
    success: function(data) {
        console.log(data)
        console.log('success')
    },
    error: function(error_data) {
        console.log('error')
    }
})

$('.model').change(function() {
    var ourRequest = new XMLHttpRequest();
    ourRequest.open("GET", url);
    ourRequest.onload = function(){
        var OurData = JSON.parse(ourRequest.responseText);
        renderHTML(OurData);
    }
    ourRequest.send()
});


function renderHTML(data) {
    var displayunit = $('.model option:selected').not('#default').text();
    var htmlString = "";
    for (i=0; i < data.length; i++){
    };


