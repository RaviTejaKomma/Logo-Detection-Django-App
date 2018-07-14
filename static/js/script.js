function readURL(input) {

  if (input.files && input.files[0]) {
    let reader = new FileReader();

    reader.onload = function(e) {
      $('#img-preview').attr('src', e.target.result);
    }

    reader.readAsDataURL(input.files[0]);
  }
}

$("#file_upload").change(function() {
            readURL(this);
});

