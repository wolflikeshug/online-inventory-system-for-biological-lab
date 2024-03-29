// Nav related code reference: https://www.cssscript.com/dashboard-sidebar-menu-template/
// Shrink button for sidebar
const shrink_btn = document.querySelector(".shrink-btn");
// Quick search button - not displayed
const search = document.querySelector(".search");
// Links on the sidebar
const sidebar_links = document.querySelectorAll(".sidebar-links a");
// Tooltips for sidebar links
const tooltip_elements = document.querySelectorAll(".tooltip-element");
// Samples card
const cards = document.querySelectorAll(".info-card");
// People card
const people_card = document.querySelectorAll(".people-card");
// Button for editing users
const edit_user = document.querySelectorAll("#edit_user");
// Button for editing freezers
const edit_freezer = document.querySelectorAll("#edit_freezer");
// Button for editing rooms
const edit_room = document.querySelectorAll("#edit_room");
// Button for editing buildings
const edit_building = document.querySelectorAll("#edit_building");
// Button for editing shelves
const edit_shelf = document.querySelectorAll("#edit_shelf");
// Button for editing boxes
const edit_box = document.querySelectorAll("#edit_box");

// Input forms border colour change on focus & blur, reference: https://jsfiddle.net/bootstrapious/3j4a0Lps
$(function () {
  $('input:not(.form-control.is-invalid), select:not(.form-control.is-invalid)').on('focus', function () {
      $(this).parent().find('.input-group-text').css('border-color', '#00a94f');
  });
  $('input:not(.form-control.is-invalid), select:not(.form-control.is-invalid)').on('blur', function () {
      $(this).parent().find('.input-group-text').css('border-color', '#ced4da');
  });
});

// If form is invalid, make the whole field have red border
$(function () {
  $('.form-control.is-invalid').parent().find('.input-group-text').css('border-color', '#dc3545');
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

// Listener for quick search
search.addEventListener("click", () => {
  document.body.classList.remove("shrink");
  search.lastElementChild.focus();
});

// When someone clicks on a person, make that card selected
people_card.forEach(peep => {
  peep.addEventListener("click", () => {
    people_card.forEach(peep => peep.classList.remove("selected-card"));
    if(!document.body.classList.contains("shrink")){
      shrinkNav();
    }
    peep.classList.add("selected-card");
    openInfo();
  })
})

// When someone clicks on a sample, make that card selected
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

  // If a card has more than three sample ids in it (child count of more than 5), then include an indicator on the card,
  // don't show more than 3
  if(card.children[0].childElementCount > 5){
    card.children[0].children[1].classList.add("show-mark")
    let i = 0
    for(i; i < card.children[0].childElementCount - 5; i++){
      card.children[0].children[5+i].classList.add("hidden")
    }
  }
});

// Function that opens another sidebar but with info relating to selected card
function openInfo(){
  if(document.getElementById("box-info").classList.contains("hidden")){
    document.getElementById("box-info").classList.remove("hidden");
  }
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

// Function that shows modals
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