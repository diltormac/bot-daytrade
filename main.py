<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Painel do Bot Day Trade</title>
    <style>
        body {
            background-color: #111;
            color: #0f0;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 40px;
        }
        h1 {
            color: #0f0;
        }
        button {
            background-color: #0f0;
            color: #000;
            font-weight: bold;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
            font-size: 16px;
            margin: 10px;
        }
        .log {
            background-color: #222;
            border: 1px solid #444;
            padding: 10px;
            margin-top: 20px;
            width: 100%;
            max-width: 500px;
            margin-left: auto;
            margin-right: auto;
            color: #0f0;
        }
    </style>
</head>
<body>
    <h1>Bot Day Trade - Painel</h1>

    <form method="POST">
        <button type="submit" name="acao" value="iniciar">Iniciar Bot</button>
        <button type="submit" name="acao" value="parar">Parar Bot</button>
    </form>

    <div class="log">
        <h3>Log:</h3>
        {% for item in log_operacoes %}
            <p>{{ item }}</p>
        {% endfor %}
    </div>
</body>
</html>
