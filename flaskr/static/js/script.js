$(function() {
    $('button#button').bind('click', function() {
    $.getJSON('/translated', {
  
      input: $('input[id="inputText"]').val(),
      target_lang: $('select[id="target_lang"]').val(),
  
    }, function(data) {
      $("#result").html('');
      $("#result").append(
       <p>{data.result}</p>
      ).show('slow');
    });
    return false;
    });
  });
  
  
  $("#button-one").click(function(event){
    event.preventDefault();
    $(".tax-discount").slideToggle("slow");
  }); 
  
  $("#button-two").click(function(event){
    event.preventDefault();
    $(".tax-discount-kids").slideToggle("slow");
  });  