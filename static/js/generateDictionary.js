var className1 = "";

function displayDictionary()
{
var className = $('#DictionaryClass').val();
className1 = className;
var html = [
    '<td><div class="col-xs-2 col-md-2" ><label for="class">Class</label>',
   '<select id="DictionaryClassNum" class="form-control" id="class" style="height:40;" onchange="registerName(this.value);">',
   '<option selected>Select Class</option>',
    '<option>8</opton>',
    '<option>11</opton>',
    '<option>15</opton>',
     '</select>',
     '</div></td>',
    '<td><div class="col-xs-2 col-md-2"><label for="obisCode">Obis Code</label><input class="form-control" id="obisCode" name="obisCode" type="text" style="height:40;" pattern="[a-f0-9]{12}++(?<!\ff)$" title="Obis code should contain 6 octet"  required/><input type="submit" id="primaryButton" style="display: none;"></div></td>',
    '<td><div class="col-xs-2 col-md-2" id="Description"><label for="Description">Description</label><input class="form-control" id="Descrip" type="text" style="height:40;" readonly="readonly" ></div></td>',
     '<td><div class="col-xs-2 col-md-2" id="Version"><label for="Version">Version</label><input class="form-control" id="dictVersion" type="text" style="height:40;" readonly="readonly"></div></td><br ><br ><br ><br >',
     '<td><div id="textareaContent2" class="table-responsive"></div></td>',
     '<td><div id="textareaContent3" class="table-responsive"></div></td> ',
].join('');
document.getElementById('mydivtag').innerHTML = html;
}
/***********************************************************/
  function registerName(valueSent) {
  var x= className1;
    f();
      $.ajax({
          type: "POST",
          cache: true,
          url: "/parseXML/",
          data:  { id : x, name: valueSent },
            success: function(result, textStatus, jqXHR)
            {
            var test_str = result.stat;
            var start_pos = 0;
            var end_pos = 0;
            var longest = '';
            var second_longest = '';
            while(end_pos != -1){
                end_pos = test_str.indexOf('\n', start_pos)
                len = test_str.substring(start_pos, end_pos);
                start_pos  = end_pos+1;
                if(longest.length < len.length){
                second_longest  = longest;
                longest = len;
                }
            }
            s = result.dictId;
            var table8 = result.association.split('\n');
            var tableAsssociation8 = result.associationMethods.split('\n');
//            switch (parseInt(s)) {
//              case 8:
//                    var table8 = result.association.split('\n');
//                    var tableAsssociation8 = result.associationMethods.split('\n');
//                    break;
//               case 11:
//                    var table11 = result.association.split('\n');
//                    break;
//               case 15:
//                    var table15 = result.association.split('\n');
//                    break;
//               default:
//                    alert('No assignement !!');
//                    break;
//              }
              var j=0;
            var meth='<label for="textareaContent3">Methods</label><tr><td>&nbsp;</td><td>';
              var elementAction1 = '';
              var elementAction2 = '';
            for(j=0;j<table8.length;j++){
                    meth += '<b>'+table8[j]+'</b><br><i>Get Set Action</i></td><td>';
                    elementAction2 +='</td><td style="display:none;"><table><tr><td><input type="checkbox" name ="'+table8[j]+'" class="checkthis classCheckbox1" value="Get"/>&nbsp;&nbsp;&nbsp;&nbsp;</td><td><input type="checkbox" name ="'+table8[j]+'" class="checkthis  classCheckbox1" value="Set"/>&nbsp;&nbsp;&nbsp;&nbsp;</td><td><input type="checkbox" name ="'+table8[j]+'" class="checkthis classCheckbox1" value="Action"/>&nbsp;</td></tr></table></td>'
                    elementAction1 += '</td><td><table><tr><td><input type="checkbox" name ="'+table8[j]+'" class="checkthis classCheckbox1" value="Get"/>&nbsp;&nbsp;&nbsp;&nbsp;</td><td><input type="checkbox" name ="'+table8[j]+'" class="checkthis  classCheckbox1" value="Set"/>&nbsp;&nbsp;&nbsp;&nbsp;</td><td><input type="checkbox" name ="'+table8[j]+'" class="checkthis classCheckbox1" value="Action"/>&nbsp;</td></tr></table></td>'
                     }
                     elementAction2 += '</tr><tr><td>';
                    elementAction1 += '</tr><tr><td>';
                    meth += '</td></tr><tr><td>';
            var methods1= result.methods;
            methods1  = meth + methods1 + '<span style="color:white;">' + second_longest +  '</span>' + elementAction2;
            var res1 = [
             methods1.replace(/(\r\n|\n|\r)/gm,elementAction1),
            ].join('');
            $("#textareaContent3 ").html('<table id="mytable" class="table table-bordred table-striped" width="100%">'+res1+'</tr></table>');
            var strUser = document.getElementById("DictionaryClassNum").options[document.getElementById("DictionaryClassNum").selectedIndex].text;
            var n= 0;

            $('.classCheckbox1').each(function(){
            var sid = Math.floor(n/(3*table8.length))+1;
            $(this).attr('id', 'm' + sid.toString());
            n++;
             });

            if(strUser==8){
             i= 0;
                for(i=0;i< table8.length;i++){
                    $("#textareaContent3 ").find(".form-group").append('<table><tr><td><h4>'+table8[i]+':&nbsp;&nbsp;&nbsp;</h4></td><td><p>&nbsp;Get&nbsp;<input type="checkbox" name ="'+table8[i]+'" class="checkthis class" value="Get"/></p></td><td><p>&nbsp;&nbsp;&nbsp;Set&nbsp;<input type="checkbox" name ="'+table8[i]+'" class="checkthis" value="Set"/></p></td><td><p>&nbsp;&nbsp;&nbsp;Action&nbsp;<input type="checkbox" name ="'+table8[i]+'" class="checkthis" value="Action"/></p></td></tr></table>');
                    }
                }
            /**************************************/
//             $("#textareaContent3 ").html('<table class="table table-bordred table-striped">'+res1+'</td></tr></table>');
            $("#Description").find(".form-control").val(result.dictDescription);
            $("#Version").find(".form-control").val(result.dictVersion);
            var i=0;
            var txt2='<label for="mytable">Attributes</label><tr><td>&nbsp;</td><td>';
            var elementAction = '';
            for(i=0;i<table8.length;i++){
                    txt2 += '<b>'+table8[i]+'</b><br><i>Get Set Action</i></td><td>';
                    elementAction += '</td><td><table><tr><td><input type="checkbox" name ="'+table8[i]+'" class="checkthis classCheckbox" value="Get"/>&nbsp;&nbsp;&nbsp;&nbsp;</td><td><input type="checkbox" name ="'+table8[i]+'" class="checkthis classCheckbox" value="Set"/>&nbsp;&nbsp;&nbsp;&nbsp;</td><td><input type="checkbox" name ="'+table8[i]+'" class="checkthis classCheckbox" value="Action"/>&nbsp;</td></tr></table></td>'
                     }
                    elementAction += '</tr><tr><td>'
                    txt2 += '</td></tr><tr><td>'
            var text= txt2+result.stat;

            var res = [
             text.replace(/(\r\n|\n|\r)/gm,elementAction),
            ].join('');

            $("#textareaContent2 ").html('<table id="mytable" class="table table-bordred table-striped">'+res+'</tr></table>');
            var strUser = document.getElementById("DictionaryClassNum").options[document.getElementById("DictionaryClassNum").selectedIndex].text;
            var l= 0;

            $('.classCheckbox').each(function(){
            var sid = Math.floor(l/(3*table8.length))+1;
            $(this).attr('id', 'a' + sid.toString());
            l++;
             });

            var i = 0;
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
    var choices = '';
    var els = document.getElementsByClassName('checkthis');
    
    for (var i=0;i<els.length;i++){
      if ( els[i].checked ) {
        choices+="@"+ els[i].name+":"+els[i].value;
      }
    }

     var element = $(this);
    f();
      $.ajax({
          type: "POST",
          cache: true,
          url: "/createTemporary/",
          data:  { checks : choices, idAttr: idAttr },
            success: function(result) {
//         
            }
        });
        return;
}
//function validation2()
//{
//    document.getElementById('primaryButton').value=1;
//     document.getElementById("primaryButton").setCustomValidity("ERROR");
//    alert(document.getElementById('primaryButton').value);
//    return 0;
//}
$(function(){
    $("#obisCode").oninvalid = function () {
        this.setCustomValidity("Please enter at least 5 characters.");
        this.setCustomValidity("");
    };
});
