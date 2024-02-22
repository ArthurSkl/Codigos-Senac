<?php

namespace App\Entity;
//importar class do banco de dados
use App\DB\Database;
use PDO;

class Produto{
    //Definindo os atributos
    public int $id_prod;
    public string $nome;
    public string $descricao;
    public string $preco;
    public string $tipo;
    //Função cadastrar

    public function cadastrar(){
        //Instanciar banco
        $db = new Database('produto');
        //inserir palestra no banco
        //passando um array chave valor por parametro
        //retornando o id cadastrado
        $db->insert(
                                    [
                                        'nome' => $this->nome,
                                        'descricao' => $this->descricao,
                                        'preco' => $this->preco,
                                        'tipo' => $this->tipo
                                    ]
                                    );

        //retornar sucesso
        return true;
    }

    public static function buscar($where = null,$order = null, $limit = null){
        //Já faz o FetchALL da classe
        return (new Database('produto'))
        ->select($where,$order,$limit)
        ->fetchAll(PDO::FETCH_CLASS,self::class);
    }

}

?>