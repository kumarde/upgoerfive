$(document).ready(function(){
  $("#submit-form").bind('click', function(e){
    e.preventDefault();
    console.log($SCRIPT_ROOT)
    $.getJSON($SCRIPT_ROOT + '/sentence', {
      sentence: $("#input.centered").val()
    }, function(data){
      $('#theData').text(data.sentence)
    });
    return false
  })
})
