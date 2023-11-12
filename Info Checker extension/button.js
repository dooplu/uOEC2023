function createVerifyButton(){
    var button = document.createElement('button');
    button.textContent = 'Verify Information';
    button.style.position = 'fixed';
    button.style.left = '10px';
    button.style.bottom = '10px';
    button.style.zIndex = '1000';

    return button;
  }
  
 // function only works if save button exists
  function addButton(){

    var buttonExists = document.querySelector('#verify-button');

    if (document.querySelector('[aria-label="Save"]')){
        if (!buttonExists) {
            var verifyButton = createVerifyButton();
            verifyButton.id = 'verify-button';
            document.body.appendChild(verifyButton);
            
            verifyButton.addEventListener('click', function(){
                var currentPageUrl = window.location.href;
                alert(currentPageUrl);
            });
        }
    }

    else {
      if (buttonExists) {
        buttonExists.remove();
      }
    }
  }
  

  var observer = new MutationObserver(function(mutations){
    mutations.forEach(function(mutation){
      addButton();
    });
  });

  observer.observe(document.body, {subtree: true, childList: true, attributes: true});
  

  addButton();
  



  