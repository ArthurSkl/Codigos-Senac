<?php
include '../vendor/autoload.php';

use App\Entity\Cliente;



if(isset($_POST['nome']) && $_POST['cpf']){
  $cliente = new Cliente;
  $cliente->nome = $_POST['nome'];
  $cliente->cpf = $_POST['cpf'];
  $cliente->idade = $_POST['idade'];
  $cliente->email = $_POST['email'];
  $cliente->celular = $_POST['celular'];
  $cliente->endereco = $_POST['endereco'];
  $cliente->cep = $_POST['cep'];
  $cliente->cidade = $_POST['cidade'];
  $cliente->estado = $_POST['estado'];

  $result =  $cliente->cadastrar();
  if($result){
    $lista=['status'=>'OK'];

  }else{
    $lista=['status'=>'ERROR'];
  }

echo json_encode($lista);
}
