<?php

namespace App\Entity;
//importar class do banco de dados
use App\DB\Database;
use PDO;

class Cliente{
    //Definindo os atributos
    // public int $id_cliente;
    public string $nome;
    public string $cpf;
    public string $idade;
    public string $email;
    public string $celular;
    public string $endereco;
    public string $cep;
    public string $cidade;
    public string $estado;

    

    // id_cliente INT NOT NULL AUTO_INCREMENT,
    // nome VARCHAR(100) NOT NULL,
    // cpf VARCHAR(11) NOT NULL,
    // idade INT NOT NULL,
    // email VARCHAR(100) NOT NULL,
    // celular VARCHAR(20) NOT NULL,
    // endereco VARCHAR(100) NOT NULL,
    // cep CHAR(8) NOT NULL,
    // cidade VARCHAR(100) NOT NULL,
    // estado VARCHAR(100) NOT NULL,
    // PRIMARY KEY (id_cliente)
    //Função cadastrar

    public function cadastrar(){
        //Instanciar banco
        $db = new Database('cliente');
        //inserir palestra no banco
        //passando um array chave valor por parametro
        //retornando o id cadastrado
        $db->insert(
                                    [
                                        'nome' => $this->nome,
                                        'cpf' => $this->cpf,
                                        'idade' => $this->idade,
                                        'email' => $this->email,
                                        'celular' => $this->celular,
                                        'endereco' => $this->endereco,
                                        'cep' => $this->cep,
                                        'cidade' => $this->cidade,
                                        'estado' => $this->estado
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