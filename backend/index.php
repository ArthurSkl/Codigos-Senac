<?php
include __DIR__.'/vendor/autoload.php';

use \App\Entity\Produto;   

$new_obj = new Produto();
$prod = $new_obj->buscar();

include __DIR__.'/includes/header.php';
include __DIR__.'/includes/menu_user.php';

echo "<pre>"; print_r($prod); echo "</pre>";

include __DIR__.'/includes/footer.php';

?>
