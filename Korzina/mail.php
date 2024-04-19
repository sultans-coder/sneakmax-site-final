<?php
$serverName = "DESKTOP-OEEO6R9"; // Имя вашего сервера SQL Server
$connectionOptions = array(
    "Database" => "sneakmaxbd", // Имя вашей базы данных
    "IntegratedSecurity" => true // Использовать Windows Authentication
);

// Подключение к серверу SQL Server
$conn = sqlsrv_connect($serverName, $connectionOptions);

// Проверка подключения
if (!$conn) {
    die("Ошибка подключения: " . print_r(sqlsrv_errors(), true));
}

// Получение данных из формы
$name = $_POST['name'];
$email = $_POST['email'];
$message = $_POST['message'];

// SQL-запрос для вставки данных
$sql = "INSERT INTO orders (name, email, message) VALUES (?, ?, ?)";
$params = array($name, $email, $message);
$stmt = sqlsrv_prepare($conn, $sql, $params);

if (sqlsrv_execute($stmt)) {
    echo "Данные успешно сохранены в базе данных";
} else {
    echo "Ошибка: " . print_r(sqlsrv_errors(), true);
}

sqlsrv_close($conn);
