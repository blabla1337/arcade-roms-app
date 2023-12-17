$(document).ready(function() {
  // Handle click event on each slide except when clicking on form elements
  $('.slide').on('click', function(event) {
    if (!$(event.target).closest('form').length) {
      var $this = $(this);
      $this.toggleClass('expand').find('.slide-content').slideToggle();
      $this.siblings('.expand').removeClass('expand').find('.slide-content').slideUp();
    }
  });

  // Prevent click event inside the form from propagating to the slide
  $('.slide form').on('click', function(event) {
    event.stopPropagation();
  });
});

$(document).ready(function() {
  $('#file-upload').change(function() {
    // Get the file name
    var fileName = $(this).val().split('\\').pop();
    // Replace the "Select File" text with the file name
    $(this).next('.custom-file-upload').text(fileName.length > 0 ? fileName : 'Select File');
  });
});
