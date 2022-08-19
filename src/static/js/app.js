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
      roomBoxes()
      break;
    case "Freezers":
      changeLink("freezers-side")
      break;
    case "Samples":
      changeLink("samples-side")
      break;
  }
}

// Building selectable boxes in pages
// Row and columns for box set-up
const row = document.createElement("div")
row.classList.add("row")
const column = document.createElement("div")
column.classList.add("col")

// Rooms page

function roomBoxes(){
  // The part of the screen that will contain the boxes for room page
  const rooms_boxes = document.getElementById("rooms-container")
  // Should be query to database to get the number of rooms but will make it as 5 more now. AJAX?
  let nrooms = 5;
  // Count to keep track of how many more boxes to add
  let nrooms_left = nrooms;
  // Number of rows to be added to page (each row fits 3 room boxes)
  let nrooms_rows = Math.ceil(nrooms/3);

  // Loop to produce all required boxes
  for(let i = 0; i < nrooms_rows; i++){
    let current_row_id = "row".concat(i.toString())
    let current_row = row
    current_row.setAttribute("id", current_row_id)
    rooms_boxes.appendChild(current_row)
    for(let j = 0; j < 3; j++){
      // WILL NEED TO DECIDE HOW TO IMPLEMENT DATABASE INFO INTO BOXES
      let current_col_id = "col".concat(j.toString())
      let current_col = column
      current_col.setAttribute("id", current_col_id)
      current_col.innerHTML = "Room"
      document.getElementById(current_row_id).appendChild(current_col)
      nrooms_left--
      if(nrooms_left == 0){
        break
      }
    }
  }
}