<!DOCTYPE html>
<html lang="fa">
<head>
<meta charset="UTF-8">
<title>A.H.K CLUB</title>

<style>
body{
margin:0;
background:#050505;
color:white;
font-family:tahoma;
direction:rtl;
}

header{
text-align:center;
padding:25px;
background:#160022;
}

.logo{
font-size:40px;
color:#b000ff;
}

.search{
text-align:center;
padding:25px;
}

input{
width:70%;
padding:15px;
border-radius:30px;
background:#111;
color:white;
border:2px solid #a000ff;
}

.games{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:20px;
padding:25px;
}

.card{
background:#111;
border-radius:20px;
padding:15px;
box-shadow:0 0 20px #7000ff;
}

button{
background:#a000ff;
color:white;
border:0;
padding:10px;
border-radius:20px;
}

</style>
</head>


<body>

<header>
<div class="logo">🎮 A.H.K CLUB</div>
<p>دانلود بازی</p>
</header>


<div class="search">
<input id="search" placeholder="🔍 سرچ بازی...">
</div>


<div class="games">


<div class="card">
<h2>GTA V</h2>
<p>حجم: 110GB</p>
<button>دانلود</button>
</div>


<div class="card">
<h2>Red Dead 2</h2>
<p>حجم: 120GB</p>
<button>دانلود</button>
</div>


<div class="card">
<h2>Cyberpunk 2077</h2>
<p>حجم: 70GB</p>
<button>دانلود</button>
</div>


</div>


<script>

let search = document.getElementById("search");
let games = document.querySelectorAll(".card");

search.onkeyup=function(){

let text=search.value.toLowerCase();

games.forEach(game=>{

if(game.innerText.toLowerCase().includes(text)){
game.style.display="block";
}else{
game.style.display="none";
}

});

}

</script>


</body>
</html>