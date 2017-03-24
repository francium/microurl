(function () {
  'use strict';
  var displayLoader = document.getElementById('display-loader');
  var displayMicro = document.getElementById('display-micro');
  var makeMicroSubmit = document.getElementById('make-micro-submit');

  makeMicroSubmit.addEventListener('click', function(event) {
    event.preventDefault();

    clearMicroResponse();
    toggleLoader(displayLoader);

    var makeMicroForm = document.getElementById('make-micro-form');
    var microFormData = new FormData(makeMicroForm);
    var request = new Request('/generate_micro', {
                                method: 'POST',
                                body: microFormData
    });

    fetch(request)
      .then(function(response) {
        return response.text();
      }).then(function(text) {
        toggleLoader(displayLoader);
        showMicroResponse(text);
    });
  });


  function toggleLoader(node) {
    node.classList.toggle('hidden');
  }

  function clearMicroResponse(text) {
    removeChildrenAddSingleChild(displayMicro, null);
  }

  function showMicroResponse(text) {
      var link = document.createElement('A');
      link.href = '/' + text;
      link.text = text;
    removeChildrenAddSingleChild(displayMicro, link);
  }

  function removeChildrenAddSingleChild(parent, newChild) {
    while(parent.hasChildNodes())
      parent.removeChild(parent.lastChild);

    if (newChild != null)
      parent.appendChild(newChild);
  }
})();

