
/*--This is the array loop for our images for 30 M--*/
/*------------------------------------*/
const images = new Array(22).fill().map((item,index)=>{
    return `/static/Kathmandu/${2000+index}.PNG`
})
var currentIndex = 0

window.onload = function(){
    document.getElementById('satelliteImage').src = images[currentIndex]
    document.getElementById('previous').addEventListener('click',function(){
      currentIndex = (currentIndex-1)<0?images.length-1: (currentIndex -1)% images.length
            document.getElementById('satelliteImage').src = images[currentIndex]
                document.getElementById('message').innerText = images[currentIndex].replace('/static/','')

    })
    document.getElementById('next').addEventListener('click',function(){
                  currentIndex = (currentIndex +1)% images.length
            document.getElementById('satelliteImage').src = images[currentIndex]
    })
}


/*--This is the array loop for our images for Gautam Buddha airport--*/
/*------------------------------------*/
/*const images = new Array(7).fill().map((item,index)=>{
    return `/static/Gautam/${022016+index}.PNG`
})
var currentIndex = 0

window.onload = function(){
    document.getElementById('gautam').src = images[currentIndex]
    document.getElementById('prev2').addEventListener('click',function(){
      currentIndex = (currentIndex-1)<0?images.length-1: (currentIndex -1)% images.length
            document.getElementById('gautam').src = images[currentIndex]
                document.getElementById('message').innerText = images[currentIndex].replace('/static/','')

    })
    document.getElementById('next2').addEventListener('click',function(){
                  currentIndex = (currentIndex +1)% images.length
            document.getElementById('gautam').src = images[currentIndex]
    })
}*/


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



