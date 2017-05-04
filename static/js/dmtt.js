
$(document).on('click', '#close-preview', function(){
    $('.image-preview').popover('hide');
    // Hover befor close the preview
    $('.image-preview').hover(
        function () {
           $('.image-preview').popover('show');
        },
         function () {
           $('.image-preview').popover('hide');
        }
    );
});

$(function() {
    // Create the close button
    var closebtn = $('<button/>', {
        type:"button",
        text: 'x',
        id: 'close-preview',
        style: 'font-size: initial;',
    });
    closebtn.attr("class","close pull-right");
    // Set the popover default content
    $('.image-preview').popover({
        trigger:'manual',
        html:true,
        title: "<strong>Preview</strong>"+$(closebtn)[0].outerHTML,
        content: "There's no image",
        placement:'bottom'
    });
    // Clear event
    $('.image-preview-clear').click(function(){
        $('.image-preview').attr("data-content","").popover('hide');
        $('.image-preview-filename').val("");
        $('.image-preview-clear').hide();
        $('.image-preview-input input:file').val("");
        $(".image-preview-input-title").text("Browse");
    });
    // Create the preview image
    $(".image-preview-input input:file").change(function (){
        var img = $('<img/>', {
            id: 'dynamic',
            width:250,
            height:200
        });
        var file = this.files[0];
        var reader = new FileReader();
        // Set preview image into the popover data-content
        reader.onload = function (e) {
            $(".image-preview-input-title").text("Change");
            $(".image-preview-clear").show();
            $(".image-preview-filename").val(file.name);
            img.attr('src', e.target.result);
//            $(".image-preview").attr("data-content",$(img)[0].outerHTML).popover("show");
        }
        reader.readAsDataURL(file);
    });
});
/**************************** prograss bar *************************/
$(document).ready(function() {
    $('.progress').css('width', 0 + "%");
           document.getElementById("demo").innerHTML = Math.round(0) +"%";
    $("#run").click(function(){

        var myVar=setInterval(function(){myTimer()},1);
        var count = 0;
        function myTimer() {
        if(count < 100){
          $('.progress').css('width', count + "%");
          count += 0.05;
           document.getElementById("demo").innerHTML = Math.round(count) +"%";
           $("#textarea ").html('Evolution of execution : '+ Math.floor( count )+'% ...');
          }
          else if(count > 99){
          count = 0;

          }
        }
    });
});

/********************* port ****************/
function myFunction() {
    var x = $('#Port').find(":selected").text();
    var y = $('#Baudrate').find(":selected").text();
    alert(x);
    alert(y);
    f();
    $.ajax({
          type: "POST",
          cache: true,
          url: "/DMTTExecution/",
          data:  { port : x, baud : y},
                success: function(result, textStatus, jqXHR)
                {
                    $("#textarea ").html(result);
                }
            });
}
/*******interface choice *******************/
function interfaceChoice(){
                var e = document.getElementById("Interface");
                var choice = e.options[e.selectedIndex].text;
                if(choice == 'HDLC'){
                        var x = document.getElementById("PortInvisible");
                        var txt = "";
                        for (var i = 0; i < x.length; i++) {
                            txt +="\n" + x.options[i].text;
                        }
                        var res = txt.split('\n');
                        var options = '';
                        for(var i=1;i<res.length;i++){
                            options += '<option>'+res[i]+'</option>';
                        }
                        var htm3 = [
                                   '<label class="control-label" for="Port">Port</label>',
                                   '<select id="Port" name="Port" class="form-control" >',
                        ].join('');
                        document.getElementById('idChoice').innerHTML = htm3 + options + '</select';
                }else if(choice == 'VALID_DC'){
                        var htm1 = [
                                   '<label class="control-label" for="Port">IP adress</label>',
                                   '<input class="form-control" type="text" placeholder="IP adress"/>',
                                   '<label class="control-label" for="Port">Serial Number</label>',
                                   '<input class="form-control" type="text" placeholder="Serial Number"/>',
                        ].join('');
                        document.getElementById('idChoice').innerHTML = htm1;
                }else if(choice == 'TCP/IP'){
                        var htm2 = [
                                   '<label class="control-label" for="Port">IP adress</label>',
                                   '<input class="form-control" type="text" placeholder="IP adress"/>',
                        ].join('');
                        document.getElementById('idChoice').innerHTML = htm2;
                }
}
