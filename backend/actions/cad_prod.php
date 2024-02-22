<?php
include '../vendor/autoload.php';

use App\Entity\Produto;

if(isset($_POST['nome']) && $_POST['desc']){
  $prod = new Produto;
  $prod->nome = $_POST['nome'];
  $prod->descricao = $_POST['desc'];
  $prod->preco = $_POST['preco'];
  $prod->tipo = $_POST['tipo'];

  $result =  $prod->cadastrar();
  if($result){
    $lista=['status'=>'OK'];

  }else{
    $lista=['status'=>'ERROR'];
  }

echo json_encode($lista);
}
