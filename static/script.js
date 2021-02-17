function updateScroll(){
    var element = document.getElementById("message-body-id");
    element.scrollTop = element.scrollHeight;
}

updateScroll();

// Add slideDown animation to Bootstrap dropdown when expanding.
$(document).ready(function(){
  
  $('.dropdown').on('show.bs.dropdown', function() {
    $(this).find('.dropdown-menu').first().stop(true, true).slideDown(100);
  });

  // Add slideUp animation to Bootstrap dropdown when collapsing.
  $('.dropdown').on('hide.bs.dropdown', function() {
    $(this).find('.dropdown-menu').first().stop(true, true).slideUp(100);
  });


});