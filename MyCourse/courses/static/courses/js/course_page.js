var player;

    document.onreadystatechange = function(){
    if(document.readyState == 'interactive'){
    player=document.getElementById('player')
     mentainRation()
    }
    }
    function mentainRation(){
    var w=player.clientWidth
    var h=(w*9)/16
    console.log({w,h});
    player.height=h
    }
    window.onresize=mentainRation