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

// When someone clicks on a box, make that card selected
cards.forEach(card => {
  card.addEventListener("click", () => {
    cards.forEach(card => card.classList.remove("selected-card"));
    if(!document.body.classList.contains("shrink")){
      shrinkNav();
    }
    card.classList.add("selected-card");
    openInfo();
  })

  // If a card doesnt have a sample id in it (child count of less than 3), then it is empty. 
  if(card.children[0].childElementCount < 3){
    card.classList.add("no-sample")
  }

  // If a card has more than one sample id in it (child count of more than 3), then include an indicator on the card
  if(card.children[0].childElementCount > 3){
    card.children[0].children[1].classList.add("show-mark")
  }

  // If a card has more than three sample ids in it (child count of more than 5), then include an indicator on the card
  if(card.children[0].childElementCount > 5){
    let i = 0
    for(i; i < card.children[0].childElementCount - 5; i++){
      card.children[0].children[5+i].classList.add("hidden")
    }
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
  $('td').on("click", ".delete_sample", function () {

    if (confirm("This will permanently delete the sample '" + this.name + "' from the database.\n Are you sure you wish to proceed ?")){
      $.get("/samples/" +this.value +'/delete/' + this.id);
      location.reload();
    }
    else{
      //Do Nothing
    }
  });
});

/*Remove Sample*/
$(function () {
  $('td').on("click", ".remove_sample", function () {
    
      $.get("/samples/remove/" + this.id);
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