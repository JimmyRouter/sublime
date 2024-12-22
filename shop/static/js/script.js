const anchors = document.querySelectorAll('a[href*="#"]')

for (let anchor of anchors){
    anchor.addEventListener("click", function(event){
        event.preventDefault();
        const blockID = anchor.getAttribute('href')
        document.querySelector('' + blockID).scrollIntoView({
            behavior: "smooth",
            block: "start"
        })
    })
}

let scrollbackBtn = document.getElementById("scrollback");
let scrollElem = document.getElementById("scrollelem");
scrollElem.onscroll = () => {scrollFunction()};

function scrollFunction() {
  if (scrollElem.scrollTop > 20) {
  console.log('scrollElem>>>>>',scrollElem.scrollTop)
    scrollbackBtn.style.display = "block";
  } else {
    scrollbackBtn.style.display = "none";
  }
}

function topFunction() {
  scrollElem.scrollTo({
    top:0,
    behavior:'smooth',
  });
}
