document.addEventListener("DOMContentLoaded",function(){
    document.getElementById("frminsertar").addEventListener("submit",function(event) {
        event.preventDefault();
        var Datos={
            Documento:document.getElementById("Documento").value,
            Nombre:document.getElementById("Nombre").value,
            Apellido:document.getElementById("Apellido").value,
            Correo:document.getElementById("Correo").value,
            Celular:document.getElementById("Celular").value
        };
        console.log(document.getElementById("Documento").value)

        var JsonData=JSON.stringify(Datos);
        console.log(JsonData)
        fetch("http://127.0.0.1:8000/insertar/",{
            method:"POST",
            body:JsonData,
            headers:{
                "Content-Type":"AppBanco/json"
            }

        })

        .then(response => response.json())
        .then(datoos=>{
            console.log(datoos)
            consultar();
        })
        .catch(console.error())

    })


})