function createVerifyButton(){
    var button = document.createElement('button');
    button.textContent = 'Report';
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
                var postUrl = window.location.href;
                
            
                var username = "Nothing";

                var pageUrl = "http://127.0.0.1/reports/" + postUrl + "+" + username;

                window.location.href = pageUrl;
                window.open(pageUrl);
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
  



  