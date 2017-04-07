//*******************add client button
var nbclient=0;
     $('input#addClient').click(function(){
          nbclient++;
          element = $('<tr><td><input class="form-control" type="text" name="clientAdress-' + nbclient + '" id="clientAdress-' + nbclient + '"  onchange="GetClientAdress(this)"  ></td>'+
          '<td><input class="form-control" type="text" name="associationName-' + nbclient + '" id="associationName-' + nbclient + '" onchange="GetAssociationName(this)" >'+
          '<input type="hidden" name="nbclient" value='+nbclient+'></td>'+
          '</tr>' );
          $("#TableClient").append(element);
          return false;

      });
// *********************************************
function GetClientAdress(value)
{
//alert('id '+ $(value).prop('id'))
}
//********************************************
function GetAssociationName(value)
{
//alert('id '+ $(value).prop('id'))
}
//**********************************************
$(":file").change(function(){
   filename=$(":file").val();
   document.getElementById("filename").value=filename;
    });
//    ***********************************************


$("#productName").change(function(){
product=document.getElementById("productName").value

    });
