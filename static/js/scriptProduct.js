//*******************add client button
var nbclient=0;
     $('input#addClient').click(function(){

          nbclient++;
          element = $('<tr><td></td><td  ><input class="form-control" type="text" name="clientAdress-' + nbclient + '" id="clientAdress-' + nbclient + '"  onchange="GetClientAdress(this)"  ></td>'+
          '<td  width="200px"><input class="form-control" type="text" name="associationName-' + nbclient + '" id="associationName-' + nbclient + '" onchange="GetAssociationName(this)" >'+
          '<input type="hidden" name="nbclient" value='+nbclient+'></td>'+
           '<td><button class="btn btn-danger" onclick="removeclient(this)" ><span class="glyphicon glyphicon-remove"></span></td>'+

          '</tr>' );
          $("#TableClient1").append(element);
          return false;

      });
// *********************************************
function removeclient(value)
{
$(value).closest('tr').remove();
}
//**********************************************
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
