// function Pessoa(props){
//     return (
//         <div>
//             <img src={props.foto} alt={props.nome}></img>
//             <h2>Nome: {props.nome}</h2>
//             <p>Idade: {props.idade}</p>
//             <p>Profissao: {props.profissao}</p>
//         </div>
//     )

// }

//ou sem props 

function Pessoa(nome,foto,idade,profissao){
    return (
        <div>
            <img src={foto} alt={nome}></img>
            <h2>Nome: {nome}</h2>
            <p>Idade: {idade}</p>
            <p>Profissao: {profissao}</p>
        </div>
    )

}
export default Pessoa