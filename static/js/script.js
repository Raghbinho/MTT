
var nb=0;
var depasse=0;
var nbclickAttr=0;
var nbclickmethod=0;
var ch="";
var ch2="";
var count=0;
var val1="";

var listCh=[];
var listCh2=[];
var countCh=-1;


var idselect=1;
var idselect2=0;

var idsize=1;
var idsize2=1;

var nbappel=0;
var nbappel2=0;

var myArray = new Array();
var tab=new Array();

var myArray2=new Array();
var tab2=new Array();


var nb_btn_clicked=0;
var nb_btn_clickedMethod=0;

 var indice=0;
 var indice2=0;

 var nbElement=0;
 var nbElement2=0;

 var nbclicstructure=0;
  var nbclicstructure2=0;

$(document).ready(function(){
try {
try {

    console.log("start");
      $('input#submit').click(function(){
        idselect++;

        idsize++;
        nbremove=0;
//        indice=0;
        ch="";
        countCh++;

//          element = $('<input class="form-control" type="text"/>');
            var attrSize=0;
            var nb_btn_clicked=0;
             nbclickAttr++;
             for(i=0;i<myArray.length;i++)
             {
             myArray[i]="";
             }

          element = $('<tr style="border-bottom: 1px solid LightSteelBlue;" id=><td > ' +
                       ' <input class="form-control" type="text"    name="AttributeID-' + idselect + '"> '+
                    '</td>' +

                    '<td >'+
                        '<input class="form-control" type="text"  name="AttributeName-' + idselect + '">'+
                    '</td>'+
                    '<td >'+
                     '<select  class="form-control" name="attributeType-' + idselect + '" id="attributeType-' + idselect + '" >'+
                        '<option value="Select type" selected="selected">Select type</option>'+
                        '<optgroup label="Simple Type">'+
                            '<option value="null-data">null-data</option>'+
                            '<option value="boolean">boolean</option>'+
                            '<option value="bit-string">bit-string</option>'+
                            '<option value="double-long">double-long</option>'+
                            '<option value="double-long-unsigned">double-long-unsigned</option>'+
                            '<option value="octet-string">octet-string</option>'+
                            '<option value="visible-string">visible-string</option>'+
                            '<option value="utf8-string">utf8-string</option>'+
                            '<option value="bcd">bcd</option>'+
                            '<option value="integer">integer</option>'+
                            '<option value="long">long</option>'+
                            '<option value="unsigned">unsigned</option>'+
                            '<option value="long-unsigned">long-unsigned</option>'+
                            '<option value="long64">long64</option>'+
                            '<option value="long64-unsigned">long64-unsigned</option>'+
                            '<option value="enum">enum</option>'+
                            '<option value="float32">float32</option>'+
                            '<option value="float64">float64</option>'+
                            '<option value="date-time">date-time</option>'+
                            '<option value="date">date</option>'+
                            '<option value="time">time</option>'+

                        '</optgroup>'+
                        '<optgroup label="Complex Type">'+
                            '<option value="array">array</option>'+
                            '<option value="structure">structure</option>'+
                            '<option value="compact array">compact array</option>'+
                            '<option value="CHOICE">CHOICE</option>'+
                        '</optgroup>'+
                     '</select>'+
                    '</td>'+
                 ' <td >'+
                    '<input class="form-control" type="text" name="attributesize-' + idsize + '"  id="attributesize-' + idsize + '" onchange="GetArraySize(this.value,this)" >' +
                  '</td>'+
                  ' <td width="100px">'+
                  '<input class="btn btn-danger" type="button" value="Remove" onclick="remove(this)">' +
                   '<input type="hidden" name="nbligne" value='+idselect+'>'+

                    '</td>'+

                '</tr>');
          $("#table_class").append(element);

//type=document.getElementById("AttributeType").selected;


//if(type=="unsigned")
//{
//document.getElementById("atributesize").value="0";
//}



//if (selected=="unsigned")
//{
//document.getElementById("atributesize").value="0";
//
//}


          return false;

      });






        $('input#methodsubmit').click(function(){
        alert()
        idselect2++;

        idsize2++;
        nbremove2=0;
        indice2=0;
        ch2="";
//          element = $('<input class="form-control" type="text"/>');
            var methodSize=0;
            var nb_btn_clickedMethod=0;
             nbclickmethod++;
             for(i=0;i<myArray2.length;i++)
             {
             myArray2[i]="";
             }
          element = $('<tr style="border-bottom: 1px solid LightSteelBlue;"><td > ' +
                       ' <input class="form-control" type="text" name="MethodeID-' + idselect2 + '" id="MethodeID-' + idselect2 + '" > '+
                    '</td>' +

                    '<td >'+
                        '<input class="form-control" type="text" name="methodName-' + idselect2 + '"  >'+
                    '</td>'+
                    '<td >'+
                     '<select  class="form-control"  id="methodType-' + idselect2 + '"  name="methodType-' + idselect2 + '" >'+
                        '<option value="Select type" selected="selected">Select type</option>'+
                        '<optgroup label="Simple Type">'+
                            '<option value="null-data">null-data</option>'+
                            '<option value="boolean">boolean</option>'+
                            '<option value="bit-string">bit-string</option>'+
                            '<option value="double-long">double-long</option>'+
                            '<option value="double-long-unsigned">double-long-unsigned</option>'+
                            '<option value="octet-string">octet-string</option>'+
                            '<option value="visible-string">visible-string</option>'+
                            '<option value="utf8-string">utf8-string</option>'+
                            '<option value="bcd">bcd</option>'+
                            '<option value="integer">integer</option>'+
                            '<option value="long">long</option>'+
                            '<option value="unsigned">unsigned</option>'+
                            '<option value="long-unsigned">long-unsigned</option>'+
                            '<option value="long64">long64</option>'+
                            '<option value="long64-unsigned">long64-unsigned</option>'+
                            '<option value="enum">enum</option>'+
                            '<option value="float32">float32</option>'+
                            '<option value="float64">float64</option>'+
                            '<option value="date-time">date-time</option>'+
                            '<option value="date">date</option>'+
                            '<option value="time">time</option>'+

                        '</optgroup>'+
                        '<optgroup label="Complex Type">'+
                            '<option value="array">array</option>'+
                            '<option value="structure">structure</option>'+
                            '<option value="compact array">compact array</option>'+
                            '<option value="CHOICE">CHOICE</option>'+
                        '</optgroup>'+
                     '</select>'+
                     '</td> ' +
                     '<td >' +
                    '<input class="form-control" type="text" name="methodsize-' + idselect2 + '"id="methodsize-' + idselect2 + '"onchange="MethodGetArraySize(this.value,this)">' +
                    '</td>'+
                    '<td > '+
                     '<input class="btn btn-danger"type="button" value="Remove" onclick="remove2(this)" >'+
                     '<input type="hidden" name="nbligne2" value='+idselect2+'>'+
                    '</td>'+
                '</tr>');
          $("#table_methode").append(element);

          return false;
      });



  }
  finally {
    console.log("finally");
  }
  }
  catch(e)
  {
    console.log("Erreur");
  }
});

 function GetSelectedTextValue(attributeType) {
        var selectedText = attributeType.options[attributeType.selectedIndex].innerHTML;
        var selectedValue = attributeType.value;

        if (selectedValue=="array")

        {







           element = $('<tr style="border-bottom: 1px solid LightSteelBlue;"><td width="300px"></td><td width="300px" > ' +
          '</td>'+
                    '<td width="300px">'+
                     '<select  class="form-control" name="AttributeTypeArray" id="attributeTypeArray" >'+
                        '<option value="Select type" selected="selected">Select type</option>'+
                        '<optgroup label="Simple Type">'+
                            '<option value="null-data">null-data</option>'+
                            '<option value="boolean">boolean</option>'+
                            '<option value="bit-string">bit-string</option>'+
                            '<option value="double-long">double-long</option>'+
                            '<option value="double-long-unsigned">double-long-unsigned</option>'+
                            '<option value="octet-string">octet-string</option>'+
                            '<option value="visible-string">visible-string</option>'+
                            '<option value="utf8-string">utf8-string</option>'+
                            '<option value="bcd">bcd</option>'+
                            '<option value="integer">integer</option>'+
                            '<option value="long">long</option>'+
                            '<option value="unsigned">unsigned</option>'+
                            '<option value="long-unsigned">long-unsigned</option>'+
                            '<option value="long64">long64</option>'+
                            '<option value="long64-unsigned">long64-unsigned</option>'+
                            '<option value="enum">enum</option>'+
                            '<option value="float32">float32</option>'+
                            '<option value="float64">float64</option>'+
                            '<option value="date-time">date-time</option>'+
                            '<option value="date">date</option>'+
                            '<option value="time">time</option>'+

                        '</optgroup>'+
                        '<optgroup label="Complex Type">'+
                            '<option value="array">array</option>'+
                            '<option value="structure">structure</option>'+
                            '<option value="compact array">compact array</option>'+
                            '<option value="CHOICE">CHOICE</option>'+
                        '</optgroup>'+
                     '</select>'+
                    '</td>'+
                 ' <td >'+
                    ''+
                  '</td>'+
                  '<td><input class="btn btn-danger"type="button" value="Remove" onclick="remove(this)"></td>'+


                '</tr>');
                $("#table_class").append(element);


        }
 return false
    }
// function GetSelectedTextValueArray(attributeTypeArray)
// {
//        var selectedText = attributeTypeArray.options[attributeTypeArray.selectedIndex].innerHTML;
//        var selectedValue = attributeTypeArray.value;
//        if (selectedValue=="structure")
//        {
//        document.getElementById("cellSize").disabled = true;
////        addTable();
//
//
////        element = $('<tr><td width="300px"></td><td width="300px" > ' +
////          '</td><td width="300px"> ' +
////                       ' '+
////                    '</td>' +
////
////                    '<td width="300px">'+
////                        ''+
////                    '</td>'+
////                    '<td><center>'+
////                    'StructureSize'+'<br>'+
////                    '<input class="form-control" type="text" value="" size="5" id="structuresize" onchange="GetStructureSize(this.value)"></center>'+
//////                    '</td>'+'</tr>'+'<tr>'+'<td></td><td></td><td></td><td></td>'+
//////                    '<td width="300px">'+
//////                     '<center>ElementType</center>'+
//////                     '<input class="form-control" type="text" name="elementType">'+'</td>'+
//////                     '<td width="300px">'+
//////                     '<center>ElementName</center>'+
//////                     '<input class="form-control" type="text" name="elementname">'+
//////                    '</td>'+
//////                    '</td>'+
////                 ' <td width="300px">'+
////                    ''+
////                  '</td>'+
////
////
////                '</tr>');
////                $("#table_class").append(element);
//
////********************for adding structures****************************************
//
//
//
//// element = $('<tr>'+
////                    '<td></td><td></td><td></td><td></td>'+
////                    '<td width="300px">'+
////                     '<center></center>'+
////                     '</td>'+
////                     '<td width="300px">'+
////                     '<center></center>'+
////
////                    '</td>'+
////                    '</td>'+
////                 ' <td width="300px">'+
////
////                  '</td>'+
////
////
////                '</tr>');
////                $("#table_class").append(element);
//
//
//
//
//
//
//
//
//        }
//  return false
//
//
// }

function GetStructureSize(value,val)
{

val1=val;

    nbElement=value;
  ch = ch.concat(nbElement.toString());
  ch=ch.concat("-");

//   listCh[countCh]=ch;
   listCh.push(ch);



    if (nbElement==0)
    {
      element = $('<tr style="border-bottom: 1px solid LightSteelBlue;">'+
                            '<td></td><td></td>'+
                            '<td >'+
                                '<center>ElementName:<br><input class="form-control" type="text" id="elementname" size="10" placeholder="empty" disabled="true"></center>'+
                                 '<center>ElementType:<br>'+


                        '<select  class="form-control" name="elementtype-' + (idselect) +  "-" +nb_btn_clicked+  "-" +(nbElement)+'"  id="attributeType-' + (idselect) +  "-" +nb_btn_clicked+  "-" +(nbElement)+'"  disabled="true">'+
                        '<option value="Select type" selected="selected">Select type</option>'+
                        '<optgroup label="Simple Type">'+
                            '<option value="null-data">null-data</option>'+
                            '<option value="boolean">boolean</option>'+
                            '<option value="bit-string">bit-string</option>'+
                            '<option value="double-long">double-long</option>'+
                            '<option value="double-long-unsigned">double-long-unsigned</option>'+
                            '<option value="octet-string">octet-string</option>'+
                            '<option value="visible-string">visible-string</option>'+
                            '<option value="utf8-string">utf8-string</option>'+
                            '<option value="bcd">bcd</option>'+
                            '<option value="integer">integer</option>'+
                            '<option value="long">long</option>'+
                            '<option value="unsigned">unsigned</option>'+
                            '<option value="long-unsigned">long-unsigned</option>'+
                            '<option value="long64">long64</option>'+
                            '<option value="long64-unsigned">long64-unsigned</option>'+
                            '<option value="enum">enum</option>'+
                            '<option value="float32">float32</option>'+
                            '<option value="float64">float64</option>'+
                            '<option value="date-time">date-time</option>'+
                            '<option value="date">date</option>'+
                            '<option value="time">time</option>'+

                        '</optgroup>'+
                        '<optgroup label="Complex Type">'+
                            '<option value="array">array</option>'+
                            '<option value="structure">structure</option>'+
                            '<option value="compact array">compact array</option>'+
                            '<option value="CHOICE">CHOICE</option>'+
                        '</optgroup>'+
                     '</select>'+
                    '<center>ElementSize:<br><input class="form-control" type="text"       name="elementsize-' + (idselect) +  "-" +nb_btn_clicked+  "-" +(nbElement)+'"  id="elementsize-' + (idselect) +  "-" +nb_btn_clicked+  "-" +(nbElement)+'" size="10" onchange="GetArraySize(this.value,this)" disabled="true"></center>'+
                                 '</center><br>'+
                             '</td>'+
                             '<td >'+
                             '<center></center>'+

                            '</td>'+

                    '<td >'+

                             '<center></center>'+
                             '<input class="btn btn-danger"type="button" value="Remove" onclick="remove(this)">'+

                            '</td>'+



                        '</tr>');

       $(val).closest('tr').after(element);
}







    for (var i=0; i<nbElement; i++)
    {

            element = $('<tr style="border-bottom: 1px solid LightSteelBlue;">'+
                            '<td></td><td></td>'+
                            '<td >'+
                                '<center>ElementName:<br><input class="form-control" type="text" id="elementname" size="10"></center>'+
                                 '<center>ElementType:<br>'+

                '<input id="hidden" type="hidden" name="nbelement" value="'+ch+'" >'+

                        '<select  class="form-control" name="elementtype-' + (idselect) +  "-" +nb_btn_clicked+  "-"+(i)+  "-" +nb+'"  id="attributeType-' + (idselect) +  "-" +nb_btn_clicked+  "-"+(i)+  "-" +nb+'" >'+
                        '<option value="Select type" selected="selected">Select type</option>'+
                        '<optgroup label="Simple Type">'+
                            '<option value="null-data">null-data</option>'+
                            '<option value="boolean">boolean</option>'+
                            '<option value="bit-string">bit-string</option>'+
                            '<option value="double-long">double-long</option>'+
                            '<option value="double-long-unsigned">double-long-unsigned</option>'+
                            '<option value="octet-string">octet-string</option>'+
                            '<option value="visible-string">visible-string</option>'+
                            '<option value="utf8-string">utf8-string</option>'+
                            '<option value="bcd">bcd</option>'+
                            '<option value="integer">integer</option>'+
                            '<option value="long">long</option>'+
                            '<option value="unsigned">unsigned</option>'+
                            '<option value="long-unsigned">long-unsigned</option>'+
                            '<option value="long64">long64</option>'+
                            '<option value="long64-unsigned">long64-unsigned</option>'+
                            '<option value="enum">enum</option>'+
                            '<option value="float32">float32</option>'+
                            '<option value="float64">float64</option>'+
                            '<option value="date-time">date-time</option>'+
                            '<option value="date">date</option>'+
                            '<option value="time">time</option>'+

                        '</optgroup>'+
                        '<optgroup label="Complex Type">'+
                            '<option value="array">array</option>'+
                            '<option value="structure">structure</option>'+
                            '<option value="compact array">compact array</option>'+
                            '<option value="CHOICE">CHOICE</option>'+
                        '</optgroup>'+
                     '</select>'+

                        '<center>ElementSize:<br><input class="form-control" type="text" id="elementsize-' + (idselect) +  "-" +nb_btn_clicked+  "-" +(i)+ "-" +nb+ '" size="10"  onchange="GetArraySize(this.value,this)"></center>'+

                                 '</center><br>'+
                             '</td>'+
                             '<td >'+
                             '<center></center>'+

                            '</td>'+

                    '<td >'+
                             '<center></center>'+
                             '<input class="btn btn-danger"type="button" value="Remove" onclick="remove(this)">'+
                             '<input type="hidden" name="nb" value='+nb+'>'+

                            '</td>'+



                        '</tr>');

       $(val).closest('tr').after(element);



}



 element2 = $('<input id="hidden" type="hidden" name="nbelement" value="'+listCh+'" >');
  $(val1).closest('tr').after(element2);

// document.getElementById("hidden").value = ch;



    return false;
    }


 function GetArraySize(value,val)
  {
//  indice=0;
nbappel=0;
 nbremove=0;
tab[nbappel-1]=nbappel;
nbappel++;
nb_btn_clicked=0;
       idsi=$(this).attr('id');
//       textsize=$(this);

     sel=document.getElementById("attributeType-"+idsize).value;


     attrSize=value;



   myArray[nbappel-1]=attrSize;


//     *****************************************************
if(nbremove==myArray[nbappel-2])


             {
                nb_btn_clicked=0;

             }

//     ****************************************************


     if (attrSize==0)
     {
//     $("#BtnAddCell").prop("disabled",true);
     }
      if (attrSize!="" & sel=="array")
      {

      }

     if (sel=="Select type"  )
     {

//      $("#BtnAddCell").prop("disabled",true);
     }
 if (attrSize =="Select type" )
     {

//      $("#BtnAddCell").prop("disabled",true);
     }

     if (sel != "Select type" )
     {
       $("#BtnAddCell").prop("disabled",false);


}


  if (attrSize != "Select type" )
     {
       $("#BtnAddCell").prop("disabled",false);


}


     return false;
   }
//  function addTable()
//  {
//
//
//                     element = $('<tr>'+
//                    '<td></td><td></td>'+
//                    '<td width="300px">'+
////                    '<input class="btn btn-primary" type="button" id="size" value="addStructure" onclick="addStructureSize()"> '+
//                     '</td>'+
//                     '<td width="300px">'+
//
//
//                    '</td>'+
//                    '<td><input class="btn btn-danger"type="button" value="Remove" ></td>'+
//
//
//
//                '</tr>');
//                $("#table_class").append(element);
//
//
//
//
//
//                return false;
//                }
// ***********************************************               number of elements***********************************************

//function getElementsNumber(value,nb)
//
//{
//
//    nbElement=value;
//    for (var i=0; i<nbElement; i++)
//    {
//    element = $('<tr>'+
//                    '<td></td><td></td>'+
//                    '<td width="300px">'+
//                        '<center>ElementName:<br><input class="form-control" type="text" id="elementname" size="10"></center>'+
//                         '<center>ElementType:<br><input class="form-control" type="text" id="elementtype" size="10"></center><br>'+
//                     '</td>'+
//                     '<td width="300px">'+
//                     '<center><input class="btn btn-primary" type="button" value="addStructure" onclick="addStructureSize()"></center>'+
//
//                    '</td>'+
//
//            '<td width="300px">'+
//                     '<center></center>'+
//                     '<input class="btn btn-danger"type="button" value="Remove" >'+
//
//                    '</td>'+
//
//
//
//                '</tr>');
////$("#table_class").append(element);
////  $('#table_class > tbody > tr').after(element);
//$(element).insertAfter( $("#"+nb ) );
//
//
//
//
//    }
//
//
//
//}

function addStructureSize()
{

nbclicstructure++;

//indice++;
  element = $('<tr style="border-bottom: 1px solid LightSteelBlue;"  id="'+(nb)+'">'+
                    '<td></td><td></td>'+
                    '<td >'+
                    '<center></center>'+
                        '<center>StructureSize:<br><input class="form-control" type="text" id="structuresize-' + (idselect) +  "-" +nb_btn_clicked+  "-" +(nbe++)+'" name="structuresize-' + (idselect) +  "-" +nb_btn_clicked+  "-" +(nbe++)+'" size="5" onchange="GetStructureSize(this.value,this)">'+
                        '<td >'+


                         '</center>'+

                     '</td>'+

                 '<td> <input class="btn btn-danger"type="button" value="Remove" onclick="remove(this)"></td>'+



//                  '<td></td>'+


                '</tr>');
//                 $('#table_class').append(element);
//                 $('#table_class > tbody > tr').eq($('tr').index($(this))).after(element);
//                   $(this).after(element);
//                    $(element).insertAfter("#1");
//                        $(this).closest('tr').after(element);
//                        $("<tr>").attr({"id":"id_"+nb}).appendTo("#table_class");
//                         $('#table_class #'+nb+).after(element);
//                         $(element).insertAfter( $("#" +nb ) );
$(element).insertAfter( $("#"+nb ) );
//                         $(this).closest('tr').after(element);






}

//******************************************delete line********************************************

//$('#table_class').on('click', 'input[type="button"]', function () {
//    $(this).closest('tr').remove();
//  })
//$('#table_methode').on('click', 'input[type="button"]', function () {
//    $(this).closest('tr').remove();
//})


//*************************************************************************************************************************


//function test(){
////    var doc = document.implementation.createDocument ('http://www.w3.org/1999/xhtml', 'html', null);
////    var body = document.createElementNS('http://www.w3.org/1999/xhtml', 'body');
////    body.setAttribute('id', 'abc');
////    doc.documentElement.appendChild(body);
////        var xmlDoc = document.implementation.createDocument(null, 'root', null);
////
////        var foo = xmlDoc.createElement('foo');
////        foo.textContent = 'bar';
////
////        xmlDoc.documentElement.appendChild(foo);
////
////        console.log(xmlDoc);
//
////var fso = new ActiveXObject("Scripting.FileSystemObject");
////// 2=overwrite, true=create if not exist, 0 = ASCII
////varFileObject = fso.OpenTextFile("Bibliothèques\Documents", 2, true,0);
////varFileObject.write("File handling in Javascript");
////varFileObject.close();
//
////var XML = new XMLWriter();
////XML.BeginNode("Foo");
////XML.Attrib("Bar", "Some Value");
////XML.EndNode();
////XML.Node("MyNode", "My Value");
////var doc = document.implementation.createDocument(null, "report", null);
//
////  if (document.implementation.createDocument &&
////                document.implementation.createDocumentType)
////            {
////                var fruitDocType = document.implementation.createDocumentType ("fruit", "SYSTEM", "<!ENTITY tf 'tropical fruit'>");
////                var xmlDoc = document.implementation.createDocument ("", "fruits", fruitDocType);
////
////                var fruitNode = xmlDoc.createElement ("fruit");
////                fruitNode.setAttribute ("name" , "avocado");
////                xmlDoc.documentElement.appendChild (fruitNode);
////
////
////
////                var serializer = new XMLSerializer();
////
////
////})
////            }
////            else {
////            }
//
//function generateXML(){
//    // Simple helper function creates a new element from a name, so you don't have to add the brackets etc.
//    $.createElement = function(name)
//    {
//        return $('<'+name+' />');
//    };
//
//    // JQ plugin appends a new element created from 'name' to each matched element.
//    $.fn.appendNewElement = function(name)
//    {
//        this.each(function(i)
//        {
//            $(this).append('<'+name+' />');
//        });
//        return this;
//    }
//
//    /* xml root element - because html() does not include the root element and we want to
//        * include <report /> in the output. There may be a better way to do this.
//        */
//    var $root = $('<XMLDocument />');
//
//    $root.append
//    (
//    // one method of adding a basic structure
//    $('<plist />').append(
//    $('<dict />').append(
//    $('<key />').text('subject'),
//    $('<string />').text('September 21'),
//    $('<key />').text('date'),
//    $('<string />').text('FOB10 Room'),
//    $('<key />').text('time'),
//    $('<string />').text('2.00 pm - 5.00 pm'),
//    $('<key />').text('briefings'),
//
//    $('<array />').append
//    (
//    $('<dict />').append
//    (
//    $('<key />').text('files'),
//    $('<array />').append
//    (
//    $('<dict />').append
//    (
//    $('<key />').text('date'),
//    $('<string />').text('09/09/2012'),
//    $('<key />').text('name'),
//    $('<string />').text('acatBriefing.pdf'),
//    $('<key />').text('description'),
//    $('<string />').text('ACAT Briefing')
//)
//),
//    $('<key />').text('subject'),
//    $('<string />').text('FAE approved ACAT Designations'),
//    $('<key />').text('presenter'),
//    $('<string />').text('Rebecca T. King'),
//    $('<key />').text('time'),
//    $('<string />').text('2.00 - 2.05 PM')
//
//)
//)
//)
//)
//);
//
//
//}
//generateXML();
//
//
//}
nbselect=0;
$('#form1').on('change', ' select', function(){
//    $(this).closest('tr').find('input[name="dbFlag"]').val('U');
nbselect++;
nbclicstructure=0;
 var selected = $(this).find("option:selected").val();
    cpt=$(this).prop('id');
    idt=$(this).attr('id');
//    ids=idsi.attr('id');


  att=document.getElementById("attributesize-"+idselect).value;

 if (($(this).find("option:selected").val()=="unsigned" ))

{
cpt=$(this).prop('id');

var afterComma = cpt.substr(cpt.indexOf("-") + 1)

$("#attributesize-"+afterComma).prop("disabled",true);
if(nb_btn_clicked>=1)
{

$("#cellSize-"+(afterComma)).prop("disabled",true);

}

if(nbElement>0)

{
$("#elementsize-"+(afterComma)).prop("disabled",true);
}

}


if (($(this).find("option:selected").val()=="null-data" ))

{
cpt=$(this).prop('id');
var afterComma = cpt.substr(cpt.indexOf("-") + 1)

$("#attributesize-"+afterComma).prop("disabled",true);
if(nb_btn_clicked>=1)
{

$("#cellSize-"+(afterComma)).prop("disabled",true);

}
if(nbElement>0)

{
$("#elementsize-"+(afterComma)).prop("disabled",true);
}

}

if (($(this).find("option:selected").val()=="boolean" ))

{
cpt=$(this).prop('id');

var afterComma = cpt.substr(cpt.indexOf("-") + 1)

$("#attributesize-"+afterComma).prop("disabled",true);
if(nb_btn_clicked>=1)
{

$("#cellSize-"+(afterComma)).prop("disabled",true);

}
if(nbElement>0)

{
$("#elementsize-"+(afterComma)).prop("disabled",true);
}
}


if (($(this).find("option:selected").val()=="double-long-unsigned" ))

{
cpt=$(this).prop('id');

var afterComma = cpt.substr(cpt.indexOf("-") + 1)

$("#attributesize-"+afterComma).prop("disabled",true);

if(nb_btn_clicked>=1)
{

$("#cellSize-"+(afterComma)).prop("disabled",true);

}


if(nbElement>0)

{
$("#elementsize-"+(afterComma)).prop("disabled",true);
}
}



if (($(this).find("option:selected").val()=="bcd" ))

{
cpt=$(this).prop('id');

var afterComma = cpt.substr(cpt.indexOf("-") + 1)

$("#attributesize-"+afterComma).prop("disabled",true);
if(nb_btn_clicked>=1)
{

$("#cellSize-"+(afterComma)).prop("disabled",true);

}

if(nbElement>0)

{
$("#elementsize-"+(afterComma)).prop("disabled",true);
}

}


if (($(this).find("option:selected").val()=="integer" ))

{
cpt=$(this).prop('id');

var afterComma = cpt.substr(cpt.indexOf("-") + 1)

$("#attributesize-"+afterComma).prop("disabled",true);
if(nb_btn_clicked>=1)
{

$("#cellSize-"+(afterComma)).prop("disabled",true);

}

if(nbElement>0)

{
$("#elementsize-"+(afterComma)).prop("disabled",true);
}

}

if (($(this).find("option:selected").val()=="long" ))

{
cpt=$(this).prop('id');

var afterComma = cpt.substr(cpt.indexOf("-") + 1)

$("#attributesize-"+afterComma).prop("disabled",true);
if(nb_btn_clicked>=1)
{

$("#cellSize-"+(afterComma)).prop("disabled",true);

}

if(nbElement>0)

{
$("#elementsize-"+(afterComma)).prop("disabled",true);
}

}



if (($(this).find("option:selected").val()=="long-unsigned" ))

{
cpt=$(this).prop('id');

var afterComma = cpt.substr(cpt.indexOf("-") + 1)

$("#attributesize-"+afterComma).prop("disabled",true);
if(nb_btn_clicked>=1)
{

$("#cellSize-"+(afterComma)).prop("disabled",true);

}
if(nbElement>0)

{
$("#elementsize-"+(afterComma)).prop("disabled",true);
}

}


if (($(this).find("option:selected").val()=="long64" ))

{
cpt=$(this).prop('id');

var afterComma = cpt.substr(cpt.indexOf("-") + 1)

$("#attributesize-"+afterComma).prop("disabled",true);
if(nb_btn_clicked>=1)
{

$("#cellSize-"+(afterComma)).prop("disabled",true);

}
if(nbElement>0)

{
$("#elementsize-"+(afterComma)).prop("disabled",true);
}

}


if (($(this).find("option:selected").val()=="long64-unsigned" ))

{
cpt=$(this).prop('id');

var afterComma = cpt.substr(cpt.indexOf("-") + 1)

$("#attributesize-"+afterComma).prop("disabled",true);
if(nb_btn_clicked>=1)
{

$("#cellSize-"+(afterComma)).prop("disabled",true);

}
if(nbElement>0)

{
$("#elementsize-"+(afterComma)).prop("disabled",true);
}

}


if (($(this).find("option:selected").val()=="enum" ))



{
cpt=$(this).prop('id');

var afterComma = cpt.substr(cpt.indexOf("-") + 1)

$("#attributesize-"+afterComma).prop("disabled",true);
if(nb_btn_clicked>=1)
{

$("#cellSize-"+(afterComma)).prop("disabled",true);

}
if(nbElement>0)

{
$("#elementsize-"+(afterComma)).prop("disabled",true);
}

}
if (($(this).find("option:selected").val()=="float32" ))

{
cpt=$(this).prop('id');

var afterComma = cpt.substr(cpt.indexOf("-") + 1)

$("#attributesize-"+afterComma).prop("disabled",true);
if(nb_btn_clicked>=1)
{

$("#cellSize-"+(afterComma)).prop("disabled",true);

}
if(nbElement>0)

{
$("#elementsize-"+(afterComma)).prop("disabled",true);
}

}

if (($(this).find("option:selected").val()=="float64" ))

{
cpt=$(this).prop('id');

var afterComma = cpt.substr(cpt.indexOf("-") + 1)

$("#attributesize-"+afterComma).prop("disabled",true);

if(nb_btn_clicked>=1)
{

$("#cellSize-"+(afterComma)).prop("disabled",true);

}
if(nbElement>0)

{
$("#elementsize-"+(afterComma)).prop("disabled",true);
}
}


if (($(this).find("option:selected").val()=="date-time" ))

{
cpt=$(this).prop('id');

var afterComma = cpt.substr(cpt.indexOf("-") + 1)

$("#attributesize-"+afterComma).prop("disabled",true);
if(nb_btn_clicked>=1)
{

$("#cellSize-"+(afterComma)).prop("disabled",true);

}
if(nbElement>0)

{
$("#elementsize-"+(afterComma)).prop("disabled",true);
}

}

if (($(this).find("option:selected").val()=="date" ))

{
cpt=$(this).prop('id');

var afterComma = cpt.substr(cpt.indexOf("-") + 1)

$("#attributesize-"+afterComma).prop("disabled",true);
if(nb_btn_clicked>=1)
{

$("#cellSize-"+(afterComma)).prop("disabled",true);

}

if(nbElement>0)

{
$("#elementsize-"+(afterComma)).prop("disabled",true);
}

}


if (($(this).find("option:selected").val()=="time" ))

{
cpt=$(this).prop('id');

var afterComma = cpt.substr(cpt.indexOf("-") + 1)

$("#attributesize-"+afterComma).prop("disabled",true);

if(nb_btn_clicked>=1)
{

$("#cellSize-"+(afterComma)).prop("disabled",true);

}
if(nbElement>0)

{
$("#elementsize-"+(afterComma)).prop("disabled",true);
}
}




if (($(this).find("option:selected").val()=="double-long" ))

{
cpt=$(this).prop('id');

var afterComma = cpt.substr(cpt.indexOf("-") + 1)

$("#attributesize-"+afterComma).prop("disabled",true);

if(nb_btn_clicked>=1)
{

$("#cellSize-"+(afterComma)).prop("disabled",true);

}
if(nbElement>0)

{
$("#elementsize-"+(afterComma)).prop("disabled",true);
}
}



  if (selected=="array" |selected=="CHOICE" | selected=="compact array")
  {

//indice++;
//

//   if (attrSize!="" & selected=="array")
//      {
//      $("#BtnAddCell").prop("disabled",false);
//      }


        nb_btn_clicked=0;
//        attrSize=0;








   element = $('<tr    style="border-bottom: 1px solid LightSteelBlue;"><td ></td><td width="300px" >' +
          '</td>'+
                    '<td><center><input  type="button" class="btn-default" value="+" onclick="addCell(this)" id="BtnAddCell"></center>'+
//                     '<select  class="form-control" name="AttributeTypeArray" id="attributeTypeArray" onchange="GetSelectedTextValueArray(this)">'+
//                        '<option value="Select type" selected="selected">Select type</option>'+
//                        '<optgroup label="Simple Type">'+
//                            '<option value="null-data">null-data</option>'+
//                            '<option value="boolean">boolean</option>'+
//                            '<option value="bit-string">bit-string</option>'+
//                            '<option value="null-data">double-long</option>'+
//                            '<option value="double-long-unsigned">double-long-unsigned</option>'+
//                            '<option value="octet-string">octet-string</option>'+
//                            '<option value="visible-string">visible-string</option>'+
//                            '<option value="utf8-string">utf8-string</option>'+
//                            '<option value="bcd">bcd</option>'+
//                            '<option value="integer">integer</option>'+
//                            '<option value="long">long</option>'+
//                            '<option value="unsigned">unsigned</option>'+
//                            '<option value="long-unsigned">long-unsigned</option>'+
//                            '<option value="long64">long64</option>'+
//                            '<option value="long64-unsigned">long64-unsigned</option>'+
//                            '<option value="enum">enum</option>'+
//                            '<option value="float32">float32</option>'+
//                            '<option value="float64">float64</option>'+
//                            '<option value="date-time">date-time</option>'+
//                            '<option value="date">date</option>'+
//                            '<option value="time">time</option>'+
//
//                        '</optgroup>'+
//                        '<optgroup label="Complex Type">'+
//                            '<option value="array">array</option>'+
//                            '<option value="structure">structure</option>'+
//                            '<option value="compact array">compact array</option>'+
//                            '<option value="CHOICE">CHOICE</option>'+
//                        '</optgroup>'+
//                     '</select>'+
                    '</td>'+
                 ' <td width="300px">'+
   '<input type="hidden" value="'+indice+'">'+
                  '</td>'+
                  '<td><input class="btn btn-danger"type="button" value="Remove" onclick="remove(this)" ></td></tr>');

//            $("#table_class").append(element);
             $(this).closest('tr').after(element);

//              $("#BtnAddCell").prop("disabled",true);
//**********************************************************
  if (att== '' & selected=="array")
      {
//      $("#BtnAddCell").prop("disabled",true);

      }
      if (att== '')
//        $("#BtnAddCell").prop("disabled",true);
      {

      }
if (att != '')
{
  $("#BtnAddCell").prop("disabled",false);
 }
//$("#BtnAddCell").prop("disabled",true);

//*************************************






}

if (selected=="structure")

{
//$("#attributesize-"+idselect).prop("disabled",true);
//$("#cellSize-"+(afterComma)).prop("disabled",true);
nbe=0

var afterComma = cpt.substr(cpt.indexOf("-") + 1)
$("#cellSize-"+afterComma).prop("disabled",true);
$("#elementsize-"+(afterComma)).prop("disabled",true);
$("#attributesize-"+afterComma).prop("disabled",true);


nb++;
//document.getElementById("cellSize").disabled = true;


                     element = $('<tr   style="border-bottom: 1px solid LightSteelBlue;" id="'+nb+'">'+
                    '<td></td><td></td>'+
                    '<td >'+
                    '<center><input class="btn btn-primary" type="button" value="addStructure" name="size" onclick="addStructureSize()"></center> '+
                     '</td>'+
                     '<td >'+
'<input type="hidden" value="'+indice+'">'+

                    '</td>'+
                    '<td><input class="btn btn-danger"type="button" value="Remove" onclick="remove(this)" ></td>'+



                '</tr>');
               $(this).closest('tr').after(element);

//index++;



}

});


//$('#table_class').on('click', 'input[type="button"]', function () {
//
//
//    var nbElement=""
//
//      element = $('<tr id="1">'+
//                        '<td></td><td></td>'+
//                        '<td width="300px">'+
//                         '<input class="btn btn-primary" type="button" value="addStructure" id="size" >'+
//                            '<center>StructureSize:<br><input class="form-control" type="text" id="structuresize" onchange="getElementsNumber(this.value)" size="5"> <td width="300px">'+
//
//
//                             '</center>'+
//
//                         '</td>'+
//
//                     '<td><input class="btn btn-danger"type="button" value="Remove" ></td>'+
//
//
//
//    //                  '<td></td>'+
//
//
//                    '</tr>');
//
//
////                   $(#table_class).closest('tr').append(element);
////                   $("#table_class").closest('tr').after(element)
////                     $('#table_class tr').after(element);
//
////                        $(element).insertAfter('#table_class select');
//
//
//                       $('#table_class > tbody > tr').eq($(" input[type='button']").index()+1).append(element);
//
//
//
//
//
//
//
//
//
//})

// $('#structuresize').on('input',function(e){
//    });
//******************************gget the text changed

//$("input[name='structuresize']").on("change",function(){
//
//});
//$('#form1').on('change', ' input[type=text]', function(){
//
// nbElement=$(this).val();
//    for (var i=0; i<nbElement; i++)
//    {
//            element = $('<tr>'+
//                            '<td></td><td></td>'+
//                            '<td width="300px">'+
//                                '<center>ElementName:<br><input class="form-control" type="text" id="elementname" size="10"></center>'+
//                                 '<center>ElementType:<br><input class="form-control" type="text" id="elementtype" size="10"></center><br>'+
//                             '</td>'+
//                             '<td width="300px">'+
//                             '<center></center>'+
//
//                            '</td>'+
//
//                    '<td width="300px">'+
//                             '<center></center>'+
//                             '<input class="btn btn-danger"type="button" value="Remove" >'+
//
//                            '</td>'+
//
//
//
//                        '</tr>');
//
//       $(this).closest('tr').after(element);
//}
//
//})


        function addCell(value)

        {
        indice++;


//s=document.getElementById("cellSize").value;

        att=document.getElementById("attributesize-"+idselect).value;
//      for (var i = 0;i<nbappel; i++) {
//      t(i)=nbappel;
//      }



//            if (nbremove >0 )
//            {
//
//            nb_btn_clicked=attrSize-nbremove;
//            nbremove=0;
//             }
//
//            else
            if(nbremove ==attrSize)
             {
             nb_btn_clicked=0;
             nbremove=0;
             }

             if(nbremove==myArray[nbappel-2])


             {
                nb_btn_clicked=0;
                nbremove=0;

             }
//            if (nbremove>0 & nbremove<attrSize)
//
//            {
//            nb_btn_clicked=attrSize-nbremove;
//
//            }
if(nbappel>1 & (attrSize!=myArray[nbappel-2]))
{
nbappel=0;
nb_btn_clicked=0;



}



            nb_btn_clicked++;
                     if (att=="" )
                     {
//                      $("#BtnAddCell").prop("disabled",true);
                     }
              if (attrSize==0)
                     {
//                     $("#BtnAddCell").prop("disabled",true);
                     }


           if (nb_btn_clicked <= attrSize ){


             element = $('<tr style="border-bottom: 1px solid LightSteelBlue;"><td width="300px"></td><td width="300px" >' +
          '</td>'+
                    '<td width="300px">'+
                     '<select  class="form-control" name="attributeTypeArray-' + (idselect) +  "-" +nb_btn_clicked+ "-"+indice+ "-" +nbclicstructure+ '" id="attributeType-' + (idselect) +  "-" +nb_btn_clicked+ "-"+indice+ "-" +nbclicstructure+ '" >'+
                        '<option value="Select type" selected="selected">Select type</option>'+
                        '<optgroup label="Simple Type">'+
                            '<option value="null-data">null-data</option>'+
                            '<option value="boolean">boolean</option>'+
                            '<option value="bit-string">bit-string</option>'+
                            '<option value="double-long">double-long</option>'+
                            '<option value="double-long-unsigned">double-long-unsigned</option>'+
                            '<option value="octet-string">octet-string</option>'+
                            '<option value="visible-string">visible-string</option>'+
                            '<option value="utf8-string">utf8-string</option>'+
                            '<option value="bcd">bcd</option>'+
                            '<option value="integer">integer</option>'+
                            '<option value="long">long</option>'+
                            '<option value="unsigned">unsigned</option>'+
                            '<option value="long-unsigned">long-unsigned</option>'+
                            '<option value="long64">long64</option>'+
                            '<option value="long64-unsigned">long64-unsigned</option>'+
                            '<option value="enum">enum</option>'+
                            '<option value="float32">float32</option>'+
                            '<option value="float64">float64</option>'+
                            '<option value="date-time">date-time</option>'+
                            '<option value="date">date</option>'+
                            '<option value="time">time</option>'+

                        '</optgroup>'+
                        '<optgroup label="Complex Type">'+
                            '<option value="array">array</option>'+
                            '<option value="structure">structure</option>'+
                            '<option value="compact array">compact array</option>'+
                            '<option value="CHOICE">CHOICE</option>'+
                        '</optgroup>'+
                     '</select>'+
                    '</td>'+
                 ' <td width="300px">'+
'<center><input type="text" class="form-control" placeholder="size"  id="cellSize-' + (idselect) + "-" +nb_btn_clicked+ "-" +indice+ "-" +nbclicstructure+'" onblur="get(this.value)"></center>'+
                  '<input type="hidden" name="nbclic+" value='+nb_btn_clicked+'>'+
                    '<input type="hidden" name="indice" value='+indice+'>'+
                     '<input type="hidden" name="nbclicstructure" value='+nbclicstructure+'>'+

                  '</td>'+
                  '<td><input class="btn btn-danger"type="button" value="Remove" onclick="remove(this)" ></td></tr>');
//
//             indice++;


             $(value).closest('tr').after(element);



             }




  else {

                 depasse++;

//                 $("#BtnAddCell").prop("disabled",true);
                 }


                     if (attrSize==nb_btn_clicked )
                 {

//                  $("#BtnAddCell").prop("disabled",true);
                 }
//                 if (document.getElementById("cellSize").value=="")
//                 {
//                 $("#BtnAddCell").prop("disabled",true);
//
//                 }

                 if (document.getElementById("cellSize-"+idselect).value==nb_btn_clicked)
                 {
//                 $("#BtnAddCell").prop("disabled",true);




                 }


        }
function get(value)
{


if(nbremove==attrSize)
{
nb_btn_clicked=0;
}

nbremove=0;
nb_btn_clicked=0;

//$("#BtnAddCell").prop("disabled",true);
attrSize=value;

}

//        ********************************************remove button **********************************************
       var nbremove=0;



        function remove(btn)
        {
        $(btn).closest('tr').remove();
        $("#BtnAddCell").prop("disabled",false);
                nbremove++;





//                if (nbremove==attrSize)
//                {
//                nb_btn_clicked=0;
//
//                }
//           else{
//
//            nb_btn_clicked=nb_btn_clicked-(depasse+nbremove)+1;}
//
//
//
//            nb_btn_clickedMethod--;
//
//
//
        }

//        **********************************remove method

 var nbremove2=0;



        function remove2(btn)
        {

        nb_btn_clickedMethod--;
        $(btn).closest('tr').remove();
        $("#BtnAddCell2").prop("disabled",false);
                nbremove2++;




//                if (nbremove==attrSize)
//                {
//                nb_btn_clicked=0;
//
//                }
//           else{
//
//            nb_btn_clicked=nb_btn_clicked-(depasse+nbremove)+1;}
//
//
//
//            nb_btn_clickedMethod--;
//
//
//
        }


//*******************************************************

//***********************************************method methodes

        function MethodGetArraySize(value,val)
          {
  indice2=0;
nbappel2=0;
 nbremove2=0;
tab2[nbappel2-1]=nbappel2;
nbappel2++;
methodSize=value;
//nb_btn_clickedMethod=0;
//       idsi=$(this).attr('id');

//       textsize=$(this);

     sel=document.getElementById("methodType-"+idselect2).value;





   myArray2[nbappel2-1]=methodSize;


//     *****************************************************
if(nbremove2==myArray2[nbappel2-2])


             {
                nb_btn_clickedMethod=0;

             }
     if( nbremove2!=0)
     {
     nb_btn_clickedMethod=nb_btn_clickedMethod;
     }
if(nbremove2!=0 &myArray2[nbappel2-1]!=methodSize)
{
nb_btn_clickedMethod=0;
}


//     ****************************************************


     if (methodSize==0)
     {
//     $("#BtnAddCell2").prop("disabled",true);
     }
      if (methodSize!="" & sel=="array")
      {

      }

     if (sel=="Select type"  )
     {

//      $("#BtnAddCell2").prop("disabled",true);
     }
 if (sel =="Select type" )
     {

//      $("#BtnAddCell2").prop("disabled",true);
     }

     if (sel != "Select type" )
     {
       $("#BtnAddCell2").prop("disabled",false);


}


  if (methodSize != "Select type" )
     {
       $("#BtnAddCell2").prop("disabled",false);


}


     return false;
   }



//        **************************************





//        ***************************






//        function GetMethodType(value,val)
//        {
//             if (value=="array" |value=="CHOICE" | value=="compact array")
//  {
//                nb_btn_clickedMethod=0;
//
//              element = $('<tr style="border-bottom: 1px solid LightSteelBlue;"><td width="300px"></td><td width="300px" >' +
//              '</td>'+
//                        '<td width="300px"><center><input  type="button" class="btn-default" value="+" onclick="addCellMethod(this)"></center>'+
//    //                     '<select  class="form-control" name="AttributeTypeArray" id="attributeTypeArray" onchange="GetSelectedTextValueArray(this)">'+
//    //                        '<option value="Select type" selected="selected">Select type</option>'+
//    //                        '<optgroup label="Simple Type">'+
//    //                            '<option value="null-data">null-data</option>'+
//    //                            '<option value="boolean">boolean</option>'+
//    //                            '<option value="bit-string">bit-string</option>'+
//    //                            '<option value="null-data">double-long</option>'+
//    //                            '<option value="double-long-unsigned">double-long-unsigned</option>'+
//    //                            '<option value="octet-string">octet-string</option>'+
//    //                            '<option value="visible-string">visible-string</option>'+
//    //                            '<option value="utf8-string">utf8-string</option>'+
//    //                            '<option value="bcd">bcd</option>'+
//    //                            '<option value="integer">integer</option>'+
//    //                            '<option value="long">long</option>'+
//    //                            '<option value="unsigned">unsigned</option>'+
//    //                            '<option value="long-unsigned">long-unsigned</option>'+
//    //                            '<option value="long64">long64</option>'+
//    //                            '<option value="long64-unsigned">long64-unsigned</option>'+
//    //                            '<option value="enum">enum</option>'+
//    //                            '<option value="float32">float32</option>'+
//    //                            '<option value="float64">float64</option>'+
//    //                            '<option value="date-time">date-time</option>'+
//    //                            '<option value="date">date</option>'+
//    //                            '<option value="time">time</option>'+
//    //
//    //                        '</optgroup>'+
//    //                        '<optgroup label="Complex Type">'+
//    //                            '<option value="array">array</option>'+
//    //                            '<option value="structure">structure</option>'+
//    //                            '<option value="compact array">compact array</option>'+
//    //                            '<option value="CHOICE">CHOICE</option>'+
//    //                        '</optgroup>'+
//    //                     '</select>'+
//                        '</td>'+
//                     ' <td width="300px">'+
//
//                      '</td>'+
//                      '<td><input class="btn btn-danger"type="button" value="Remove" onclick="remove(this)"></td></tr>');
//
////            $("#table_class").append(element);
//                 $(val).closest('tr').after(element);
////
////
//
//}
//
//                if (value=="structure")
//
//                {
//                nb++;
//
//
//
//                                     element = $('<tr style="border-bottom: 1px solid LightSteelBlue;" id="'+nb+'">'+
//                                    '<td></td><td></td>'+
//                                    '<td width="300px">'+
//                                    '<center><input class="btn btn-primary" type="button" value="addStructure" name="size" onclick="addStructureSize()"></center> '+
//                                     '</td>'+
//                                     '<td width="300px">'+
//
//
//                                    '</td>'+
//                                    '<td><input class="btn btn-danger"type="button" value="Remove" onclick="remove(this)" ></td>'+
//
//
//
//                                '</tr>');
//                               $(val).closest('tr').after(element);
//
//                //index++;
//
//
//
//                }
//
//
//
//
//        }

//        function addCellMethod(v)
//        {
//
//            nb_btn_clickedMethod++;
//
//
//
//
//
//           if (nb_btn_clickedMethod <= methodSize ){
//
//             element = $('<tr style="border-bottom: 1px solid LightSteelBlue;"><td width="300px"></td><td width="300px" >' +
//          '</td>'+
//                    '<td width="300px">'+
//                     '<center><input  type="button" class="btn-default" value="+" onclick="addCellMethod(this)"></center><select  class="form-control" onchange="GetMethodType(this.value,this)" >'+
//                        '<option value="Select type" selected="selected">Select type</option>'+
//                        '<optgroup label="Simple Type">'+
//                            '<option value="null-data">null-data</option>'+
//                            '<option value="boolean">boolean</option>'+
//                            '<option value="bit-string">bit-string</option>'+
//                            '<option value="null-data">double-long</option>'+
//                            '<option value="double-long-unsigned">double-long-unsigned</option>'+
//                            '<option value="octet-string">octet-string</option>'+
//                            '<option value="visible-string">visible-string</option>'+
//                            '<option value="utf8-string">utf8-string</option>'+
//                            '<option value="bcd">bcd</option>'+
//                            '<option value="integer">integer</option>'+
//                            '<option value="long">long</option>'+
//                            '<option value="unsigned">unsigned</option>'+
//                            '<option value="long-unsigned">long-unsigned</option>'+
//                            '<option value="long64">long64</option>'+
//                            '<option value="long64-unsigned">long64-unsigned</option>'+
//                            '<option value="enum">enum</option>'+
//                            '<option value="float32">float32</option>'+
//                            '<option value="float64">float64</option>'+
//                            '<option value="date-time">date-time</option>'+
//                            '<option value="date">date</option>'+
//                            '<option value="time">time</option>'+
//
//                        '</optgroup>'+
//                        '<optgroup label="Complex Type">'+
//                            '<option value="array">array</option>'+
//                            '<option value="structure">structure</option>'+
//                            '<option value="compact array">compact array</option>'+
//                            '<option value="CHOICE">CHOICE</option>'+
//                        '</optgroup>'+
//                     '</select><center><input type="text" class="form-control" placeholder="size" id="cellSize"></center>'+
//                    '</td>'+
//                 ' <td width="300px">'+
//
//                  '</td>'+
//                  '<td><input class="btn btn-danger"type="button" value="Remove" onclick="remove(this)" ></td></tr>');
//
//
//             $(v).closest('tr').after(element);
//               }
//  if (nb_btn_clickedMethod > methodSize )
//  {
//  }
// }

//------------------------------------------------------------*Methods*------------------------------------------------------------
nbselect2=0;
 $('#form2').on('change', ' select', function(){
//    $(this).closest('tr').find('input[name="dbFlag"]').val('U');
nbselect2++;
 var selected = $(this).find("option:selected").val();

// *********************modif

 cpt2=$(this).prop('id');
    idt=$(this).attr('id');
//    ids=idsi.attr('id');


  att=document.getElementById("methodsize-"+idselect2).value;

 if (($(this).find("option:selected").val()=="unsigned" ))

{
cpt2=$(this).prop('id');


var afterComma2 = cpt2.substr(cpt2.indexOf("-") + 1)

$("#methodsize-"+afterComma2).prop("disabled",true);
if(nb_btn_clickedMethod>=1)
{

$("#cellSizeMethod-"+(afterComma2)).prop("disabled",true);

}

if(nbElement>0)

{
$("#elementsizemethod-"+(afterComma2)).prop("disabled",true);
}

}


if (($(this).find("option:selected").val()=="null-data" ))

{
cpt2=$(this).prop('id');
var afterComma2 = cpt2.substr(cpt2.indexOf("-") + 1)

$("#methodsize-"+afterComma2).prop("disabled",true);
if(nb_btn_clickedMethod>=1)
{

$("#cellSizeMethod-"+(afterComma2)).prop("disabled",true);

}
if(nbElement2>0)

{
$("#elementsizemethod-"+(afterComma2)).prop("disabled",true);
}

}


if (($(this).find("option:selected").val()=="boolean" ))

{
cpt2=$(this).prop('id');
var afterComma2 = cpt2.substr(cpt2.indexOf("-") + 1)

$("#methodsize-"+afterComma2).prop("disabled",true);
if(nb_btn_clickedMethod>=1)
{

$("#cellSizeMethod-"+(afterComma2)).prop("disabled",true);

}
if(nbElement2>0)

{
$("#elementsizemethod-"+(afterComma2)).prop("disabled",true);
}

}


if (($(this).find("option:selected").val()=="double-long" ))

{
cpt2=$(this).prop('id');
var afterComma2 = cpt2.substr(cpt2.indexOf("-") + 1)

$("#methodsize-"+afterComma2).prop("disabled",true);
if(nb_btn_clickedMethod>=1)
{

$("#cellSizeMethod-"+(afterComma2)).prop("disabled",true);

}
if(nbElement2>0)

{
$("#elementsizemethod-"+(afterComma2)).prop("disabled",true);
}

}


if (($(this).find("option:selected").val()=="double-long-unsigned" ))

{
cpt2=$(this).prop('id');
var afterComma2 = cpt2.substr(cpt2.indexOf("-") + 1)

$("#methodsize-"+afterComma2).prop("disabled",true);
if(nb_btn_clickedMethod>=1)
{

$("#cellSizeMethod-"+(afterComma2)).prop("disabled",true);

}
if(nbElement2>0)

{
$("#elementsizemethod-"+(afterComma2)).prop("disabled",true);
}

}

if (($(this).find("option:selected").val()=="bcd" ))

{
cpt2=$(this).prop('id');
var afterComma2 = cpt2.substr(cpt2.indexOf("-") + 1)

$("#methodsize-"+afterComma2).prop("disabled",true);
if(nb_btn_clickedMethod>=1)
{

$("#cellSizeMethod-"+(afterComma2)).prop("disabled",true);

}
if(nbElement2>0)

{
$("#elementsizemethod-"+(afterComma2)).prop("disabled",true);
}

}


if (($(this).find("option:selected").val()=="integer" ))

{
cpt2=$(this).prop('id');
var afterComma2 = cpt2.substr(cpt2.indexOf("-") + 1)

$("#methodsize-"+afterComma2).prop("disabled",true);
if(nb_btn_clickedMethod>=1)
{

$("#cellSizeMethod-"+(afterComma2)).prop("disabled",true);

}
if(nbElement2>0)

{
$("#elementsizemethod-"+(afterComma2)).prop("disabled",true);
}

}

if (($(this).find("option:selected").val()=="long" ))

{
cpt2=$(this).prop('id');
var afterComma2 = cpt2.substr(cpt2.indexOf("-") + 1)

$("#methodsize-"+afterComma2).prop("disabled",true);
if(nb_btn_clickedMethod>=1)
{

$("#cellSizeMethod-"+(afterComma2)).prop("disabled",true);

}
if(nbElement2>0)

{
$("#elementsizemethod-"+(afterComma2)).prop("disabled",true);
}

}


if (($(this).find("option:selected").val()=="unsigned" ))

{
cpt2=$(this).prop('id');
var afterComma2 = cpt2.substr(cpt2.indexOf("-") + 1)

$("#methodsize-"+afterComma2).prop("disabled",true);
if(nb_btn_clickedMethod>=1)
{

$("#cellSizeMethod-"+(afterComma2)).prop("disabled",true);

}
if(nbElement2>0)

{
$("#elementsizemethod-"+(afterComma2)).prop("disabled",true);
}

}


if (($(this).find("option:selected").val()=="long-unsigned" ))

{
cpt2=$(this).prop('id');
var afterComma2 = cpt2.substr(cpt2.indexOf("-") + 1)

$("#methodsize-"+afterComma2).prop("disabled",true);
if(nb_btn_clickedMethod>=1)
{

$("#cellSizeMethod-"+(afterComma2)).prop("disabled",true);

}
if(nbElement2>0)

{
$("#elementsizemethod-"+(afterComma2)).prop("disabled",true);
}

}

if (($(this).find("option:selected").val()=="long64" ))

{
cpt2=$(this).prop('id');
var afterComma2 = cpt2.substr(cpt2.indexOf("-") + 1)

$("#methodsize-"+afterComma2).prop("disabled",true);
if(nb_btn_clickedMethod>=1)
{

$("#cellSizeMethod-"+(afterComma2)).prop("disabled",true);

}
if(nbElement2>0)

{
$("#elementsizemethod-"+(afterComma2)).prop("disabled",true);
}

}


if (($(this).find("option:selected").val()=="long64-unsigned" ))

{
cpt2=$(this).prop('id');
var afterComma2 = cpt2.substr(cpt2.indexOf("-") + 1)

$("#methodsize-"+afterComma2).prop("disabled",true);
if(nb_btn_clickedMethod>=1)
{

$("#cellSizeMethod-"+(afterComma2)).prop("disabled",true);

}
if(nbElement2>0)

{
$("#elementsizemethod-"+(afterComma2)).prop("disabled",true);
}

}


if (($(this).find("option:selected").val()=="enum" ))

{
cpt2=$(this).prop('id');
var afterComma2 = cpt2.substr(cpt2.indexOf("-") + 1)

$("#methodsize-"+afterComma2).prop("disabled",true);
if(nb_btn_clickedMethod>=1)
{

$("#cellSizeMethod-"+(afterComma2)).prop("disabled",true);

}
if(nbElement2>0)

{
$("#elementsizemethod-"+(afterComma2)).prop("disabled",true);
}

}

if (($(this).find("option:selected").val()=="float32" ))

{
cpt2=$(this).prop('id');
var afterComma2 = cpt2.substr(cpt2.indexOf("-") + 1)

$("#methodsize-"+afterComma2).prop("disabled",true);
if(nb_btn_clickedMethod>=1)
{

$("#cellSizeMethod-"+(afterComma2)).prop("disabled",true);

}
if(nbElement2>0)

{
$("#elementsizemethod-"+(afterComma2)).prop("disabled",true);
}

}

if (($(this).find("option:selected").val()=="float64" ))

{
cpt2=$(this).prop('id');
var afterComma2 = cpt2.substr(cpt2.indexOf("-") + 1)

$("#methodsize-"+afterComma2).prop("disabled",true);
if(nb_btn_clickedMethod>=1)
{

$("#cellSizeMethod-"+(afterComma2)).prop("disabled",true);

}
if(nbElement2>0)

{
$("#elementsizemethod-"+(afterComma2)).prop("disabled",true);
}

}


if (($(this).find("option:selected").val()=="date-time" ))

{
cpt2=$(this).prop('id');
var afterComma2 = cpt2.substr(cpt2.indexOf("-") + 1)

$("#methodsize-"+afterComma2).prop("disabled",true);
if(nb_btn_clickedMethod>=1)
{

$("#cellSizeMethod-"+(afterComma2)).prop("disabled",true);

}
if(nbElement2>0)

{
$("#elementsizemethod-"+(afterComma2)).prop("disabled",true);
}

}


if (($(this).find("option:selected").val()=="date" ))

{
cpt2=$(this).prop('id');
var afterComma2 = cpt2.substr(cpt2.indexOf("-") + 1)

$("#methodsize-"+afterComma2).prop("disabled",true);
if(nb_btn_clickedMethod>=1)
{

$("#cellSizeMethod-"+(afterComma2)).prop("disabled",true);

}
if(nbElement2>0)

{
$("#elementsizemethod-"+(afterComma2)).prop("disabled",true);
}

}


if (($(this).find("option:selected").val()=="time" ))

{
cpt2=$(this).prop('id');
var afterComma2 = cpt2.substr(cpt2.indexOf("-") + 1)

$("#methodsize-"+afterComma2).prop("disabled",true);
if(nb_btn_clickedMethod>=1)
{

$("#cellSizeMethod-"+(afterComma2)).prop("disabled",true);

}
if(nbElement2>0)

{
$("#elementsizemethod-"+(afterComma2)).prop("disabled",true);
}

}
//**********************fin modif


  if (selected=="array" |selected=="CHOICE" | selected=="compact array")
  {
         nb_btn_clickedMethod=0;
         indice2++;
//


             element = $('<tr    style="border-bottom: 1px solid LightSteelBlue;"><td></td><td  >' +
                             '</td>'+
                                 '<td ><center><input  type="button" class="btn-default" value="+" onclick="addCellMethod(this)" id="BtnAddCell2"></center>'+
//                     '<select  class="form-control" name="AttributeTypeArray" id="attributeTypeArray" onchange="GetSelectedTextValueArray(this)">'+
//                        '<option value="Select type" selected="selected">Select type</option>'+
//                        '<optgroup label="Simple Type">'+
//                            '<option value="null-data">null-data</option>'+
//                            '<option value="boolean">boolean</option>'+
//                            '<option value="bit-string">bit-string</option>'+
//                            '<option value="null-data">double-long</option>'+
//                            '<option value="double-long-unsigned">double-long-unsigned</option>'+
//                            '<option value="octet-string">octet-string</option>'+
//                            '<option value="visible-string">visible-string</option>'+
//                            '<option value="utf8-string">utf8-string</option>'+
//                            '<option value="bcd">bcd</option>'+
//                            '<option value="integer">integer</option>'+
//                            '<option value="long">long</option>'+
//                            '<option value="unsigned">unsigned</option>'+
//                            '<option value="long-unsigned">long-unsigned</option>'+
//                            '<option value="long64">long64</option>'+
//                            '<option value="long64-unsigned">long64-unsigned</option>'+
//                            '<option value="enum">enum</option>'+
//                            '<option value="float32">float32</option>'+
//                            '<option value="float64">float64</option>'+
//                            '<option value="date-time">date-time</option>'+
//                            '<option value="date">date</option>'+
//                            '<option value="time">time</option>'+
//
//                        '</optgroup>'+
//                        '<optgroup label="Complex Type">'+
//                            '<option value="array">array</option>'+
//                            '<option value="structure">structure</option>'+
//                            '<option value="compact array">compact array</option>'+
//                            '<option value="CHOICE">CHOICE</option>'+
//                        '</optgroup>'+
//                     '</select>'+
                                    '</td>'+
                                 ' <td >'+

                                  '</td>'+
                                  '<td><input class="btn btn-danger"type="button" value="Remove" onclick="remove2(this)"></td></tr>');


                        $(this).closest('tr').after(element);
//
//



if (att== '' & selected=="array")
      {
//      $("#BtnAddCell2").prop("disabled",true);

      }
      if (att== '')
//        $("#BtnAddCell2").prop("disabled",true);
      {

      }
if (att != '')
{
  $("#BtnAddCell2").prop("disabled",false);
 }



}

if (selected=="structure")

{
nb++;
var afterComma2 = cpt2.substr(cpt2.indexOf("-") + 1)
$("#cellSizeMethod-"+afterComma2).prop("disabled",true);
$("#elementsizemethod-"+(afterComma2)).prop("disabled",true);
$("#methodsize-"+afterComma2).prop("disabled",true);


                     element = $('<tr   style="border-bottom: 1px solid LightSteelBlue;" id="'+nb+'">'+
                    '<td></td><td></td>'+
                    '<td >'+
                    '<center><input class="btn btn-primary" type="button" value="addStructure" name="size" onclick="addStructureSizeMethod()"></center> '+
                     '</td>'+
                     '<td >'+


                    '</td>'+
                    '<td ><input class="btn btn-danger"type="button" value="Remove" onclick="remove2(this)" ></td>'+



                '</tr>');
               $(this).closest('tr').after(element);

//index++;



}

});




function addCellMethod(value)

        {





indice2++;

//s=document.getElementById("cellSize").value;

        att=document.getElementById("methodsize-"+idselect2).value;
//      for (var i = 0;i<nbappel; i++) {
//      t(i)=nbappel;
//      }


//            if (nbremove >0 )
//            {
//
//            nb_btn_clicked=attrSize-nbremove;
//            nbremove=0;
//             }
//
//            else
            if(nbremove2 >=methodSize)
             {
             nb_btn_clickedMethod=0;
             nbremove2=0;
             }

             if(nbremove2==myArray2[nbappel2-2])


             {
                nb_btn_clickedMethod=0;
                nbremove2=0;

             }
//            if (nbremove>0 & nbremove<attrSize)
//
//            {
//            nb_btn_clicked=attrSize-nbremove;
//
//            }
if(nbappel2>1 & (methodSize!=myArray2[nbappel2-2]))
{
nbappel2=0;
nb_btn_clickedMethod=0;
}

if (nbremove2==myArray2[nbappel2-2] & myArray2[nbappel2-2]!=methodSize)
{
nb_btn_clickedMethod=0;
nbremove2=0;
}



if (nbremove2 !=0 & nbremove2 < methodSize & myArray2[nbappel2-2]!=methodSize)

{
nb_btn_clickedMethod=methodSize-nbremove2;
nbremove2=0;
}


if ($("#check").length==0)
{
test=true;
}
//if(test==true & nbremove2!=0)
//{
//nb_btn_clickedMethod=0;
//}



            nb_btn_clickedMethod++;

                     if (att=="" )
                     {
//                      $("#BtnAddCell2").prop("disabled",true);
                     }
              if (methodSize==0)
                     {
//                     $("#BtnAddCell2").prop("disabled",true);
                     }

           if (nb_btn_clickedMethod <= methodSize ){
             element = $('<tr style="border-bottom: 1px solid LightSteelBlue; id="check"><td ></td><td  >' +
                    '</td>'+
                    '<td >'+
                     '<select  class="form-control"    id="methodType-' + (idselect2) +  "-" +nb_btn_clickedMethod+ "-"+indice2+ "-" +nbclicstructure2+ '" name="methodType-' + (idselect2) +  "-" +nb_btn_clickedMethod+ "-"+indice2+ "-" +nbclicstructure2+ '">'+
                        '<option value="Select type" selected="selected">Select type</option>'+
                        '<optgroup label="Simple Type">'+
                            '<option value="null-data">null-data</option>'+
                            '<option value="boolean">boolean</option>'+
                            '<option value="bit-string">bit-string</option>'+
                            '<option value="double-long">double-long</option>'+
                            '<option value="double-long-unsigned">double-long-unsigned</option>'+
                            '<option value="octet-string">octet-string</option>'+
                            '<option value="visible-string">visible-string</option>'+
                            '<option value="utf8-string">utf8-string</option>'+
                            '<option value="bcd">bcd</option>'+
                            '<option value="integer">integer</option>'+
                            '<option value="long">long</option>'+
                            '<option value="unsigned">unsigned</option>'+
                            '<option value="long-unsigned">long-unsigned</option>'+
                            '<option value="long64">long64</option>'+
                            '<option value="long64-unsigned">long64-unsigned</option>'+
                            '<option value="enum">enum</option>'+
                            '<option value="float32">float32</option>'+
                            '<option value="float64">float64</option>'+
                            '<option value="date-time">date-time</option>'+
                            '<option value="date">date</option>'+
                            '<option value="time">time</option>'+

                        '</optgroup>'+
                        '<optgroup label="Complex Type">'+
                            '<option value="array">array</option>'+
                            '<option value="structure">structure</option>'+
                            '<option value="compact array">compact array</option>'+
                            '<option value="CHOICE">CHOICE</option>'+
                        '</optgroup>'+
                     '</select><center></center>'+
                    '</td>'+
                 ' <td >'+
'<input type="text" class="form-control" placeholder="size" id="cellSizeMethod-' + (idselect2) + "-" +nb_btn_clickedMethod+ "-" +indice2+ "-" +nbclicstructure2+'" name="cellSizeMethod-' + (idselect2) + "-" +nb_btn_clickedMethod+ "-" +indice2+ "-" +nbclicstructure2+'" onblur="GetSizeArrayMethod(this.value)">'+
                  '</td>'+
                  '<td><input class="btn btn-danger"type="button" value="Remove" onclick="remove2(this)" ></td></tr>');

//            $("#table_class").append(element);
             $(value).closest('tr').after(element);}


             else {

                 depasse++;

//                 $("#BtnAddCell2").prop("disabled",true);
                 }


                     if (methodSize==nb_btn_clickedMethod )
                 {

//                  $("#BtnAddCell2").prop("disabled",true);
                 }
//                 if (document.getElementById("cellSize").value=="")
//                 {
//                 $("#BtnAddCell").prop("disabled",true);
//
//                 }

                 if (document.getElementById("cellSizeMethod-"+idselect2).value==nb_btn_clickedMethod)
                 {
//                 $("#BtnAddCell2").prop("disabled",true);




                 }
      }




        function GetSizeArrayMethod (value)
        {


            if(nbremove2==myArray2[nbappel2-2])


                         {
                            nb_btn_clickedMethod=0;

                         }
             if(nbremove2==methodSize)


                         {
                            nb_btn_clickedMethod=0;

                         }


                 if( nbremove2!=0)
                 {
                 nb_btn_clickedMethod=nb_btn_clickedMethod;
                 }
            if(nbremove2!=0 &myArray2[nbappel2-1]!=methodSize)
            {

            if(methodSize==myArray2[nbappel2-2]-nbremove2)
                {

//                 $("#BtnAddCell2").prop("disabled",true);
                }
                else
                     { nb_btn_clickedMethod=0;}
            }
         methodSize=value;

if (nbremove2 !=0 & nbremove2 < methodSize)

{
nb_btn_clickedMethod=methodSize-nbremove2-1;
nbremove2=0;
}
if (nbremove2==myArray2[nbappel2-2] & myArray2[nbappel2-2]!=methodSize)
{
nb_btn_clickedMethod=0;
nbremove2=0;
}

if (nbremove2!=0)
{
if(methodSize==myArray2[nbappel2-2]-nbremove2)
{

nb_btn_clickedMethod=myArray2[nbappel2-2]-nbremove2;
}



}




         }







     function GetStructureSizeMethod(value,val)
{

//     document.getElementById("cellSizeMethod").disabled = true;
id=$(val).prop('id');
    nbElement2=value;
//    ***************************

  ch2 = ch2.concat(nbElement2.toString());
  ch2=ch2.concat("-");

   listCh2.push(ch2);
//**************************


    if (nbElement2==0)
    {
      element = $('<tr style="border-bottom: 1px solid LightSteelBlue;">'+
                            '<td></td><td></td>'+
                            '<td >'+
                                '<center>ElementName:<br><input class="form-control" type="text" id="elementname" size="10" placeholder="empty" disabled="true"></center>'+
                                 '<center>ElementType:<br>'+



                        '<select  class="form-control"  disabled="true">'+
                        '<option value="Select type" selected="selected">Select type</option>'+
                        '<optgroup label="Simple Type">'+
                            '<option value="null-data">null-data</option>'+
                            '<option value="boolean">boolean</option>'+
                            '<option value="bit-string">bit-string</option>'+
                            '<option value="double-long">double-long</option>'+
                            '<option value="double-long-unsigned">double-long-unsigned</option>'+
                            '<option value="octet-string">octet-string</option>'+
                            '<option value="visible-string">visible-string</option>'+
                            '<option value="utf8-string">utf8-string</option>'+
                            '<option value="bcd">bcd</option>'+
                            '<option value="integer">integer</option>'+
                            '<option value="long">long</option>'+
                            '<option value="unsigned">unsigned</option>'+
                            '<option value="long-unsigned">long-unsigned</option>'+
                            '<option value="long64">long64</option>'+
                            '<option value="long64-unsigned">long64-unsigned</option>'+
                            '<option value="enum">enum</option>'+
                            '<option value="float32">float32</option>'+
                            '<option value="float64">float64</option>'+
                            '<option value="date-time">date-time</option>'+
                            '<option value="date">date</option>'+
                            '<option value="time">time</option>'+

                        '</optgroup>'+
                        '<optgroup label="Complex Type">'+
                            '<option value="array">array</option>'+
                            '<option value="structure">structure</option>'+
                            '<option value="compact array">compact array</option>'+
                            '<option value="CHOICE">CHOICE</option>'+
                        '</optgroup>'+
                     '</select>'+
                    '<center>ElementSize:<br><input class="form-control" type="text" id="elementsizemethod" size="10" onblur="GetSizeArrayMethod(this.value)" disabled="true"></center>'+
                                 '</center><br>'+
                             '</td>'+
                             '<td >'+
                             '<center></center>'+

                            '</td>'+

                    '<td >'+
                             '<center></center>'+
                             '<input class="btn btn-danger"type="button" value="Remove" onclick="remove2(this)">'+

                            '</td>'+



                        '</tr>');

       $(val).closest('tr').after(element);
}







    for (var i=0; i<nbElement2; i++)
    {
            element = $('<tr style="border-bottom: 1px solid LightSteelBlue;">'+
                            '<td></td><td></td>'+
                            '<td >'+
                                '<center>ElementName:<br><input class="form-control" type="text" id="elementname" size="10"></center>'+
                                 '<center>ElementType:<br>'+



                        '<select  class="form-control" id="methodType-' + (idselect2) +  "-" +nb_btn_clickedMethod+  "-"+(i)+  "-" +nb+'" name="methodType-' + (idselect2) +  "-" +nb_btn_clickedMethod+  "-"+(i)+  "-" +nb+'" >'+
                        '<option value="Select type" selected="selected">Select type</option>'+
                        '<optgroup label="Simple Type">'+
                            '<option value="null-data">null-data</option>'+
                            '<option value="boolean">boolean</option>'+
                            '<option value="bit-string">bit-string</option>'+
                            '<option value="double-long">double-long</option>'+
                            '<option value="double-long-unsigned">double-long-unsigned</option>'+
                            '<option value="octet-string">octet-string</option>'+
                            '<option value="visible-string">visible-string</option>'+
                            '<option value="utf8-string">utf8-string</option>'+
                            '<option value="bcd">bcd</option>'+
                            '<option value="integer">integer</option>'+
                            '<option value="long">long</option>'+
                            '<option value="unsigned">unsigned</option>'+
                            '<option value="long-unsigned">long-unsigned</option>'+
                            '<option value="long64">long64</option>'+
                            '<option value="long64-unsigned">long64-unsigned</option>'+
                            '<option value="enum">enum</option>'+
                            '<option value="float32">float32</option>'+
                            '<option value="float64">float64</option>'+
                            '<option value="date-time">date-time</option>'+
                            '<option value="date">date</option>'+
                            '<option value="time">time</option>'+

                        '</optgroup>'+
                        '<optgroup label="Complex Type">'+
                            '<option value="array">array</option>'+
                            '<option value="structure">structure</option>'+
                            '<option value="compact array">compact array</option>'+
                            '<option value="CHOICE">CHOICE</option>'+
                        '</optgroup>'+
                     '</select>'+

                        '<center>ElementSize:<br><input class="form-control" type="text"id="elementsizemethod-' + (idselect2) +  "-" +nb_btn_clickedMethod+  "-"+(i)+  "-" +nb+'" size="10"  onblur="GetSizeArrayMethod(this.value)"></center>'+

                                 '</center><br>'+
                             '</td>'+
                             '<td >'+
                             '<center></center>'+

                            '</td>'+

                    '<td >'+
                             '<center></center>'+
                             '<input class="btn btn-danger"type="button" value="Remove" onclick="remove2(this)">'+

                            '</td>'+



                        '</tr>');

       $(val).closest('tr').after(element);


//        $("input#"+id).closest().after(element);
}

element2 = $('<input id="hidden" type="hidden" name="nbelementM" value="'+listCh2+'" >');
  $(val).closest('tr').after(element2);


    return false;
    }


    function addStructureSizeMethod()


    {


nbclicstructure2++;
indice2++;

    var nbElement2=0;
//nb++;


  element = $('<tr style="border-bottom: 1px solid LightSteelBlue;"  id="'+(nb)+'">'+
                    '<td></td><td></td>'+
                    '<td >'+
                    '<center></center>'+
                        '<center>StructureSize:<br><input class="form-control" type="text" id="structuresize-' + (idselect2) +  "-" +nb_btn_clickedMethod+  "-" +(nbclicstructure2)+'" name="structuresize-' + (idselect2) +  "-" +nb_btn_clickedMethod+  "-" +(nbclicstructure2)+'" size="5" onblur="GetStructureSizeMethod(this.value,this)">'+
                        '<td >'+


                         '</center>'+

                     '</td>'+

                 '<td> <input class="btn btn-danger"type="button" value="Remove" onclick="remove2(this)"></td>'+



//                  '<td></td>'+


                '</tr>');
//                 $('#table_class').append(element);
//                 $('#table_class > tbody > tr').eq($('tr').index($(this))).after(element);
//                   $(this).after(element);
//                    $(element).insertAfter("#1");
//                        $(this).closest('tr').after(element);
//                        $("<tr>").attr({"id":"id_"+nb}).appendTo("#table_class");
//                         $('#table_class #'+nb+).after(element);
//                         $(element).insertAfter( $("#" +nb ) );
                            $(element).insertAfter( $("#"+nb ) );
//                         $(this).closest('tr').after(element);






}


