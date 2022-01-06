
/*--This is the array loop for our images--*/
/*------------------------------------*/
const images = new Array(22).fill().map((item,index)=>{
    return `/static/${2000+index}.PNG`
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

/*--This is the array loop for our leaflet--*/
/*------------------------------------*/

