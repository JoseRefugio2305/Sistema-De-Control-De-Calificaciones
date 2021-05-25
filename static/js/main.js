const btnDelete= document.querySelectorAll('.btn-delete');//Selecciona todos los botones que tengan la clase btn-delete
if(btnDelete) {
  const btnArray = Array.from(btnDelete);
  btnArray.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      if(!confirm('¿Estas seguro de querer borrar el grupo?')){
        e.preventDefault();
      }
    });
  })
}


