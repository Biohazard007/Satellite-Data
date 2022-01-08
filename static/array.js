
/*--This is the array loop for our images for 30 M--*/
/*------------------------------------*/

const imagesMapping  = {
   "Kathmandu": {
    total: 22,
    start: 2000
   },
   "Gautam": {
    total: 7,
    start: 22016
   },
   "kalika": {
    total: 4,
    start: 1
   },
   "Hydro":{
   total: 12,
   start: 202101
   },
   "Sanima":{
   total: 8,
   start: 1
   },
    "Royal":{
   total: 58,
   start: 1
   }
}
var currentIndex=0
var currentAddress='Kathmandu'

 function getImages(each='Kathmandu'){
    const images = new Array(imagesMapping[each].total).fill().map((item,index)=>{
        return `/static/${each}/${imagesMapping[each].start+index}.PNG`
    })
    return images;
 }
function updateImages(each = 'Kathmandu'){
    let currentIndex = 0
    // KathmandusatelliteImage



}

window.onload = function(){
    console.log("windows onload")
    document.getElementById('previous').addEventListener('click',function(){
      currentIndex = (currentIndex-1)<0?getImages(currentAddress).length-1: (currentIndex -1)% getImages(currentAddress).length
            document.getElementById('satelliteImage').src = getImages(currentAddress)[currentIndex]

    })
    document.getElementById('next').addEventListener('click',function(){
                  currentIndex = (currentIndex +1)% getImages(currentAddress).length
            document.getElementById('satelliteImage').src = getImages(currentAddress)[currentIndex]
    })
    let array = Object.keys(imagesMapping)
     var ul = document.getElementById('buttonList');

    for(let item of array){
        //updateImages(item)
         let li = document.createElement("li");
         let button = document.createElement('button');
         button.addEventListener('click',function(){
            document.getElementById('satelliteImage').src = getImages(item)[0]
            currentAddress=item
            var x = document.getElementById("popup");
            if (x.style.display === "none") {
              x.style.display = "block";
            } else {
            x.style.display = "none";
            }
         })
         button.appendChild(document.createTextNode(item))
  li.appendChild(button);
    ul.appendChild(li);
//        //document.getElementById('buttonList').innerHtml = `<li><button onclick="myFunction()">${item}</button></li>`
    }
}




/*--This is the array loop for our images for Gautam Buddha airport--*/
/*------------------------------------*/
//const images = new Array(7).fill().map((item,index)=>{
//    return `/static/Gautam/${022016+index}.PNG`
//})
//var currentIndex = 0
//
//window.onload = function(){
//    document.getElementById('gautam').src = images[currentIndex]
//    document.getElementById('prev2').addEventListener('click',function(){
//      currentIndex = (currentIndex-1)<0?images.length-1: (currentIndex -1)% images.length
//            document.getElementById('gautam').src = images[currentIndex]
//                document.getElementById('message').innerText = images[currentIndex].replace('/static/','')
//
//    })
//    document.getElementById('next2').addEventListener('click',function(){
//                  currentIndex = (currentIndex +1)% images.length
//            document.getElementById('gautam').src = images[currentIndex]
//    })
//}


/*--This is the array loop for our images for Kaligandaki dam--*/
/*------------------------------------*/
/*const images = new Array(11).fill().map((item,index)=>{
    return `/static/Hydro/${202101+index}.PNG`
})
var currentIndex = 0

window.onload = function(){
    document.getElementById('kali').src = images[currentIndex]
    document.getElementById('prev3').addEventListener('click',function(){
      currentIndex = (currentIndex-1)<0?images.length-1: (currentIndex -1)% images.length
            document.getElementById('kali').src = images[currentIndex]
                document.getElementById('message').innerText = images[currentIndex].replace('/static/','')

    })
    document.getElementById('next3').addEventListener('click',function(){
                  currentIndex = (currentIndex +1)% images.length
            document.getElementById('kali').src = images[currentIndex]
    })
}*/





/*--This is the array loop for our images for Royal Palace--*/
/*------------------------------------*/





/*--This is for map--*/
/*------------------------------------*/


            var map_38833bccc8c44b61a7f3e48cea0dec7a = L.map(
                "map_38833bccc8c44b61a7f3e48cea0dec7a",
                {
                    center: [27.6557582, 85.3283925],
                    crs: L.CRS.EPSG3857,
                    zoom: 12,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );

            var tile_layer_71042c6ead90408785c2c73fa3f5c0ea = L.tileLayer(
                "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                {"attribution": "Data by \u0026copy; \u003ca href=\"http://openstreetmap.org\"\u003eOpenStreetMap\u003c/a\u003e, under \u003ca href=\"http://www.openstreetmap.org/copyright\"\u003eODbL\u003c/a\u003e.", "detectRetina": false, "maxNativeZoom": 18, "maxZoom": 18, "minZoom": 0, "noWrap": false, "opacity": 1, "subdomains": "abc", "tms": false}
            ).addTo(map_38833bccc8c44b61a7f3e48cea0dec7a);



