var menu = document.querySelectorAll('li')[0];
var toggle = [];
var ativo = true;
var titulo = document.title.toUpperCase();
var ligaDesliga = document.querySelectorAll('.navbar li');

if (titulo == "ALUNO - FATECCI" || titulo == "PROFESSOR - FATECCI" || titulo == "BOLETIM - FATECCI"){
	document.getElementsByTagName('img')[1].style.display = 'none';
	document.getElementsByTagName('img')[2].style.display = 'none';
}

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