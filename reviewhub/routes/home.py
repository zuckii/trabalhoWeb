from flask import Blueprint, render_template, redirect, url_for, session

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def homepage():
    # redirect to login if not authenticated or in guest mode
    if not session.get('user_id') and not session.get('guest_mode'):
        return redirect(url_for('auth.login'))
    
    # Mock movies data - Real poster URLs
    # Mock movies data - replace with database query later
    movies = [
    {'id': 1, 'genre': 'Ficção', 'title': 'A Origem', 'poster': 'https://image.tmdb.org/t/p/w500/9gk7adHYeDvHkCSEqAvQNLV5Uge.jpg'},
    {'id': 2, 'genre': 'Ação', 'title': 'Batman: O Cavaleiro das Trevas', 'poster': 'https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg'},
    {'id': 3, 'genre': 'Crime', 'title': 'Seven: Os Sete Crimes', 'poster': 'https://image.tmdb.org/t/p/w500/6yoghtyTpznpBik8EngEmJskVUO.jpg'},
    {'id': 4, 'genre': 'Ficção', 'title': 'Matrix', 'poster': 'https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg'},
    {'id': 5, 'genre': 'Suspense', 'title': 'Parasita', 'poster': 'https://image.tmdb.org/t/p/w500/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg'},
    {'id': 6, 'genre': 'Crime', 'title': 'Pulp Fiction: Tempo de Violência', 'poster': 'https://image.tmdb.org/t/p/w500/d5iIlFn5s0ImszYzBPb8JPIfbXD.jpg'},
    {'id': 7, 'genre': 'Ação', 'title': 'Gladiador', 'poster': 'https://image.tmdb.org/t/p/w500/ty8TGRuvJLPUmAR1H1nRIsgwvim.jpg'},
    {'id': 8, 'genre': 'Ficção', 'title': 'Avatar', 'poster': 'https://image.tmdb.org/t/p/w500/kyeqWdyUXW608qlYkRqosgbbJyK.jpg'},
    {'id': 9, 'genre': 'Crime', 'title': 'O Poderoso Chefão', 'poster': 'https://image.tmdb.org/t/p/w500/3bhkrj58Vtu7enYsRolD1fZdja1.jpg'},
    {'id': 10, 'genre': 'Drama', 'title': 'Clube da Luta', 'poster': 'https://image.tmdb.org/t/p/w500/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg'},
    {'id': 11, 'genre': 'Drama', 'title': 'Forrest Gump: O Contador de Histórias', 'poster': 'https://image.tmdb.org/t/p/w500/arw2vcBveWOVZr6pxd9XTd1TdQa.jpg'},
    {'id': 12, 'genre': 'Drama', 'title': 'Um Sonho de Liberdade', 'poster': 'https://image.tmdb.org/t/p/w500/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg'},
    {'id': 13, 'genre': 'Crime', 'title': 'Coringa', 'poster': 'https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg'},
    {'id': 14, 'genre': 'Ação', 'title': 'Vingadores: Ultimato', 'poster': 'https://image.tmdb.org/t/p/w500/or06FN3Dka5tukK1e9sl16pB3iy.jpg'},
    {'id': 15, 'genre': 'Animação', 'title': 'Homem-Aranha: Através do Aranhaverso', 'poster': 'https://image.tmdb.org/t/p/w500/8Vt6mWEReuy4Of61Lnj5Xj704m8.jpg'},
    {'id': 16, 'genre': 'Biografia', 'title': 'Oppenheimer', 'poster': 'https://image.tmdb.org/t/p/w500/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg'},
    {'id': 17, 'genre': 'Ficção', 'title': 'Duna: Parte 2', 'poster': 'https://image.tmdb.org/t/p/w500/1pdfLvkbY9ohJlCjQH2CZjjYVvJ.jpg'},
    {'id': 18, 'genre': 'Fantasia', 'title': 'O Senhor dos Anéis: O Retorno do Rei', 'poster': 'https://image.tmdb.org/t/p/w500/rCzpDGLbOoPwLjy3OAm5NUPOTrC.jpg'},
    {'id': 19, 'genre': 'Romance', 'title': 'Titanic', 'poster': 'https://image.tmdb.org/t/p/w500/9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg'},
    {'id': 20, 'genre': 'Ficção', 'title': 'De Volta para o Futuro', 'poster': 'https://image.tmdb.org/t/p/w500/fNOH9f1aA7XRTzl1sAOx9iF553Q.jpg'},
    {'id': 21, 'genre': 'Animação', 'title': 'O Rei Leão', 'poster': 'https://image.tmdb.org/t/p/w500/sKCr78MXSLixwmZ8DyJLrpMsd15.jpg'},
    {'id': 22, 'genre': 'Animação', 'title': 'Toy Story', 'poster': 'https://image.tmdb.org/t/p/w500/uXDfjJbdP4ijW5hWSBrPrlKpxab.jpg'},
    {'id': 23, 'genre': 'Animação', 'title': 'Up: Altas Aventuras', 'poster': 'https://image.tmdb.org/t/p/w500/vpbaStTMt8qqXaEgnOR2EE4DNJk.jpg'},
    {'id': 24, 'genre': 'Ficção', 'title': 'Interestelar', 'poster': 'https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg'},
    {'id': 25, 'genre': 'Ação', 'title': 'Homem de Ferro', 'poster': 'https://image.tmdb.org/t/p/w500/78lPtwv72eTNqFW9COBYI0dWDJa.jpg'},
    {'id': 26, 'genre': 'Ação', 'title': 'Pantera Negra', 'poster': 'https://image.tmdb.org/t/p/w500/uxzzxijgPIY7slzFvMotPv8wjKA.jpg'},
    {'id': 27, 'genre': 'Ficção', 'title': 'Guardiões da Galáxia', 'poster': 'https://image.tmdb.org/t/p/w500/r7vmZjiyZw9rpJMQJdXpjgiCOk9.jpg'},
    {'id': 28, 'genre': 'Ação', 'title': 'Thor: Ragnarok', 'poster': 'https://image.tmdb.org/t/p/w500/rzRwTcFvttcN1ZpX2xv4j3tSdJu.jpg'},
    {'id': 29, 'genre': 'Fantasia', 'title': 'Doutor Estranho', 'poster': 'https://image.tmdb.org/t/p/w500/uGBVj3bEbCoZbDjjl9wTxcygko1.jpg'},
    {'id': 30, 'genre': 'Ação', 'title': 'Deadpool', 'poster': 'https://image.tmdb.org/t/p/w500/fSRb7vyIP8rQpL0I47P3qUsEKX3.jpg'},
    {'id': 31, 'genre': 'Crime', 'title': 'Batman', 'poster': 'https://image.tmdb.org/t/p/w500/74xTEgt7R36Fpooo50r9T25onhq.jpg'},
    {'id': 32, 'genre': 'Ação', 'title': 'Top Gun: Maverick', 'poster': 'https://image.tmdb.org/t/p/w500/62HCnUTziyWcpDaBO2i1DX17ljH.jpg'},
    {'id': 33, 'genre': 'Ação', 'title': 'Mad Max: Estrada da Fúria', 'poster': 'https://image.tmdb.org/t/p/w500/8tZYtuWezp8JbcsvHYO0O46tFbo.jpg'},
    {'id': 34, 'genre': 'Fantasia', 'title': 'Harry Potter e a Pedra Filosofal', 'poster': 'https://image.tmdb.org/t/p/w500/wuMc08IPKEatf9rnMNXvIDxqP4W.jpg'},
    {'id': 35, 'genre': 'Terror', 'title': 'Alien: O 8º Passageiro', 'poster': 'https://image.tmdb.org/t/p/w500/vfrQk5IPloGg1v9Rzbh2Eg3VGyM.jpg'},
    {'id': 36, 'genre': 'Ficção', 'title': 'Blade Runner 2049', 'poster': 'https://image.tmdb.org/t/p/w500/gajva2L0rPYkEWjzgFlBXCAVBE5.jpg'},
    {'id': 37, 'genre': 'Mistério', 'title': 'Garota Exemplar', 'poster': 'https://image.tmdb.org/t/p/w500/qymaJhucquUwjpb8oiqynMeXnID.jpg'},
    {'id': 38, 'genre': 'Comédia', 'title': 'Space Jam: O Jogo do Século', 'poster': 'https://image.tmdb.org/t/p/w500/5bFK5d3mVTAvBCXi5NPWH0tYjKl.jpg'},
    {'id': 39, 'genre': 'Guerra', 'title': 'Bastardos Inglórios', 'poster': 'https://image.tmdb.org/t/p/w500/7sfbEnaARXDDhKm0CZ7D7uc2sbo.jpg'}
]
    
    return render_template("home/index.html", movies=movies)

