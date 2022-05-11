var btn = '';

const info = `
    <div class="main">
    <form class="container">
        <div class="row row-1">
            <label class="form-control" for="nome"> Primeiro Nome
                <input type="text" name="nome">
                <i class="icon"><img src="/static/img/icons/user.svg" alt=""></i>
            </label>

            <label class="form-control" for="sobrenome"> Sobrenome
                <input type="text" name="sobrenome">
                <i class="icon"><img src="/static/img/icons/user.svg" alt=""></i>
            </label>
        </div>

        <div class="row row-2">
            <label class="form-control" for="email"> E-mail
                <input type="email" name="email">
                <i class="icon"><img src="/static/img/icons/email.svg" alt=""></i>
            </label>

            <label class="form-control" for="telefone"> Telefone de Contato
                <input type="number" name="telefone">
                <i class="icon"><img src="/static/img/icons/cel.svg" alt=""></i>
            </label>
        </div>
        <div class="row row-3">
            <label class="form-control" for="cpf"> CPF
                <input type="number" name="cpf">
                <i class="icon"><img src="/static/img/icons/cpf.svg" alt=""></i>
            </label>

            <label class="form-control" for="nascimento"> Data de Nascimento
                <input type="number" name="nascimento">
                <i class="icon"><img src="/static/img/icons/calendario.png" alt=""></i>
            </label>
        </div>

        <div class="row row-4">
            <div class="btn">
                <button href="#">Atualizar</button>
            </div>
        </div>
        </form>
        </div>`;

const endereco = `<section class="enderecos">
        <div class="container">

            <div class="card-add">
                <a href="/adicionarEndereco">
                    <img src="/static/img/icons/plus.svg" alt="">
                    <p>Adicionar endereço</p>
                </a>
            </div>
            <div class="card-endereco">
                <div class="head-endereco">
                    <h3>Endereço:</h3>
                    
                    <a href="#"><img src="/static/img/icons/bin.svg" alt=""></a>
                </div>
                <div class="separador"></div>
                <div class="content">
                    <p>Rua da Paz, 54</p>
                    <p>Bairro da Felicidade - Salvador/BA</p>
                    <p>CEP: 12345-678</p>
                </div>

                <a class="card-editar" href="#">Editar endereço</a>
            </div>
        </div>
        </section>`

const envio = `<h1> Envio </h1>`

let pages = 'infos';
var main = document.querySelector(".app");

if(pages === 'infos'){
        
    main.innerHTML = info;
}
else{
    main.innerHTML = endereco;
}

function btnColor(page){

    if(btn != ''){
        btn.classList.remove("btn-selected");
        btn.classList.add("btn-def");
    }
    
    if(page === 'infos'){
        
        btn = document.querySelector('.btn-info');
        
    }
    if(page === 'ender'){

        btn = document.querySelector('.btn-endereco');
    } 
    if(page === 'envi'){
        
        btn = document.querySelector('.btn-envio');
    }

    console.log(btn.textContent)
    btn.classList.remove("btn-def");
    btn.classList.add("btn-selected");

}
function toggle(page){
    pages = page;

    if(pages === 'infos'){
        
        main.innerHTML = info;
    }
    if(pages === 'ender'){
        main.innerHTML = endereco;
    } 
    if(pages === 'envi'){
        main.innerHTML = envio;
    }

    btnColor(page);
}


btnColor('infos');