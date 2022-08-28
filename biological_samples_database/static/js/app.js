// Nav related code reference: https://www.cssscript.com/dashboard-sidebar-menu-template/
const shrink_btn = document.querySelector(".shrink-btn");
const search = document.querySelector(".search");
const sidebar_links = document.querySelectorAll(".sidebar-links a");
const active_tab = document.querySelector(".active-tab");
const shortcuts = document.querySelector(".sidebar-links h4");
const tooltip_elements = document.querySelectorAll(".tooltip-element");

let activeIndex;

// Functions/listeners for shrinking sidetab
shrink_btn.addEventListener("click", () => {
  shrinkNav();
});

function shrinkNav(){
  document.body.classList.toggle("shrink");

  shrink_btn.classList.add("hovered");

  setTimeout(() => {
    shrink_btn.classList.remove("hovered");
  }, 500);
}

search.addEventListener("click", () => {
  document.body.classList.remove("shrink");
  search.lastElementChild.focus();
});

// Changing the active sidebar tab
function changeLink(sidetab) {
  sidebar_links.forEach((sideLink) => sideLink.classList.remove("active"));
  document.getElementById(sidetab).classList.add("active");

  activeIndex = document.getElementById(sidetab).dataset.active;

}

// Function to show tooltip for sidebar tabs
function showTooltip() {
  let tooltip = this.parentNode.lastElementChild;
  let spans = tooltip.children;
  let tooltipIndex = this.dataset.tooltip;

  Array.from(spans).forEach((sp) => sp.classList.remove("show"));
  spans[tooltipIndex].classList.add("show");

  tooltip.style.top = `${(100 / (spans.length * 2)) * (tooltipIndex * 2 + 1)}%`;
}

// When mouse hovers of sidebar tab, show tooltip
tooltip_elements.forEach((elem) => {
  elem.addEventListener("mouseover", showTooltip);
});

// When page loads, set appropriate side-tab to be active - highlighted icon, green box
window.onload=function(){
  switch(document.title){
    case "Dashboard":
      changeLink("dashboard-side")
      break;
    case "Inventory":
      changeLink("inventory-side")
      break;
    case "People":
      changeLink("people-side")
      break;
    case "Rooms":
      changeLink("rooms-side")
      //roomBoxes()
      break;
    case "Freezers":
      changeLink("freezers-side")
      break;
    case "Samples":
      changeLink("samples-side")
      break;
  }
}

// Function to build a box with a given box id (containing info), inside a given row.
function buildBox(row_id, box_id, title, info){
  // Create box
  let card = document.createElement("div")
  let card_body = document.createElement("div")
  let card_title = document.createElement("h5")
  let card_text = document.createElement("p")
  let card_button = document.createElement("a")
  card.classList.add("card")
  card_body.classList.add("card-body")
  card_title.classList.add("card-title")
  card_text.classList.add("card-text")
  card_button.classList.add("btn")
  card_button.classList.add("btn-primary")
  card.setAttribute("id", box_id)
  card_title.innerText = title
  card_text.innerText = info
  card_button.innerText = "Enter"
  card_button.setAttribute("href", "#")
  
  card_body.appendChild(card_title)
  card_body.appendChild(card_text)
  card_body.appendChild(card_button)
  card.appendChild(card_body)
  document.getElementById(row_id).appendChild(card)
  // debug
  console.log("appended", box_id)
}

function buildEmptyBox(row_id, box_id){
  let current_box = document.createElement("div")
  current_box.classList.add("card")
  current_box.setAttribute("id", box_id)
  document.getElementById(row_id).appendChild(current_box)
  // debug
  console.log("appended", box_id)
}

// Function to build a row with a given row id, inside a given container (or div).
function buildRow(row_id, container){
  let current_row = document.createElement("div")
  current_row.classList.add("card-deck")
  current_row.setAttribute("id", row_id)
  container.appendChild(current_row)
  // debug
  console.log("appended", row_id)
}


// Building rooms page

function roomBoxes(){
  // The part of the screen that will contain the boxes for room page
  const rooms_boxes = document.getElementById("rooms-container");
  // Should be query to database to get the number of rooms but will make it as 5 more now. AJAX?
  let nrooms = 5;
  // Count to keep track of how many more boxes to add
  let nrooms_left = nrooms;
  // Number of rows to be added to page (each row fits 3 room boxes)
  let nrooms_rows = Math.ceil(nrooms/3);
  // Count number of boxes added
  let box_index = 0;

  // Loop to produce all required boxes
  for(let i = 0; i < nrooms_rows; i++){
    let current_row_id = "row".concat(i.toString())
    buildRow(current_row_id, rooms_boxes)
    for(let j = 0; j < 3; j++){
      // WILL NEED TO DECIDE HOW TO IMPLEMENT DATABASE INFO INTO BOXES: currently set to just "Info"

      // Build three columns: if there's no more columns/rooms to build, fill row with remainder
      // empty columns (for aesthetics)
      if(nrooms_left != 0){
        let current_box_id = "box".concat(box_index.toString())
        // GET INFO FROM DATABASE
        let room_name = "Room"
        let room_info = "Info"
        buildBox(current_row_id, current_box_id, room_name, room_info)
        box_index++
        nrooms_left--
      }
      else{
        let current_box_id = "box-empty"
        buildEmptyBox(current_row_id, current_box_id)
      }
    }
    let gap = document.createElement("br")
    rooms_boxes.appendChild(gap)
  }
}

async function testPost(){
    fetch('http://localhost:5000/samples/cell_line/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
    },    
    }).then(response => {
      if(response.status == 200){
          return response.json();
      } else {
          ;
      }
  }).then(json => {
      ;
  }).catch(error => {
      console.log('error with access token req!')
  })
}