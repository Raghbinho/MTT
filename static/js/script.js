$(document).ready(function(){
try {
try {
    console.log("start");
      $('input#submit').click(function(){
//          element = $('<input type="text"/>');
          element = $('<tr><td width="300px"></td><td width="300px" > ' +
          '</td><td width="300px"> ' +
                       ' <input type="text" name="AttributeID"> '+
                    '</td>' +

                    '<td width="300px">'+
                        '<input type="text" name="AttributeName">'+
                    '</td>'+
                    '<td width="300px">'+
                     '<select name="AttributeType" id="attributeType">'+
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
                    '<input type="text" name="AttributeSize">'+
                  '</td>'+


                '</tr>');
          $("#table_class").append(element);
          return false;
      });



        $('input#methodsubmit').click(function(){
//          element = $('<input type="text"/>');
          element = $('<tr><td width="300px" > ' +
          '</td><td width="300px"> ' +
                       ' <input type="text" name="MethodeID"> '+
                    '</td>' +

                    '<td width="300px">'+
                        '<input type="text" name="MethodeName">'+
                    '</td>'+
                    '<td width="300px">'+
                     '<select name="MethodeType" id="methodeType">'+
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