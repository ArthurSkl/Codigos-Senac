<div class="container">
    <div class="row">
        <div class="col-12 p-3 text-center"><h1> Cadastro de Produtos </h1></div>
    </div>

  <!-- Modal utilizando a tag DiaLog e buttons -->
<dialog open id="modal" class="oculta">
  <form method="dialog" id="form_modal">
    <section>
      <p> Cadastrado com SUCESSO!!!  </p>
    </section>
    <section>
    <button type="submit">OK</button>
    </section>
  </form>
</dialog>


<form id="forms_cad" method="POST">
        <div class="row">
          <div class="col-md-12 mb-3">
            <label for="nome" class="form-label"> Nome</label>
            <input
              type="text"
              class="form-control"
              id="nome"
              name="nome"
              placeholder="Digite o Produto"
              required
            />
          </div>
        </div>

        <div class="row">
          <div class="col-md-12 mb-3">
            <label for="desc" class="form-label"> Descrição </label>
            <input
              type="text"
              class="form-control"
              id="desc"
              name="desc"
              placeholder="Descrição do Produto"
              required
            />
          </div>
        </div>

        <div class="row">
          <div class="col-md-12 mb-3">
            <label for="preco" class="form-label"> Preço </label>
            <input
              type="number"
              class="form-control"
              id="preco"
              name="preco"
              placeholder="Preço"
              required
            />
          </div>

        </div>

        <div class="row">
          <div class="col-md-12 mb-3">
            <label for="tipo" class="form-label"> Tipo  </label>
            <select class="form-select" name="tipo" id="tipo">
              <option value="NULL" selected disabled>Selecione o Tipo</option>
              <option value="Informática">Informática</option>
              <option value="Eletrônico">Eletrônico</option>
              <option value="Smartphones">Smartphones</option>
              <option value="Videogames">Videogames</option>    
            </select>
          </div>

        </div>

        <div class="row">
          <div class="col-md-12 mb-3 d-flex justify-content-center">
              <button type="reset" id="cancelar" class="btn  btn-danger mx-3">Cancelar</button>
              <button type="submit" id="cadastrar" class="btn btn-primary mx-3">Cadastrar</button>
          </div>
      </div>
      </form>
  
</div>
<script>

let bot =document.getElementById("cancelar");
console.log(bot);

bot.addEventListener('click', function(){
  // alert("cliclou no botao cancelar ")
  console.log("clicou em cancelar")
})

const modal = document.getElementById("modal");

// function Digaoi(){
//   console.log("oi")
// }

function chamaModal(){
  modal.classList.remove("oculta");
  modal.classList.add("chama");
}


const formulario = document.getElementById("forms_cad");
console.log(formulario);



formulario.addEventListener("submit", async function(event) {
      event.preventDefault(); // Evita a submissão do formulário padrão

      const formData = new FormData(formulario);
      //console.log(formData.get('cargo')); testando se pegou algo do input

      //na criação da variável dados_php, envia o form via POST e espera o resultado!!!
        let dados_php = await fetch('./actions/cad_prod.php',{
        method:'POST',
        body: formData
      })

      //recupera o array que veio do PHP
      let resposta = await dados_php.json()
      console.log(resposta)
      console.log(resposta.status)

      if(resposta.status == "OK"){
        // alert("Dados recebidos com sucesso!!")
        chamaModal()
      }else{
        alert("ERRO AO CADASTRAR")
      }
    });

</script>
