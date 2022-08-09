// Ensure active tab reinstated on page reload
$(function() {
    $('button[data-bs-toggle="tab"]').on('shown.bs.tab', function (e) {
        localStorage.setItem('activeTab', $(e.target).attr('data-bs-target'));
    });

    var activeTab = localStorage.getItem('activeTab');
    if(activeTab){
        $('.nav-tabs button[data-bs-target="' + activeTab + '"]').tab('show');
    }
});

$('.datepicker').datepicker();