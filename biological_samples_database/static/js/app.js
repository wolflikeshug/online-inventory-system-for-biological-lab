// Nav related code reference: https://www.cssscript.com/dashboard-sidebar-menu-template/
const shrink_btn = document.querySelector(".shrink-btn");
const search = document.querySelector(".search");
const sidebar_links = document.querySelectorAll(".sidebar-links a");
const active_tab = document.querySelector(".active-tab");
const shortcuts = document.querySelector(".sidebar-links h4");
const tooltip_elements = document.querySelectorAll(".tooltip-element");
const cards = document.querySelectorAll(".info-card");
const nopropagation = document.querySelectorAll(".noprop");
const edit_user = document.querySelectorAll("#edit_user");
const edit_freezer = document.querySelectorAll("#edit_freezer");
const edit_room = document.querySelectorAll("#edit_room");
const edit_building = document.querySelectorAll("#edit_building");
const edit_shelf = document.querySelectorAll("#edit_shelf");
const edit_box = document.querySelectorAll("#edit_box");

let activeIndex;

// Input forms, reference: https://jsfiddle.net/bootstrapious/3j4a0Lps
$(function () {
  $('input, select').on('focus', function () {
      $(this).parent().find('.input-group-text').css('border-color', '#00a94f');
  });
  $('input, select').on('blur', function () {
      $(this).parent().find('.input-group-text').css('border-color', '#ced4da');
  });
});

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

// Stop card event from playing if clicking on element (with id noprop) inside it
nopropagation.forEach(noprop => {
  noprop.addEventListener("click", (e) =>{
  e.stopPropagation();
  })
});

// When someone clicks on a box
cards.forEach(card => {
  card.addEventListener("click", () => {
    cards.forEach(card => card.classList.remove("selected-card"));
    if(!document.body.classList.contains("shrink")){
      shrinkNav();
    }
    card.classList.add("selected-card");
    openInfo();
  })
  if(card.children[0].childElementCount == 1){
    card.classList.add("no-sample")
  }
});

function openInfo(){
  if(document.getElementById("box-info").classList.contains("hidden")){
    document.getElementById("box-info").classList.remove("hidden");
  }
}

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

function modal_display(id, get_location) {
  try {
    $.ajax({
      url: get_location,
      type: 'GET',
      dataType: 'html',
      data: {
        'id': id
      },
      beforeSend: function (data) {
        $('#modal-response').on('shown.bs.modal', function () {
          $('#primary-tab-index').trigger('focus');
        })
        $("#modal-response").modal({ backdrop: true, keyboard: true, focus: false }, "show");

      },
      success: function (data) {
        $("#modal-response .modal-content").html(data);
      }
    });
  }
  catch (ex) {
    alert(ex);
  }
};

/*Create Shelf Modal*/
$(function () {
  $('#create_shelf').click(function () {
    modal_display(null, "/shelf/create/"+this.value);
  });
});

/*Edit Shelf Modal*/
edit_shelf.forEach(edit => {
  edit.addEventListener("click", () =>{
    var sid = $(edit).data("id");
    modal_display(null, "/shelf/edit/"+sid);
  })
});

/*Create Box Modal*/
$(function () {
  $('#create_box').click(function () {
    modal_display(null, "/box/create/"+this.value);
  });
});

/*Edit Box Modal*/
edit_box.forEach(edit => {
  edit.addEventListener("click", () =>{
    var bid = $(edit).data("id");
    modal_display(null, "/box/edit/"+bid);
  })
});

/*Create Freezer Modal*/
$(function () {
  $('#create_freezer').click(function () {
    modal_display(null, "/freezer/create/"+this.value);
  });
});

/*Edit Freezer Modal*/
edit_freezer.forEach(edit => {
  edit.addEventListener("click", () =>{
    var fid = $(edit).data("id");
    modal_display(null, "/freezer/edit/"+fid);
  })
});

/*Create Room Modal*/
$(function () {
  $('#create_room').click(function () {
    modal_display(null, "/room/create/"+this.value);
  });
});

/*Edit Room Modal*/
edit_room.forEach(edit => {
  edit.addEventListener("click", () =>{
    var rid = $(edit).data("id");
    modal_display(null, "/room/edit/"+rid);
  })
});

/*Create Building Modal*/
$(function () {
  $('#create_building').click(function () {
    modal_display(null, "/building/create");
  });
});

/*Edit Room Modal*/
edit_building.forEach(edit => {
  edit.addEventListener("click", () =>{
    var bid = $(edit).data("id");
    modal_display(null, "/building/edit/"+bid);
  })
});

/*Create Sample Modal*/
$(function () {
  $('div').on("click", "#create_sample_box_cell", function () {
    let bid = $('#create_sample_box_cell').attr('data-box_id');
    let pos = $('#create_sample_box_cell').attr('data-pos');
    modal_display(null, "/samples/" + this.value + "/create/"+bid+"/"+pos);
  });
});

$(function () {
  $('div').on("click", ".edit_sample_box_cell", function () {
    modal_display(null, "/samples/" + this.value + "/edit/"+this.id);
  });
});

$(function () {
  $('div').on("click", ".copy_sample_box_cell", function () {
    modal_display(null, "/samples/" + this.value + "/copy/"+this.id);
  });
});

$(function () {
  $('#create_sample').click(function () {
    modal_display(null, "/samples/"+this.value+"/create/");
  });
});

/*Edit Sample Modal*/
$(function () {
  $('.edit_sample').click(function () {        
    modal_display(null, "/samples/" + this.value + "/edit/" + this.id);
  });
});

/*Delete Sample*/
$(function () {
  $('.delete_sample').click(function () {   
    $.get("/samples/" +this.value +'/delete/' + this.id);
    location.reload();
  });
});

/*Data Overview*/
$(function () {
  $('#overview').click(function () {
    modal_display(null, "/overview");
  });
});

/*Example Page*/
$(function () {
  $('#example').click(function () {
    modal_display(null, "/example");
  });
});

/*Edit User Modal*/
edit_user.forEach(edit => {
  edit.addEventListener("click", () =>{
    var uid = $(edit).data("id");
    modal_display(null, "/users/people/edit/"+uid);
  })
});

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










// UNSUSED CODE THAT MAY BE USED IF CURRENT IDEAS GO BAD
/*
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
    case "Login":
      changeLink("login-side")
      break;
    case "Register":
      changeLink("register-side")
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
}*/