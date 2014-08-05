function randomizeX() { return randomize((browserWidth()-800)); }
function randomizeY() { return (browserHeight()-randomize(40)-40); }
totalCount = 0
function moveUp() {
    this.count+=Math.random()*10;
    this.y -= this.z;
    this.x+=(Math.cos(this.count));

    if (this.y<32) {
        clearInterval(this.loopID);
        this.y = 99999;
        // 'body'.removeChild(this.name);
        totalCount += 1;
        setTimeout('startBubbles(4, '+totalCount+');',300);
    }
    move(this.name,this.x,this.y);
}



function makeDiv(objName,x,y,content,w,h,overfl,parentDiv) {
        if (parentDiv==null) parentDiv='body';
        var oDiv = document.createElement ("DIV");
    oDiv.id = objName;
    if (w) oDiv.style.width = w;
        if (h) oDiv.style.height= h;
        if (content) oDiv.innerHTML=content;
        oDiv.style.position = "absolute";
        if (x) oDiv.style.left=x; else oDiv.style.left=-2000;
        if (y) oDiv.style.top=y; else oDiv.style.top=-2000;
        if (overfl) oDiv.style.overflow=overfl; else oDiv.style.overflow="hidden";
    eval('  document.'+parentDiv+'.appendChild (oDiv);  ');
        delete oDiv;
}


function randomize(maxNumber) { var r=Math.random()*maxNumber; r=Math.floor(r); return (r+1); }

// Got to have this for my website or else it will strangely produce an error in IE... .:s
document.body.onLoad=setTimeout('startBubbles(0);',200);

//Non-Bubble Scripts:

function showMe (box) {

    var chboxs = document.getElementsByName("c1");
    var vis = "none";
    for(var i=0;i<chboxs.length;i++) { 
        if(chboxs[i].checked){
         vis = "block";
            break;
        }
    }
    document.getElementById(box).style.display = vis;


}