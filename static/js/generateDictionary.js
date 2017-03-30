var className1 = "";

function displayDictionary()
{
var className = $('#DictionaryClass').val();
className1 = className;
var html = [
    '<td><div class="col-xs-2 col-md-2" ><label for="class">Class</label>',
   '<select id="DictionaryClassNum" class="form-control" id="class" style="height:40;" onchange="registerName(this.value);">',
   '<option selected>Select File</option>',
    '<option>8</opton>',
    '<option>11</opton>',
    '<option>15</opton>',
     '</select>',
     '</div></td>',
    '<td><div class="col-xs-2 col-md-2"><label for="obisCode">Obis Code</label><input class="form-control" id="obisCode" type="text" style="height:40;" maxlength="12" pattern="[A-Za-z]{3}"></div></td>',
    '<td><div class="col-xs-2 col-md-2" id="Description"><label for="Description">Description</label><input class="form-control" id="Descrip" type="text" style="height:40;" readonly="readonly" ></div></td>',
     '<td><div class="col-xs-2 col-md-2" id="Version"><label for="Version">Version</label><input class="form-control" id="dictVersion" type="text" style="height:40;" readonly="readonly"></div></td><br ><br ><br ><br >',
     '<td><div id="textareaContent2" class="table-responsive"></div></td>',
     '<td><div id="textareaContent3" class="table-responsive"></div></td> ',
].join('');
document.getElementById('mydivtag').innerHTML =html;
}
/***********************************************************/
  function registerName(valueSent) {
  var x= className1+"\\class_"+valueSent;
    function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
      $.ajax({
          type: "POST",
          cache: true,
          url: "/parseXML/",
          data:  { id : x, name: valueSent },
            success: function(result, textStatus, jqXHR)
            {
            var methods = '<label for="textareaContent3">Methods</label><tr><td>'+result.methods;
            s = result.dictId;
            switch (parseInt(s)) {
              case 8:
                    var table8 = result.association.split('\n');
                    var tableAsssociation8 = result.associationMethods.split('\n');
                    break;
               case 11:
                    var table11 = result.association.split('\n');
                    break;
               case 15:
                    var table15 = result.association.split('\n');
                    break;
               default:
                    alert('No assignement !!');
                    break;
              }
            var res1 = [
            methods.replace(/(\r\n|\n|\r)/gm,'</td><td><div data-placement="top" data-toggle="tooltip" title="Edit" ><button onclick="fonc2(this.id);" style="float: right;" class="btn btn-primary btn-xs" data-title="Edit" data-toggle="modal" data-target="#methods" ><span class="glyphicon glyphicon-pencil"></span></button></div></td></tr><tr><td>'),
            '<div class="modal fade" id="methods" tabindex="-1" role="dialog" aria-labelledby="edit" aria-hidden="true">',
            '<div class="modal-dialog">',
            '<div class="modal-content">',
            '<div class="modal-header">',
            '<button type="button" class="close" data-dismiss="modal" aria-hidden="true"><span class="glyphicon glyphicon-remove" aria-hidden="true"></span></button>',
            '<div class="modal-body">',
            '<div class="form-group">',
            '</div></div>',
            '<div class="modal-footer ">',
            '<center>',
            '<button id="temporary" class="btn btn-primary "data-toggle="modal" data-target="" onclick="fonc1();">OK</button></center>',
            '</div></div></div></div>'
            ].join('');
            $("#textareaContent3 ").html('<table id="mytable" class="table table-bordred table-striped">'+res1+'</tr></table>');
            var strUser = document.getElementById("DictionaryClassNum").options[document.getElementById("DictionaryClassNum").selectedIndex].text;
            if(strUser==8){
            var i;
                for(i=0;i<tableAsssociation8.length;i++){
                    $("#textareaContent3 ").find(".form-group").append('<table><tr><td><h4>'+tableAsssociation8[i]+':&nbsp;&nbsp;&nbsp;</h4></td><td><p>&nbsp;Get&nbsp;<input type="checkbox" name ="'+tableAsssociation8[i]+'" class="checkthis" value="Get"/></p></td><td><p>&nbsp;&nbsp;&nbsp;Set&nbsp;<input type="checkbox" name ="'+tableAsssociation8[i]+'" class="checkthis" value="Set"/></p></td><td><p>&nbsp;&nbsp;&nbsp;Action&nbsp;<input type="checkbox" name ="'+tableAsssociation8[i]+'" class="checkthis" value="Action"/></p></td></tr></table>');
                    }
                }
            /**************************************/
//             $("#textareaContent3 ").html('<table class="table table-bordred table-striped">'+res1+'</td></tr></table>');
            $("#Description").find(".form-control").val(result.dictDescription);
            $("#Version").find(".form-control").val(result.dictVersion);
            var text= '<label for="mytable">Attributes</label><tr><td>'+result.stat;
            var res = [
             text.replace(/(\r\n|\n|\r)/gm,'</td><td><div data-placement="top" data-toggle="tooltip" title="Edit"><button onclick="fonc2(this.id);" class="btn btn-primary btn-xs" data-toggle="modal" data-target="#edit"><span class="glyphicon glyphicon-pencil"></span></button></div></td></tr><tr><td>'),
            '<div class="modal fade" id="edit" tabindex="-1" role="dialog" aria-labelledby="edit" aria-hidden="true">',
            '<div class="modal-dialog">',
            '<div class="modal-content">',
            '<div class="modal-header">',
            '<button type="button" class="close" onclick="$(this).parent().hide();">×</button>',
            '<div class="modal-body">',
            '<div class="form-group">',
            '</div></div>',
            '<div class="modal-footer ">',
            '<center>',
            '<button id="temporary" class="btn btn-primary "data-toggle="modal" data-target="" onclick="fonc1(this.id);">OK</button></center>',
            '</div></div></div></div>'
            ].join('');
            $("#textareaContent2 ").html('<table id="mytable" class="table table-bordred table-striped">'+res+'</tr></table>');
            var strUser = document.getElementById("DictionaryClassNum").options[document.getElementById("DictionaryClassNum").selectedIndex].text;
            var i= 0;
            $('.btn').each(function(){
            $(this).attr('id', i++);
             });
            var i=0;
            if(strUser==8){
                for(i=0;i<table8.length;i++){
                    $("#textareaContent2 ").find(".form-group").append('<table><tr><td><h4>'+table8[i]+':&nbsp;&nbsp;&nbsp;</h4></td><td><p>&nbsp;Get&nbsp;<input type="checkbox" name ="'+table8[i]+'" class="checkthis" value="Get"/></p></td><td><p>&nbsp;&nbsp;&nbsp;Set&nbsp;<input type="checkbox" name ="'+table8[i]+'" class="checkthis" value="Set"/></p></td><td><p>&nbsp;&nbsp;&nbsp;Action&nbsp;<input type="checkbox" name ="'+table8[i]+'" class="checkthis" value="Action"/></p></td></tr></table>');
                    }
                }else if(strUser==11){
                    for(i=0;i<table11.length;i++){
                    $("#textareaContent2 ").find(".form-group").append('<table><tr><td><h4>'+table11[i]+':&nbsp;&nbsp;&nbsp;</h4></td><td><p>&nbsp;Get&nbsp;<input type="checkbox" name ="'+table11[i]+'" class="checkthis" value="Get"/></p></td><td><p>&nbsp;&nbsp;&nbsp;Set&nbsp;<input type="checkbox" name ="'+table11[i]+'" class="checkthis" value="Set"/></p></td><td><p>&nbsp;&nbsp;&nbsp;Action&nbsp;<input type="checkbox" name ="'+table11[i]+'" class="checkthis" value="Action"/></p></td></tr></table>');
                    }
                }else if(strUser==15){
                    for(i=0;i<table15.length;i++){
                    $("#textareaContent2 ").find(".form-group").append('<table><tr><td><h4>'+table15[i]+':&nbsp;&nbsp;&nbsp;</h4></td><td><p>&nbsp;Get&nbsp;<input type="checkbox" name ="'+table15[i]+'" class="checkthis" value="Get"/></p></td><td><p>&nbsp;&nbsp;&nbsp;Set&nbsp;<input type="checkbox" name ="'+table15[i]+'" class="checkthis" value="Set"/></p></td><td><p>&nbsp;&nbsp;&nbsp;Action&nbsp;<input type="checkbox" name ="'+table15[i]+'" class="checkthis" value="Action"/></p></td></tr></table>');
                    }
                }

            }

        });
}

var idAttr;
function fonc2(c){
idAttr = c;
alert(idAttr);
}
function fonc1(x) {
    var choices = "";
    var els = document.getElementsByClassName('checkthis');
    for (var i=0;i<els.length;i++){
      if ( els[i].checked ) {
        choices+="@"+ els[i].name+":"+els[i].value;
      }
    }
     var element = $(this);
    function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
      $.ajax({
          type: "POST",
          cache: true,
          url: "/createTemporary/",
          data:  { checks : choices, idAttr: idAttr },
            success: function(result) {
//            window.alert('m');
            }
        });

        $('#mydivtag').hide();
}