/**
 * workflow JS
 */

if (pycms == undefined) {
  var pycms = {};
}

pycms['workflow'] = {};

/**
 * Transition to other state
 */
pycms.workflow.trans = function(to) {
  
  $.get("./trans?to=" + to, function(data) {
      $("#wf_action").replaceWith(data);
    });
}


