import logo from './logo.svg';
import './App.css';
import HelloWorld from './components/HellowWorld';
import SayMyName from './components/SayMyName';
import Pessoa from './components/Pessoa';

function App() {
  const nome = "Nome aleatorio"

  function sum(a,b){
    return a+b
  }

  const url = 'https://via.placeholder.com/150'
  return (
    <div className="App">
      <h1>Ola, React!</h1>
      <p>Meu primeiro app em React</p>
      <p>Olá {nome}</p>
      <p>Soma: {sum(5,9)}</p>
      <img src={url} alt="minha imagem"/> 
      <HelloWorld></HelloWorld>
      <SayMyName nome="Arthur"/>
      <SayMyName nome="JÃO"/>
      <SayMyName nome={nome}/>
      <Pessoa nome="Arthur Frantz" idade="23" profissao="Programador Front-end" foto="https://via.placeholder.com/150"/>
      
    </div>
  );
}

export default App;
