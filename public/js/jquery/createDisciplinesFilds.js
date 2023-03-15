function createFilds(){
    numberFilds = document.getElementById('disciplines').value

    if(numberFilds){
        numberFilds = parseInt(numberFilds)

        //alert(numberFilds)

        var div = document.createElement("div")

        for(i = 0; i < numberFilds.length; i++){  
            var div2 = document.createElement("div")
            div2.innerHTML = `
            <hr>
                <div class="form-row">
                    <div class="input-group col-md-2">
                        <div class="input-group-prepend">
                          <div class="input-group-text">ID</div>
                        </div>
                        <input type="text" class="form-control" name="grade" id="moodleID" placeholder="ID no Moodle">
                    </div>
      
                      <div class="input-group col-md-8">
                        <div class="input-group-prepend">
                          <div class="input-group-text">DISCIPLINA</div>
                        </div>
                        <input type="text" name="grade" class="form-control discipline" placeholder="Nome Sala no Moodle">
                      </div>
      
                      <div class="input-group col-md-2">
                        <div class="input-group-prepend">
                          <div class="input-group-text">C.H</div>
                        </div>
                        <input type="text" name="grade" class="form-control discipline" placeholder="C. Horária Disciplina">
                      </div>
                </div>
              `
            div.appendChild(div2);  
        }  
        document.getElementById('discGrade').appendChild(div)
    }
}