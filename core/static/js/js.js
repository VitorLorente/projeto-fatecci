var menu = document.querySelectorAll('li')[0];
var toggle = [];
var ativo = true;

var ligaDesliga = document.querySelectorAll('.navbar li');

menu.addEventListener('click', function(){
	console.log('Teste');
	if(ativo == true){
		for(var i = 0; i < ligaDesliga.length; i++){
			ligaDesliga[i].style.display = 'block';
			ativo = false;
		}
	}else{
		for(var i = 0; i < ligaDesliga.length; i++){
			ligaDesliga[i].style.display = 'none';
		}
		ligaDesliga[0].style.display = 'block';
		ativo = true;
	}
});

document.getElementById("login").onsubmit=function(event){
	var raCampo = document.getElementById("ra");
	var senhaCampo = document.getElementById("senha");
	if(raCampo.value == "") {
	    alert("Campo obrigatório não preenchido");
	    return false;
	}
	if(senhaCampo.value == "") {
	    alert("Campo obrigatório não preenchido");
	    return false;
	}

};

document.getElementById("cadastro").onsubmit=function(event){
	var nomeCampo = document.getElementById("nome");
	var sexoCampo = document.getElementById("sexo");
	var emailCampo = document.getElementById("email");
	
	var telCampo = document.getElementById("telefone");
	var nascCampo = document.getElementById("nasc");
	var raCampo = document.getElementById("ra");
	var cursoCampo = document.getElementById("curso");
	var estadoCampo = document.getElementById("estado");
	var cidadeCampo = document.getElementById("cidade");
	var bairroCampo = document.getElementById("bairro");
	var enderecoCampo = document.getElementById("endereco");
	var numeroCampo = document.getElementById("numero");
	
	if(nomeCampo.value == "") {
	    alert("Campo obrigatório não preenchido");
	    return false;
	}
	if (sexoCampo.value == "Selecione"){
		alert("Campo obrigatório não preenchido");
	    return false;

	}
	if (emailCampo.value == ""){
		alert("Campo obrigatório não preenchido");
	    return false;

	}
	if(telCampo.value == "") {
	    alert("Campo obrigatório não preenchido");
	    return false;
	}
	if(nascCampo.value == "") {
	    alert("Campo obrigatório não preenchido");
	    return false;
	}
	
	if(raCampo.value == "") {
	    alert("Campo obrigatório não preenchido");
	    return false;
	}


	if(cursoCampo.value == "Selecione") {
	    alert("Campo obrigatório não preenchido");
	    return false;
	}

	if(estadoCampo.value == "Selecione") {
	    alert("Campo obrigatório não preenchido");
	    return false;
	}

	if(cidadeCampo.value == "") {
	    alert("Campo obrigatório não preenchido");
	    return false;
	}

	if(bairroCampo.value == "") {
	    alert("Campo obrigatório não preenchido");
	    return false;
	}

	if(enderecoCampo.value == "") {
	    alert("Campo obrigatório não preenchido");
	    return false;
	}
	
	if(numeroCampo.value == "") {
	    alert("Campo obrigatório não preenchido");
	    return false;
	}

};
