from django.shortcuts import render
from django.http import HttpResponse
import datetime

def home(request):
    nama = "Aldi"
    waktu = datetime.datetime.now().strftime("%H:%M:%S")

    return HttpResponse(f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>🏠 Home - Al-Chips Shopping Online</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}

            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                color: #333;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
            }}

            .nav {{
                text-align: center;
                padding: 20px;
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                border-bottom: 1px solid rgba(255, 255, 255, 0.2);
            }}

            .nav a {{
                margin: 0 15px;
                text-decoration: none;
                color: white;
                font-weight: bold;
                padding: 10px 20px;
                border-radius: 25px;
                background: rgba(255, 255, 255, 0.1);
                transition: all 0.3s;
            }}

            .nav a:hover {{
                background: rgba(255, 255, 255, 0.2);
                transform: translateY(-2px);
            }}

            .hero {{
                text-align: center;
                padding: 80px 20px;
                color: white;
            }}

            .hero h1 {{
                font-size: 3.5rem;
                margin-bottom: 20px;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            }}

            .hero p {{
                font-size: 1.2rem;
                margin-bottom: 30px;
                opacity: 0.9;
            }}

            .btn {{
                display: inline-block;
                padding: 15px 30px;
                background: #ff6b6b;
                color: white;
                text-decoration: none;
                border-radius: 50px;
                font-weight: bold;
                font-size: 1.1rem;
                transition: all 0.3s;
                box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3);
            }}

            .btn:hover {{
                background: #ff5252;
                transform: translateY(-3px);
                box-shadow: 0 6px 20px rgba(255, 107, 107, 0.4);
            }}

            .container {{
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 20px;
            }}

            .features {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 30px;
                padding: 60px 0;
            }}

            .feature-card {{
                background: rgba(255, 255, 255, 0.95);
                padding: 30px;
                border-radius: 20px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
                text-align: center;
                transition: transform 0.3s;
                backdrop-filter: blur(10px);
            }}

            .feature-card:hover {{
                transform: translateY(-10px);
            }}

            .feature-card h3 {{
                color: #667eea;
                margin-bottom: 15px;
                font-size: 1.5rem;
            }}

            .welcome {{
                background: rgba(255, 255, 255, 0.1);
                padding: 40px;
                border-radius: 20px;
                text-align: center;
                margin: 40px 0;
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.2);
            }}

            .welcome h2 {{
                color: white;
                margin-bottom: 10px;
                font-size: 2rem;
            }}

            .welcome p {{
                color: white;
                opacity: 0.9;
                font-size: 1.1rem;
            }}

            .stats {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px;
                padding: 40px 0;
            }}

            .stat {{
                background: rgba(255, 255, 255, 0.1);
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.2);
            }}

            .stat h3 {{
                color: #ffd700;
                font-size: 2rem;
                margin-bottom: 5px;
            }}

            .stat p {{
                color: white;
                opacity: 0.8;
            }}

            footer {{
                background: rgba(0, 0, 0, 0.3);
                padding: 30px;
                text-align: center;
                color: white;
                backdrop-filter: blur(10px);
            }}

            @media (max-width: 768px) {{
                .hero h1 {{
                    font-size: 2.5rem;
                }}

                .features {{
                    grid-template-columns: 1fr;
                }}

                .stats {{
                    grid-template-columns: 1fr;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="nav">
            <a href="/" style="font-weight: bold; background: rgba(255, 255, 255, 0.2);">🏠 Home</a>
            <a href="/about/">📋 About</a>
            <a href="/contact/">📞 Contact</a>
            <a href="/shop/">🛍️ Shop</a>
        </div>

        <section class="hero">
            <div class="container">
                <h1>🎉 Welcome to Al-Chips!</h1>
                <p>Your ultimate destination for premium quality chips and snacks</p>
                <a href="/shop/" class="btn">🛍️ Start Shopping</a>
            </div>
        </section>

        <section class="container">
            <div class="features">
                <div class="feature-card">
                    <h3>🥔 Premium Quality</h3>
                    <p>All our chips are made from the finest ingredients with no artificial preservatives or additives.</p>
                </div>
                <div class="feature-card">
                    <h3>🚚 Fast Delivery</h3>
                    <p>Get your favorite chips delivered to your doorstep quickly and safely.</p>
                </div>
                <div class="feature-card">
                    <h3>💳 Secure Payment</h3>
                    <p>Shop with confidence using our secure and trusted payment methods.</p>
                </div>
            </div>

            <div class="welcome">
                <h2>Hello {nama}! 👋</h2>
                <p>Current time: <strong>{waktu}</strong></p>
                <p>Welcome to your Django-powered shopping experience!</p>
            </div>

            <div class="stats">
                <div class="stat">
                    <h3>1000+</h3>
                    <p>Happy Customers</p>
                </div>
                <div class="stat">
                    <h3>50+</h3>
                    <p>Product Variants</p>
                </div>
                <div class="stat">
                    <h3>2025</h3>
                    <p>Founded Year</p>
                </div>
                <div class="stat">
                    <h3>⭐5.0</h3>
                    <p>Customer Rating</p>
                </div>
            </div>
        </section>

        <footer>
            <div class="container">
                <h3>🛍️ Al-Chips Shopping Online</h3>
                <p>Made with ❤️ using Django Framework</p>
                <p>&copy; 2025 Al-Chips. All rights reserved.</p>
            </div>
        </footer>
    </body>
    </html>
    """)

def about(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>About - Django Website</title>
        <style>
            body { font-family: Arial; margin: 40px; background: #f0f0f0; }
            .container { background: white; padding: 30px; border-radius: 10px; }
            h1 { color: #007bff; }
            ul { background: #e9ecef; padding: 15px; border-radius: 5px; }
            a { color: #007bff; text-decoration: none; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <div style="text-align: center; margin-bottom: 20px; padding: 10px; background: #e9ecef; border-radius: 5px;">
            <a href="/" style="margin: 0 15px; text-decoration: none; color: #007bff; font-weight: bold;">🏠 Home</a>
            <a href="/about/" style="margin: 0 15px; text-decoration: none; color: #007bff; font-weight: bold;">📋 About</a>
            <a href="/contact/" style="margin: 0 15px; text-decoration: none; color: #007bff;">📞 Contact</a>
            <a href="/shop/" style="margin: 0 15px; text-decoration: none; color: #007bff;">🛍️ Shop</a>
        </div>
        <div class="container">
            <h1>📋 Tentang Website</h1>
            <p>Ini adalah halaman About yang sudah distyling!</p>
            <p>Website ini dibuat dengan Python Django.</p>
            <ul>
                <li><strong>Framework:</strong> Django</li>
                <li><strong>Language:</strong> Python</li>
                <li><strong>Database:</strong> SQLite</li>
                <li><strong>Server:</strong> Development Server</li>
            </ul>
            <p><a href="/">← Kembali ke Home</a></p>
        </div>
    </body>
    </html>
    """)

def contact(request):
    return HttpResponse("""
    <div style="text-align: center; margin-bottom: 20px; padding: 10px; background: #f0f0f0; border-radius: 5px;">
        <a href="/" style="margin: 0 15px; text-decoration: none; color: #007bff;">🏠 Home</a>
        <a href="/about/" style="margin: 0 15px; text-decoration: none; color: #007bff;">📋 About</a>
        <a href="/contact/" style="margin: 0 15px; text-decoration: none; color: #007bff; font-weight: bold;">📞 Contact</a>
        <a href="/shop/" style="margin: 0 15px; text-decoration: none; color: #007bff;">🛍️ Shop</a>
    </div>
    <h1>📞 Contact Us</h1>
    <p>Hubungi kami di:</p>
    <ul>
        <li>Email: admin@website.com</li>
        <li>Phone: +62 123 456 789</li>
        <li>Address: Jakarta, Indonesia</li>
    </ul>
    <p><a href="/">← Kembali ke Home</a></p>
    """)
