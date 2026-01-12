from django.shortcuts import render
from django.http import HttpResponse

def toko_home(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>🛍️ Al-Chips - Toko Keripik Terpercaya</title>
        <style>
            body { 
                font-family: 'Segoe UI', Arial; 
                margin: 0; 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }
            .header { 
                background: rgba(0,0,0,0.3); 
                padding: 20px; 
                text-align: center; 
                border-bottom: 3px solid #ffd700;
            }
            .container { 
                max-width: 1200px; 
                margin: 0 auto; 
                padding: 30px; 
            }
            .products { 
                display: grid; 
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); 
                gap: 20px; 
                margin-top: 30px; 
            }
            .product { 
                background: rgba(255,255,255,0.1); 
                padding: 20px; 
                border-radius: 15px; 
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255,255,255,0.2);
                transition: transform 0.3s;
            }
            .product:hover { 
                transform: translateY(-5px); 
                background: rgba(255,255,255,0.2);
            }
            .price { 
                font-size: 1.5em; 
                color: #ffd700; 
                font-weight: bold; 
            }
            .btn { 
                background: #ff6b6b; 
                color: white; 
                padding: 10px 20px; 
                border: none; 
                border-radius: 25px; 
                cursor: pointer; 
                text-decoration: none;
                display: inline-block;
                margin-top: 10px;
            }
            .btn:hover { 
                background: #ff5252; 
            }
            .nav { 
                text-align: center; 
                margin: 20px 0; 
            }
            .nav a { 
                color: #ffd700; 
                text-decoration: none; 
                margin: 0 15px; 
                font-weight: bold;
                background: rgba(0,0,0,0.3);
                padding: 10px 20px;
                border-radius: 20px;
            }
            .nav a:hover { 
                background: rgba(0,0,0,0.5); 
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🛍️ AL-CHIPS</h1>
            <p>Toko Keripik Terpercaya & Berkualitas</p>
        </div>
        
        <div class="nav">
            <a href="/">🏠 Home</a>
            <a href="/shop/products/">📦 Produk</a>
            <a href="/shop/cart/">🛒 Keranjang</a>
            <a href="/shop/about/">ℹ️ Tentang</a>
        </div>
        
        <div class="container">
            <h2>🔥 PRODUK UNGGULAN</h2>
            
            <div class="products">
                <div class="product">
                    <h3>🥔 Al-Chips Potatoes</h3>
                    <p>Keripik kentang renyah dengan rasa gurih dan tekstur yang sempurna.</p>
                    <div class="price">Rp 25.000</div>
                    <a href="/shop/product/1/" class="btn">Lihat Detail</a>
                </div>
                
                <div class="product">
                    <h3>🍠 Al-Chips Cassava</h3>
                    <p>Keripik singkong premium dengan cita rasa autentik dan kriuknya tahan lama.</p>
                    <div class="price">Rp 20.000</div>
                    <a href="/shop/product/2/" class="btn">Lihat Detail</a>
                </div>
                
                <div class="product">
                    <h3>🍠 Al-Chips Sweet Potatoes</h3>
                    <p>Keripik ubi jalar manis dengan rasa unik dan nutrisi tinggi.</p>
                    <div class="price">Rp 30.000</div>
                    <a href="/shop/product/3/" class="btn">Lihat Detail</a>
                </div>
                
                <div class="product">
                    <h3>🍖 Al-Chips Meatball</h3>
                    <p>Keripik bakso dengan cita rasa pedas dan gurih yang menggugah selera.</p>
                    <div class="price">Rp 35.000</div>
                    <a href="/shop/product/4/" class="btn">Lihat Detail</a>
                </div>
                        
                 <div class="product">
                    <h3>🍖 Al-Chips Tempe</h3>
                    <p>Keripik tempe dengan cita rasa khas dan tekstur renyah yang menggoda.</p>
                    <div class="price">Rp 25.000</div>
                    <a href="/shop/product/5/" class="btn">Lihat Detail</a>
                </div>
                        
            </div>
            
            <div style="text-align: center; margin-top: 40px; padding: 30px; background: rgba(0,0,0,0.3); border-radius: 15px;">
                <h3>🎯 KENAPA PILIH AL-CHIPS?</h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin-top: 20px;">
                    <div>✅ 100% Alami</div>
                    <div>🚚 Gratis Ongkir</div>
                    <div>💯 Tanpa Pengawet</div>
                    <div>🌶️ Berbagai Varian Rasa</div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """)

def products(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>📦 Semua Produk - Al-Chips</title>
        <style>
            body { 
                font-family: 'Segoe UI', Arial; 
                margin: 0; 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }
            .header { 
                background: rgba(0,0,0,0.3); 
                padding: 20px; 
                text-align: center; 
                border-bottom: 3px solid #ffd700;
            }
            .container { 
                max-width: 1200px; 
                margin: 0 auto; 
                padding: 30px; 
            }
            .products { 
                display: grid; 
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); 
                gap: 25px; 
                margin-top: 30px; 
            }
            .product { 
                background: rgba(255,255,255,0.1); 
                padding: 25px; 
                border-radius: 15px; 
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255,255,255,0.2);
                transition: transform 0.3s;
                text-align: center;
            }
            .product:hover { 
                transform: translateY(-5px); 
                background: rgba(255,255,255,0.2);
            }
            .product h3 {
                margin-bottom: 10px;
                color: #ffd700;
            }
            .price { 
                font-size: 1.5em; 
                color: #ffd700; 
                font-weight: bold;
                margin: 15px 0;
            }
            .btn { 
                background: #ff6b6b; 
                color: white; 
                padding: 12px 25px; 
                border: none; 
                border-radius: 25px; 
                cursor: pointer; 
                text-decoration: none;
                display: inline-block;
                margin-top: 15px;
                font-weight: bold;
                transition: background 0.3s;
            }
            .btn:hover { 
                background: #ff5252; 
            }
            .nav { 
                text-align: center; 
                margin: 20px 0; 
            }
            .nav a { 
                color: #ffd700; 
                text-decoration: none; 
                margin: 0 15px; 
                font-weight: bold;
                background: rgba(0,0,0,0.3);
                padding: 10px 20px;
                border-radius: 20px;
            }
            .nav a:hover { 
                background: rgba(0,0,0,0.5); 
            }
            .filter-bar {
                background: rgba(0,0,0,0.2);
                padding: 20px;
                border-radius: 15px;
                margin-bottom: 30px;
                text-align: center;
            }
            .filter-bar h2 {
                margin-bottom: 15px;
                color: #ffd700;
            }
            .filter-btn {
                background: rgba(255,255,255,0.1);
                color: white;
                border: 1px solid rgba(255,255,255,0.3);
                padding: 8px 16px;
                border-radius: 20px;
                margin: 0 5px;
                cursor: pointer;
                transition: all 0.3s;
            }
            .filter-btn:hover, .filter-btn.active {
                background: #ff6b6b;
                border-color: #ff6b6b;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>�️ AL-CHIPS</h1>
            <p>Toko Keripik Terpercaya & Berkualitas</p>
        </div>
        
        <div class="nav">
            <a href="/">🏠 Home</a>
            <a href="/shop/products/" style="background: rgba(0,0,0,0.5);">📦 Produk</a>
            <a href="/shop/cart/">🛒 Keranjang</a>
            <a href="/shop/about/">ℹ️ Tentang</a>
        </div>
        
        <div class="container">
            <div class="filter-bar">
                <h2>🔍 Filter Produk</h2>
                <button class="filter-btn active">Semua</button>
                <button class="filter-btn">Kentang</button>
                <button class="filter-btn">Singkong</button>
                <button class="filter-btn">Protein</button>
                <button class="filter-btn">Terbaru</button>
            </div>
            
            <div class="products">
                <div class="product">
                    <h3>🥔 Al-Chips Potatoes</h3>
                    <p>Keripik kentang renyah dengan rasa gurih dan tekstur yang sempurna. Dibuat dari kentang pilihan tanpa pengawet.</p>
                    <div class="price">Rp 25.000</div>
                    <a href="/shop/product/1/" class="btn">Lihat Detail</a>
                </div>
                
                <div class="product">
                    <h3>🍠 Al-Chips Cassava</h3>
                    <p>Keripik singkong premium dengan cita rasa autentik dan kriuknya tahan lama. Klasik yang tak pernah bosan.</p>
                    <div class="price">Rp 20.000</div>
                    <a href="/shop/product/2/" class="btn">Lihat Detail</a>
                </div>
                
                <div class="product">
                    <h3>🍠 Al-Chips Sweet Potatoes</h3>
                    <p>Keripik ubi jalar manis dengan rasa unik dan nutrisi tinggi. Alternatif sehat untuk camilan Anda.</p>
                    <div class="price">Rp 30.000</div>
                    <a href="/shop/product/3/" class="btn">Lihat Detail</a>
                </div>
                
                <div class="product">
                    <h3>🍖 Al-Chips Meatball</h3>
                    <p>Keripik bakso dengan cita rasa pedas gurih yang menggugah selera. Inovasi terbaru dari Al-Chips.</p>
                    <div class="price">Rp 35.000</div>
                    <a href="/shop/product/4/" class="btn">Lihat Detail</a>
                </div>
                        
                <div class="product">
                    <h3>🍖 Al-Chips Tempe</h3>
                    <p>Keripik tempe dengan cita rasa khas dan tekstur renyah yang menggoda. Camilan sehat dari bahan lokal.</p>
                    <div class="price">Rp 25.000</div>
                    <a href="/shop/product/5/" class="btn">Lihat Detail</a>
                </div>
                        
                <div class="product">
                    <h3>🌶️ Al-Chips Spicy Mix</h3>
                    <p>Campuran berbagai keripik dengan level pedas yang bervariasi. Untuk pecinta pedas sejati.</p>
                    <div class="price">Rp 40.000</div>
                    <a href="/shop/product/6/" class="btn">Lihat Detail</a>
                </div>

                <div class="product">
                    <h3>🧀 Al-Chips Cheese</h3>
                    <p>Keripik dengan taburan keju premium yang meleleh di mulut. Gurihnya tak tertandingi.</p>
                    <div class="price">Rp 32.000</div>
                    <a href="/shop/product/7/" class="btn">Lihat Detail</a>
                </div>

                <div class="product">
                    <h3>🍫 Al-Chips Chocolate</h3>
                    <p>Keripik dengan lapisan coklat premium. Manisnya yang pas untuk menemani waktu santai.</p>
                    <div class="price">Rp 28.000</div>
                    <a href="/shop/product/8/" class="btn">Lihat Detail</a>
                </div>
            </div>
        </div>
    </body>
    </html>
    """)

def product_detail(request, product_id):
    products = {
        1: {"name": "🥔 Al-Chips Potatoes", "price": "Rp 25.000", "desc": "Keripik kentang renyah dengan rasa gurih alami, tanpa pengawet. Dibuat dari kentang pilihan berkualitas tinggi."},
        2: {"name": "🍠 Al-Chips Cassava", "price": "Rp 20.000", "desc": "Keripik singkong premium dengan tekstur kriuk dan rasa autentik. Klasik yang tak pernah bosan."},
        3: {"name": "🍠 Al-Chips Sweet Potatoes", "price": "Rp 30.000", "desc": "Keripik ubi jalar manis dengan nutrisi tinggi dan rasa unik. Alternatif sehat untuk camilan Anda."},
        4: {"name": "🍖 Al-Chips Meatball", "price": "Rp 35.000", "desc": "Keripik bakso dengan cita rasa pedas gurih yang menggugah selera. Inovasi terbaru dari Al-Chips."},
        5: {"name": "🍖 Al-Chips Tempe", "price": "Rp 25.000", "desc": "Keripik tempe dengan cita rasa khas dan tekstur renyah yang menggoda. Camilan sehat dari bahan lokal."},
        6: {"name": "🌶️ Al-Chips Spicy Mix", "price": "Rp 40.000", "desc": "Campuran berbagai keripik dengan level pedas yang bervariasi. Untuk pecinta pedas sejati."},
        7: {"name": "🧀 Al-Chips Cheese", "price": "Rp 32.000", "desc": "Keripik dengan taburan keju premium yang meleleh di mulut. Gurihnya tak tertandingi."},
        8: {"name": "🍫 Al-Chips Chocolate", "price": "Rp 28.000", "desc": "Keripik dengan lapisan coklat premium. Manisnya yang pas untuk menemani waktu santai."},
    }
    
    product = products.get(product_id, {"name": "Produk tidak ditemukan", "price": "Rp 0", "desc": "Maaf, produk tidak tersedia"})
    
    return HttpResponse(f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{product['name']} - Al-Chips</title>
        <style>
            body {{ 
                font-family: 'Segoe UI', Arial; 
                margin: 0; 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }}
            .nav {{
                text-align: center; 
                margin: 20px 0; 
            }}
            .nav a {{ 
                color: #ffd700; 
                text-decoration: none; 
                margin: 0 15px; 
                font-weight: bold;
                background: rgba(0,0,0,0.3);
                padding: 10px 20px;
                border-radius: 20px;
            }}
            .nav a:hover {{ 
                background: rgba(0,0,0,0.5); 
            }}
            .container {{
                max-width: 800px;
                margin: 0 auto;
                padding: 30px;
            }}
            .product-detail {{
                background: rgba(255,255,255,0.1);
                padding: 40px;
                border-radius: 20px;
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255,255,255,0.2);
                text-align: center;
            }}
            .product-name {{
                font-size: 2.5rem;
                color: #ffd700;
                margin-bottom: 20px;
            }}
            .product-price {{
                font-size: 2rem;
                color: #ff6b6b;
                font-weight: bold;
                margin: 20px 0;
            }}
            .product-desc {{
                font-size: 1.1rem;
                line-height: 1.6;
                margin: 30px 0;
                opacity: 0.9;
            }}
            .btn {{
                background: #ff6b6b; 
                color: white; 
                padding: 15px 30px; 
                border: none; 
                border-radius: 25px; 
                cursor: pointer; 
                text-decoration: none;
                display: inline-block;
                margin: 10px;
                font-weight: bold;
                font-size: 1.1rem;
                transition: background 0.3s;
            }}
            .btn:hover {{ 
                background: #ff5252; 
            }}
            .btn-secondary {{
                background: rgba(255,255,255,0.2);
                border: 1px solid rgba(255,255,255,0.3);
            }}
            .btn-secondary:hover {{
                background: rgba(255,255,255,0.3);
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🛍️ AL-CHIPS</h1>
            <p>Toko Keripik Terpercaya & Berkualitas</p>
        </div>
        
        <div class="nav">
            <a href="/">🏠 Home</a>
            <a href="/shop/products/">📦 Produk</a>
            <a href="/shop/cart/">🛒 Keranjang</a>
            <a href="/shop/about/">ℹ️ Tentang</a>
        </div>
        
        <div class="container">
            <div class="product-detail">
                <h1 class="product-name">{product['name']}</h1>
                <div class="product-price">{product['price']}</div>
                <p class="product-desc">{product['desc']}</p>
                <button class="btn">🛒 Tambah ke Keranjang</button>
                <a href="/shop/products/" class="btn btn-secondary">← Kembali ke Produk</a>
            </div>
        </div>
    </body>
    </html>
    """)

def cart(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>🛒 Keranjang Belanja - Al-Chips</title>
        <style>
            body { 
                font-family: 'Segoe UI', Arial; 
                margin: 0; 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }
            .header { 
                background: rgba(0,0,0,0.3); 
                padding: 20px; 
                text-align: center; 
                border-bottom: 3px solid #ffd700;
            }
            .nav { 
                text-align: center; 
                margin: 20px 0; 
            }
            .nav a { 
                color: #ffd700; 
                text-decoration: none; 
                margin: 0 15px; 
                font-weight: bold;
                background: rgba(0,0,0,0.3);
                padding: 10px 20px;
                border-radius: 20px;
            }
            .nav a:hover { 
                background: rgba(0,0,0,0.5); 
            }
            .container {
                max-width: 900px;
                margin: 0 auto;
                padding: 30px;
            }
            .cart-empty {
                background: rgba(255,255,255,0.1);
                padding: 60px 40px;
                border-radius: 20px;
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255,255,255,0.2);
                text-align: center;
            }
            .cart-empty h1 {
                color: #ffd700;
                margin-bottom: 20px;
                font-size: 2.5rem;
            }
            .cart-empty p {
                font-size: 1.2rem;
                margin-bottom: 30px;
                opacity: 0.9;
            }
            .btn {
                background: #ff6b6b; 
                color: white; 
                padding: 15px 30px; 
                border: none; 
                border-radius: 25px; 
                cursor: pointer; 
                text-decoration: none;
                display: inline-block;
                margin: 10px;
                font-weight: bold;
                font-size: 1.1rem;
                transition: background 0.3s;
            }
            .btn:hover { 
                background: #ff5252; 
            }
            .btn-secondary {
                background: rgba(255,255,255,0.2);
                border: 1px solid rgba(255,255,255,0.3);
            }
            .btn-secondary:hover {
                background: rgba(255,255,255,0.3);
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🛍️ AL-CHIPS</h1>
            <p>Toko Keripik Terpercaya & Berkualitas</p>
        </div>
        
        <div class="nav">
            <a href="/">🏠 Home</a>
            <a href="/shop/products/">📦 Produk</a>
            <a href="/shop/cart/">🛒 Keranjang</a>
            <a href="/shop/about/">ℹ️ Tentang</a>
        </div>
        
        <div class="container">
            <div class="cart-empty">
                <h1>🛒 Keranjang Belanja</h1>
                <p>Keranjang Anda masih kosong. Yuk mulai berbelanja!</p>
                <a href="/shop/products/" class="btn">🛍️ Mulai Belanja</a>
                <a href="/shop/" class="btn btn-secondary">← Kembali ke Toko</a>
            </div>
        </div>
                        
        
    </body>
    </html>
    """)

def shop_about(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>ℹ️ Tentang Al-Chips</title>
        <style>
            body { 
                font-family: 'Segoe UI', Arial; 
                margin: 0; 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }
            .header { 
                background: rgba(0,0,0,0.3); 
                padding: 20px; 
                text-align: center; 
                border-bottom: 3px solid #ffd700;
            }
            .nav { 
                text-align: center; 
                margin: 20px 0; 
            }
            .nav a { 
                color: #ffd700; 
                text-decoration: none; 
                margin: 0 15px; 
                font-weight: bold;
                background: rgba(0,0,0,0.3);
                padding: 10px 20px;
                border-radius: 20px;
            }
            .nav a:hover { 
                background: rgba(0,0,0,0.5); 
            }
            .container {
                max-width: 900px;
                margin: 0 auto;
                padding: 30px;
            }
            .about-content {
                background: rgba(255,255,255,0.1);
                padding: 40px;
                border-radius: 20px;
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255,255,255,0.2);
                text-align: center;
            }
            .about-content h1 {
                color: #ffd700;
                margin-bottom: 30px;
                font-size: 2.5rem;
            }
            .about-content p {
                font-size: 1.1rem;
                line-height: 1.6;
                margin-bottom: 30px;
                opacity: 0.9;
            }
            .features {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                margin-top: 40px;
            }
            .feature {
                background: rgba(0,0,0,0.2);
                padding: 25px;
                border-radius: 15px;
                border: 1px solid rgba(255,255,255,0.1);
            }
            .feature h3 {
                color: #ff6b6b;
                margin-bottom: 15px;
            }
            .btn {
                background: #ff6b6b; 
                color: white; 
                padding: 15px 30px; 
                border: none; 
                border-radius: 25px; 
                cursor: pointer; 
                text-decoration: none;
                display: inline-block;
                margin: 20px 10px 0;
                font-weight: bold;
                font-size: 1.1rem;
                transition: background 0.3s;
            }
            .btn:hover { 
                background: #ff5252; 
            }
            .btn-secondary {
                background: rgba(255,255,255,0.2);
                border: 1px solid rgba(255,255,255,0.3);
            }
            .btn-secondary:hover {
                background: rgba(255,255,255,0.3);
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🛍️ AL-CHIPS</h1>
            <p>Toko Keripik Terpercaya & Berkualitas</p>
        </div>
        
        <div class="nav">
            <a href="/">🏠 Home</a>
            <a href="/shop/products/">📦 Produk</a>
            <a href="/shop/cart/">🛒 Keranjang</a>
            <a href="/shop/about/">ℹ️ Tentang</a>
        </div>
        
        <div class="container">
            <div class="about-content">
                <h1>ℹ️ Tentang Al-Chips</h1>
                <p>Al-Chips adalah toko online terpercaya yang menyediakan berbagai macam keripik berkualitas tinggi. Sejak 2025, kami telah melayani ribuan pelanggan dengan produk keripik 100% alami tanpa pengawet.</p>
                
                <p>Kami berkomitmen untuk memberikan pengalaman berbelanja yang menyenangkan dengan produk-produk berkualitas tinggi, pengiriman yang cepat, dan pelayanan pelanggan yang prima.</p>
                
                <div class="features">
                    <div class="feature">
                        <h3>🌱 100% Alami</h3>
                        <p>Semua produk kami dibuat dari bahan-bahan alami pilihan tanpa pengawet buatan.</p>
                    </div>
                    <div class="feature">
                        <h3>🚚 Pengiriman Cepat</h3>
                        <p>Kami memastikan produk sampai dengan aman dan cepat ke tangan Anda.</p>
                    </div>
                    <div class="feature">
                        <h3>💪 Kualitas Terjamin</h3>
                        <p>Setiap produk melalui proses quality control yang ketat sebelum dikirim.</p>
                    </div>
                </div>
                
                <a href="/shop/products/" class="btn">🛍️ Lihat Produk Kami</a>
                <a href="/contact/" class="btn btn-secondary">📞 Hubungi Kami</a>
            </div>
        </div>
    </body>
    </html>
    """)
