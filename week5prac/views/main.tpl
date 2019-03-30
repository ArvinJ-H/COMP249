<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
<title>Unit</title>
</head>
<body>
<nav>
    <a href="/">Home</a>
</nav>
<main>
    <form method="POST">
        <legend>Your Likes</legend>
        <ul>
            <li>What do you like<input name= 'name'></li>
            <li>what unit<input name= 'unit'></li>
        </ul>
        <input type="submit">
    </form>
    <ul>
    % for item in units:
    <li>{{item}}</li>
    %end
    </ul>
</main>
</body>
</html>