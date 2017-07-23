$(document).ready(function (){
var isHidden = false;
$("#clicker").click( function (){

if(isHidden){
        $(".list").show();
}else{
        $(".list").hide();
}
isHidden = !isHidden;
})

$('#my_name').t({
    speed:70,
    blink:400,
    mistype:0,
    pause_on_click:true
});

})