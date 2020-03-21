$("#id_brand").change(function () {
  var url = $("#ACServiceCalcForm").attr("data-models-url");
  var brandId = $(this).val();

  $.ajax({
    url: url,
    data: {
      'brand': brandId
    },
    success: function (data) {
      $("#id_model").html(data);
    }
  });

});

$('#calculate').click(function(){
    var sqrFt = $('#id_square_feet').val()
    aler(sqrFt)
})


