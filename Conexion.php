<?php

    require_once("infoBDD.php");

    class ConexionBDD extends DataConexion
    {
        var $con = "";
        var $consulta="";

        private function Conect()
        {
            $this->conn = mysqli_connect($this->DBHost, $this->DBUser, $this->DBPass, $this->DB)
            if ($this-conn)
            {
                echo "Entro"
            }
        }


    }

    $db = new ConexionBDD;

?>