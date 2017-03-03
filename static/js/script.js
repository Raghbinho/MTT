
$(document).ready(function(){
try {
try {
    console.log("start");
      $('input#submit').click(function(){
//          element = $('<input class="form-control" type="text"/>');



          element = $('<tr id=><td > ' +
                       ' <input class="form-control" type="text" name="AttributeID"> '+
                    '</td>' +

                    '<td >'+
                        '<input class="form-control" type="text" name="AttributeName">'+
                    '</td>'+
                    '<td >'+
                     '<select  class="form-control" name="AttributeType" id="attributeType"  >'+
                        '<option value="Select type" selected="selected">Select type</option>'+
                        '<optgroup label="Simple Type">'+
                            '<option value="null-data">null-data</option>'+
                            '<option value="boolean">boolean</option>'+
                            '<option value="bit-string">bit-string</option>'+
                            '<option value="null-data">double-long</option>'+
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
                    '<input class="form-control" type="text" name="AttributeSize" id="atributesize"onchange="GetArraySize(this.value)">' +
                  '</td>'+
                  ' <td width="100px">'+
                  '<input class="btn btn-danger" type="button" value="Remove" >' +
                    '</td>'+

                '</tr>');
          $("#table_class").append(element);




          return false;
           ;
      });



        $('input#methodsubmit').click(function(){
//          element = $('<input class="form-control" type="text"/>');
          element = $('<tr><td > ' +
                       ' <input class="form-control" type="text" name="MethodeID"> '+
                    '</td>' +

                    '<td >'+
                        '<input class="form-control" type="text" name="MethodeName">'+
                    '</td>'+
                    '<td >'+
                     '<select  class="form-control" name="MethodeType" id="methodeType">'+
                        '<option value="Select type" selected="selected">Select type</option>'+
                        '<optgroup label="Simple Type">'+
                            '<option value="null-data">null-data</option>'+
                            '<option value="boolean">boolean</option>'+
                            '<option value="bit-string">bit-string</option>'+
                            '<option value="null-data">double-long</option>'+
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
                     '<td width="100px">' +
                     '<input class="btn btn-danger"type="button" value="Remove" >'+
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
        alert("Selected Text: " + selectedText + " Value: " + selectedValue);

        if (selectedValue=="array")

        {







           element = $('<tr><td width="300px"></td><td width="300px" > ' +
          '</td>'+
                    '<td width="300px">'+
                     '<select  class="form-control" name="AttributeTypeArray" id="attributeTypeArray" onchange="GetSelectedTextValueArray(this)">'+
                        '<option value="Select type" selected="selected">Select type</option>'+
                        '<optgroup label="Simple Type">'+
                            '<option value="null-data">null-data</option>'+
                            '<option value="boolean">boolean</option>'+
                            '<option value="bit-string">bit-string</option>'+
                            '<option value="null-data">double-long</option>'+
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
                    ''+
                  '</td>'+
                  '<td><input class="btn btn-danger"type="button" value="Remove" ></td>'+


                '</tr>');
                $("#table_class").append(element);
        }
 return false
    }
 function GetSelectedTextValueArray(attributeTypeArray)
 {
        var selectedText = attributeTypeArray.options[attributeTypeArray.selectedIndex].innerHTML;
        var selectedValue = attributeTypeArray.value;
        if (selectedValue=="structure")
        {
        alert("Selected Text structure: " + selectedText );
//        addTable();


//        element = $('<tr><td width="300px"></td><td width="300px" > ' +
//          '</td><td width="300px"> ' +
//                       ' '+
//                    '</td>' +
//
//                    '<td width="300px">'+
//                        ''+
//                    '</td>'+
//                    '<td><center>'+
//                    'StructureSize'+'<br>'+
//                    '<input class="form-control" type="text" value="" size="5" id="structuresize" onchange="GetStructureSize(this.value)"></center>'+
////                    '</td>'+'</tr>'+'<tr>'+'<td></td><td></td><td></td><td></td>'+
////                    '<td width="300px">'+
////                     '<center>ElementType</center>'+
////                     '<input class="form-control" type="text" name="elementType">'+'</td>'+
////                     '<td width="300px">'+
////                     '<center>ElementName</center>'+
////                     '<input class="form-control" type="text" name="elementname">'+
////                    '</td>'+
////                    '</td>'+
//                 ' <td width="300px">'+
//                    ''+
//                  '</td>'+
//
//
//                '</tr>');
//                $("#table_class").append(element);

//********************for adding structures****************************************



// element = $('<tr>'+
//                    '<td></td><td></td><td></td><td></td>'+
//                    '<td width="300px">'+
//                     '<center></center>'+
//                     '</td>'+
//                     '<td width="300px">'+
//                     '<center></center>'+
//
//                    '</td>'+
//                    '</td>'+
//                 ' <td width="300px">'+
//
//                  '</td>'+
//
//
//                '</tr>');
//                $("#table_class").append(element);








        }
  return false


 }
//function GetStructureSize(value)
//{
//    var e=document.getElementById("structuresize").value ;
//    alert(value);
//    return false;
//}
var attrSize="";
 function GetArraySize(value)
  {
      attrSize=document.getElementById("atributesize").value ;
     alert(attrSize);
     return false;
   }
  function addTable()
  {


                     element = $('<tr>'+
                    '<td></td><td></td>'+
                    '<td width="300px">'+
                    '<input class="btn btn-primary" type="button" id="size" value="addStructure" onclick="addStructureSize()"> '+
                     '</td>'+
                     '<td width="300px">'+


                    '</td>'+
                    '<td><input class="btn btn-danger"type="button" value="Remove" ></td>'+



                '</tr>');
                $("#table_class").append(element);




                return false;
                }
// ***********************************************               number of elements***********************************************

function getElementsNumber(value)

{

    nbElement=value;
    alert (nbElement);
    for (var i=0; i<nbElement; i++)
    {
    element = $('<tr>'+
                    '<td></td><td></td>'+
                    '<td width="300px">'+
                        '<center>ElementName:<br><input class="form-control" type="text" id="elementname" size="10"></center>'+
                         '<center>ElementType:<br><input class="form-control" type="text" id="elementtype" size="10"></center><br>'+
                     '</td>'+
                     '<td width="300px">'+
                     '<center></center>'+

                    '</td>'+

            '<td width="300px">'+
                     '<center></center>'+
                     '<input class="btn btn-danger"type="button" value="Remove" >'+

                    '</td>'+



                '</tr>');
$("#table_class").append(element);

    }



}

function addStructureSize()
{
var nbElement=""
  element = $('<tr>'+
                    '<td></td><td></td>'+
                    '<td width="300px">'+
                     '<input class="btn btn-primary" type="button" value="addStructure" onclick="addStructureSize()">'+
                        '<center>StructureSize:<br><input class="form-control" type="text" id="structuresize" onchange="getElementsNumber(this.value)" size="5"> <td width="300px">'+


                         '</center>'+

                     '</td>'+

                 '<td><input class="btn btn-danger"type="button" value="Remove" ></td>'+



//                  '<td></td>'+


                '</tr>');
                $("#table_class").append(element);

}

//******************************************delete line********************************************

$('#table_class').on('click', 'input[type="button"]', function () {
    $(this).closest('tr').remove();
})
$('#table_methode').on('click', 'input[type="button"]', function () {
    $(this).closest('tr').remove();
})



function test(){
   alert("test");
//    var doc = document.implementation.createDocument ('http://www.w3.org/1999/xhtml', 'html', null);
//    var body = document.createElementNS('http://www.w3.org/1999/xhtml', 'body');
//    body.setAttribute('id', 'abc');
//    doc.documentElement.appendChild(body);
//    alert(doc.getElementById('abc')); // [object HTMLBodyElement];
//        var xmlDoc = document.implementation.createDocument(null, 'root', null);
//
//        var foo = xmlDoc.createElement('foo');
//        foo.textContent = 'bar';
//
//        xmlDoc.documentElement.appendChild(foo);
//
//        console.log(xmlDoc);
//        alert("XML created");

//var fso = new ActiveXObject("Scripting.FileSystemObject");
//// 2=overwrite, true=create if not exist, 0 = ASCII
//varFileObject = fso.OpenTextFile("Bibliothèques\Documents", 2, true,0);
//varFileObject.write("File handling in Javascript");
//varFileObject.close();
//alert("file is created");

//var XML = new XMLWriter();
//XML.BeginNode("Foo");
//XML.Attrib("Bar", "Some Value");
//XML.EndNode();
//XML.Node("MyNode", "My Value");
//alert("xml created");
//var doc = document.implementation.createDocument(null, "report", null);

//  if (document.implementation.createDocument &&
//                document.implementation.createDocumentType)
//            {
//                var fruitDocType = document.implementation.createDocumentType ("fruit", "SYSTEM", "<!ENTITY tf 'tropical fruit'>");
//                var xmlDoc = document.implementation.createDocument ("", "fruits", fruitDocType);
//
//                var fruitNode = xmlDoc.createElement ("fruit");
//                fruitNode.setAttribute ("name" , "avocado");
//                xmlDoc.documentElement.appendChild (fruitNode);
//
//
//
//                var serializer = new XMLSerializer();
//
//                alert (serializer.serializeToString (xmlDoc));
//
//})
//            }
//            else {
//                alert ("Your browser does not support this example");
//            }

function generateXML(){
    // Simple helper function creates a new element from a name, so you don't have to add the brackets etc.
    $.createElement = function(name)
    {
        return $('<'+name+' />');
    };

    // JQ plugin appends a new element created from 'name' to each matched element.
    $.fn.appendNewElement = function(name)
    {
        this.each(function(i)
        {
            $(this).append('<'+name+' />');
        });
        return this;
    }

    /* xml root element - because html() does not include the root element and we want to
        * include <report /> in the output. There may be a better way to do this.
        */
    var $root = $('<XMLDocument />');

    $root.append
    (
    // one method of adding a basic structure
    $('<plist />').append(
    $('<dict />').append(
    $('<key />').text('subject'),
    $('<string />').text('September 21'),
    $('<key />').text('date'),
    $('<string />').text('FOB10 Room'),
    $('<key />').text('time'),
    $('<string />').text('2.00 pm - 5.00 pm'),
    $('<key />').text('briefings'),

    $('<array />').append
    (
    $('<dict />').append
    (
    $('<key />').text('files'),
    $('<array />').append
    (
    $('<dict />').append
    (
    $('<key />').text('date'),
    $('<string />').text('09/09/2012'),
    $('<key />').text('name'),
    $('<string />').text('acatBriefing.pdf'),
    $('<key />').text('description'),
    $('<string />').text('ACAT Briefing')
)
),
    $('<key />').text('subject'),
    $('<string />').text('FAE approved ACAT Designations'),
    $('<key />').text('presenter'),
    $('<string />').text('Rebecca T. King'),
    $('<key />').text('time'),
    $('<string />').text('2.00 - 2.05 PM')

)
)
)
)
);


    alert($root.html());
}
generateXML();


}
$('#form1').on('change', ' select', function(){
//    $(this).closest('tr').find('input[name="dbFlag"]').val('U');

 var selected = $(this).find("option:selected").val();
  if (selected=="array")
  {

   element = $('<tr><td width="300px"></td><td width="300px" > ' +
          '</td>'+
                    '<td width="300px">'+
                     '<select  class="form-control" name="AttributeTypeArray" id="attributeTypeArray" onchange="GetSelectedTextValueArray(this)">'+
                        '<option value="Select type" selected="selected">Select type</option>'+
                        '<optgroup label="Simple Type">'+
                            '<option value="null-data">null-data</option>'+
                            '<option value="boolean">boolean</option>'+
                            '<option value="bit-string">bit-string</option>'+
                            '<option value="null-data">double-long</option>'+
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
                    ''+
                  '</td>'+
                  '<td><input class="btn btn-danger"type="button" value="Remove" ></td></tr>');

//            $("#table_class").append(element);
             $(this).closest('tr').after(element);

}

if (selected=="structure")

{

                     element = $('<tr>'+
                    '<td></td><td></td>'+
                    '<td width="300px">'+
                    '<input class="btn btn-primary" type="button" value="addStructure" id ="size" onclick="addStructureSize()"> '+
                     '</td>'+
                     '<td width="300px">'+


                    '</td>'+
                    '<td><input class="btn btn-danger"type="button" value="Remove" ></td>'+



                '</tr>');
               $(this).closest('tr').after(element);


}

});





