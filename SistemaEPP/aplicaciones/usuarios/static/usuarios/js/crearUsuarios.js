
function openModal() {

    console.log("Probando aqui...");
    document.querySelector('#idUser').value = "";
    document.querySelector('#titleModal').innerHTML = 'Nuevo Usuario';
    document.querySelector('.modal-header').classList.replace('updateRegister','headerRegister');
    document.querySelector('#btnActionForm').classList.replace('btn-info','btn-primary');
    document.querySelector('#btnText').innerHTML = 'Guardar';
    document.querySelector('#formUser').reset();
    $('#modalFormUser').modal('show');
}
