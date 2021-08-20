const createForm = () => {
  // get alpha high value form form
  const alpha_high = document.getElementById('alpha-high').value

  // remove initial form content
  var initFormContent = document.getElementById("formInitialContent")
  initFormContent.parentNode.removeChild(initFormContent);

  var theForm = document.getElementById('form');
  var br = document.createElement("br"); 

  const para = document.createElement("p");
  const node = document.createTextNode("Input the values of alpha and the corresponding beta values");
  para.appendChild(node);
  theForm.appendChild(para);

  var hiddenInput = document.createElement("input");
  hiddenInput.setAttribute("hidden", "true");
  hiddenInput.setAttribute("name", "alpha-total");
  hiddenInput.setAttribute("type", "number");
  hiddenInput.setAttribute("value", alpha_high);

  theForm.appendChild(hiddenInput);

  for (let i = 0; i < parseInt(alpha_high) + 1 ; i++) {
    var alphaInput = document.createElement("input");
    alphaInput.setAttribute("type", "text");
    alphaInput.setAttribute("name", `alpha-${i}` );
    alphaInput.setAttribute("placeholder", `alpha-${i}` );

    theForm.appendChild(alphaInput);

    var betaInput = document.createElement("input");
    betaInput.setAttribute("type", "text");
    betaInput.setAttribute("name", `beta-${i}` );
    betaInput.setAttribute("placeholder", `beta-${i}` );

    theForm.appendChild(betaInput);
    theForm.appendChild(br.cloneNode()); 
  }

  var submitButton = document.createElement("input");
  submitButton.setAttribute("type", "submit");
  submitButton.setAttribute("value", "Submit");
  theForm.appendChild(submitButton); 

}