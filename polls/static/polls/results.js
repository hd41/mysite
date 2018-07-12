$(document).ready(function(e) {
   // your code here
  console.log("hi there!!");

  $("#sub").click(function(){
      var tmp = $("#param").val();
      var choice = $("input[name='choice']:checked").val();
      console.log(choice);
      var csrf  = $("input[name='csrfmiddlewaretoken']").val();
      console.log(csrf);
      // var link =
      $.post("/polls/resp/",
      {
          'param': tmp,
          'opt': choice,
          'csrfmiddlewaretoken': csrf,
      },
      function(data, status){
        console.log(data);
        var res="";
        for (var k in data){
          res+= k +'&emsp;&emsp;'+ data[k]+'</br>';
        }

        $("#div1").html((res));
      });
      console.log("asdasd");
  });

});
