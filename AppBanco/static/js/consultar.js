function consultar(){

    fetch("http://127.0.0.1:8000/cliente",{
        method:"GET",
        headers:{
            "consultar-Type":"AppBanco/json"
        }

    })

    .then(response => response.json())
    .then(datos=>{
        console.log(datos)
        var tabla=document.getElementById("consultaclientes");
        tabla.innerHTML="";
        if(datos==0){
            tabla.innerHTML+=`<tr> <td>no hay datos</td> </tr>`       
        }
        else{
            for(let dat of datos){
                tabla.innerHTML+=`
                <tr> 
                    <td>${dat.Documento}</td>
                    <td>${dat.Nombre}</td>
                    <td>${dat.Apellido}</td>
                    <td>${dat.Correo}</td>
                    <td>${dat.Celular}</td>
                </tr>`
            }
        }
    })
    

}