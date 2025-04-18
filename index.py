<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>YouTube Sentiment Analysis</title>
<style>
body {
font-family: 'Arial', sans-serif;
margin: 0;
padding: 0;
background-color: #f2f2f2;
}

header {
background-color: #333;
color: white;
padding: 1em;
text-align: center;
}

nav {
background-color: #444;
overflow: hidden;
}

nav a {
float: left;
display: block;
color: white;
text-align: center;
padding: 14px 16px;
text-decoration: none;
}

nav a:hover {
background-color: #ddd;
color: black;
}

form {
max-width: 400px;
margin: 20px auto;
background-color: white;

padding: 20px;
border-radius: 8px;
box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
label {
display: block;
font-weight: bold;
margin-bottom: 8px;
}
input {
width: 100%;
padding: 10px;
margin-bottom: 16px;
box-sizing: border-box;
}
button {
background-color: #007bff;
color: white;
padding: 10px 20px;
border: none;
border-radius: 4px;
cursor: pointer;
}
button:hover {
background-color: #0056b3;
}
footer {
background-color: #333;
color: white;
text-align: center;

padding: 1em;
position: fixed;
bottom: 0;
width: 100%;
}
</style>
</head>
<body>
<header>
<h1>YouTube Sentiment Analysis</h1>
</header>

<nav>
<a href="#">Home</a>
<a href="#">About</a>
<a href="#">Contact</a>
</nav>

<form action="/analyze" method="post">
<label for="video_url">Enter YouTube Video URL:</label>
<input type="text" name="video_url" id="video_url" required>
<button type="submit">Analyze</button>
</form>

<footer>
&copy; 2024 YouTube Sentiment Analysis
</footer>
</body>
</html>
