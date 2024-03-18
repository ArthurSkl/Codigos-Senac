import logo from './logo.svg';
import './App.css';

function App() {
  const nome = "Arthur"

  function sum(a,b){
    return a+b
  }

  const url = 'https://via.placeholder.com/150'
  return (
    <div className="App">
      <h1>Ola React!</h1>
      <p>Meu primeiro app em React</p>
      <p>Olá, {nome}</p>
      <p>Soma: {sum(5,9)}</p>
      <img src={url} alt="minha imagem"/> 
    </div>
  );
}

export default App;
