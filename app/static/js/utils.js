function hash(string) {
  const utf8 = new TextEncoder().encode(string);
  return crypto.subtle.digest('SHA-256', utf8).then((hashBuffer) => {
    const hashArray = Array.from(new Uint8Array(hashBuffer));
      return hashArray
        .map((bytes) => bytes.toString(16).padStart(2, '0'))
        .join('');
  });
}

//Adding Plants to index.html
function addPlants() {
  let plantHTML = '';
  for (//p in plants when user=user) {
    let topPlantHTML = '<div id="fill-user-plants"><div class="plant col-md-6 mb-3 text-center"><div class="plant-height d-flex flex-column justify-content-between"><br>';
    let graphHTML = '<div class="row align-items-center"><div class="col-10"><div class="progress" style="height: 40px" role="progressbar" aria-valuenow="';
    let graphWaterHTML2 = '" aria-valuemin="0" aria-valuemax="100"><div class="progress-bar text-bg-primary" style="width: 100%">';
    let graphSunHTML2 = '" aria-valuemin="0" aria-valuemax="100"><div class="progress-bar text-bg-warning" style="width: 100%">';
    75%
    let graphHTML3 = '</div></div></div></div>';

    //iterare through users plant list
    plantHTML = topPlantHTML+ 'name' + '<br>' + 'type' + '<br>' + graphHTML + 
  }
  //Add to HTML
  HTML = document.getElementById("fill-user-plants")
  HTML.innerHTML = plantHTML
}

