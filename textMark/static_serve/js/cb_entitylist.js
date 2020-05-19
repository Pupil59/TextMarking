$(document).ready(function()
{
  var name = $("#entity_name").val();
  //location.reload();
  $.ajax({
    type:"GET",
    url:"/api/project/entities?action=list_entity",
    success:function (data) {
        console.log((data));
        for (var i = data.retlist.length - 1; i >= 0; i--) {
          $("#submene").append($("<li id = \"en" + data.retlist[i].id + "\">" + (data.retlist[i].name) + "</li>"));
        }
    },
    error:function (data) {
        //console.log("error");
    },
    complete: function (data) {
        //console.log("complete");
    },
  });

  $("#mymenu ul li").next("ul").hide();
  $("#mymenu ul li").click(function()
  {
    $(this).next("ul").toggle();
  });
});

// $("#id0").click(function()
// {

// });
$(document).on("click","#submene li",function(){
  var status = confirm("del?");
  if (!status) {return false;}
  console.log($(this)[0].id);
  $.ajax({
  type:"DELETE",
  url:"/api/project/entities",
  contentType: "application/json",
  dataType:"json",
  async:false,
  data:JSON.stringify({
    "action":"del_entity",
    "id": $(this)[0].id.slice(2)
  }),
  success:function (data) {
      console.log((data));
  },
  error:function (data) {
      console.log("error");
  },
  complete: function (data) {
      console.log("complete");
  },
  });
  location.reload();
});