$(document).ready(function()
{
  var name = $("#entity_name").val();
  //location.reload();
  $.ajax({
    type:"GET",
    url:"/api/project/relations?action=list_type",
    async:false,
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
  var relId = $(this)[0].id.slice(2);
  var status = confirm("确定删除该关系类型么？");
  if (!status) {return false;}
  if (relId == 0 || relId == 1 || relId == 2) {
    alert("初始关系不能删除！");
    return false;
  }
  console.log($(this)[0].id);
  $.ajax({
  type:"DELETE",
  url:"/api/project/relations",
  contentType: "application/json",
  dataType:"json",
  async:false,
  data:JSON.stringify({
    "action":"del_type",
    "id": relId
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
