<?php
/**
 * Autor: @Thiago Almeida
 */

namespace App\DB;
use PDO;
use PDOException;

class Database{

    private $conn;
    private string $local="localhost";
    private string $db="sysadmin";
    private string $user = "root";
    private string $password = "";
    private $table;

    public function __construct($table = null){
        $this->table = $table;
        $this->conecta();
    }

    private function conecta(){
        try {
            $this->conn = new PDO("mysql:host=".$this->local.";dbname=$this->db",$this->user,$this->password); 
            $this->conn->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);

            //echo "Conectado com Sucesso!!";
        } catch (PDOException $err) {
            //retirar msg em produção
            die("Connection Failed " . $err->getMessage());
        }
    }

    public function execute($query,$binds = []){
        //BINDS = parametros
        try{
            $stmt = $this->conn->prepare($query);
            $stmt->execute($binds);
            return $stmt;

        }catch (PDOException $err) {
            //retirar msg em produção
            die("Connection Failed " . $err->getMessage());
        }

    }

    public function insert($values){
        //DEBUG
        //echo "<pre>";print_r($values);echo "</pre>";
        //Dados query $fields=campos $binds=parametros
        $fields = array_keys($values);
        //$data = array_values($values); TESTE DE RECEBIMENTO
        $binds = array_pad([],count($fields),'?');

        //Montar query
        $query = 'INSERT INTO ' . $this->table .'  (' .implode(',',$fields). ') VALUES (' .implode(',',$binds).')';
        //DEBUG para saber se está montando a query corretamente
        // print_r($query);
        // print_r(array_values($values));
        
        //Método para executar a Query
        $this->execute($query,array_values($values));
    }

    public function select($where = null,$order = null,$limit = null,$fields = '*'){
        $where = strlen($where) ? 'WHERE '.$where : '';
        $order = strlen($order) ? 'ORDER BY '.$order : '';
        $limit = strlen($limit) ? 'LIMIT '.$limit : '';

        //Método para montar a consulta/query
        $query ='SELECT '.$fields.' FROM ' .$this->table .' '.$where.' '.$order.' '.$limit;
        
        //Método para executar a consulta/query
        return $this->execute($query);
    }

    public function update($where,$values){
        $fields = array_keys($values);
        //Método para montar a consulta/query
        $query = 'UPDATE ' . $this->table .' SET '.implode('=?,',$fields). '=? WHERE '. $where;
        //Método para executar o update
        $this->execute($query,array_values($values));

        return true;
    }

    public function delete($where){
        //montar a query
        $query = 'DELETE FROM '.$this->table.' WHERE '.$where;

        $this->execute($query);
        return true;
    }

}

?>
