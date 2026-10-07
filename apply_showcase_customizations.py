# -*- coding: utf-8 -*-
"""
Apply user updates:
1. Add profile.png as artistic watermark/background to the video showcase section.
2. Add Semicolon Academy logo (icon.svg) to the header.
3. Remove the play/stop button from the footer.
4. Optimize the layout and styling.
"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Enhanced Showcase CSS with Teacher Background Watermark
updated_showcase_css = """
  /* ================= Semicolon Video Showcase (VIP Studio Design with Background) ================= */
  .video-showcase-wrapper {
    margin: 45px 0 50px;
    background: 
      radial-gradient(circle at 85% 30%, rgba(215, 38, 56, 0.18) 0%, transparent 45%),
      radial-gradient(circle at 15% 30%, rgba(246, 190, 31, 0.15) 0%, transparent 45%),
      radial-gradient(circle at 50% 10%, #1c1528 0%, #0e0a16 55%, #050408 100%);
    border: 2px solid rgba(246, 190, 31, 0.5);
    border-radius: 36px;
    padding: 34px 38px 28px;
    box-shadow: 0 30px 80px rgba(0, 0, 0, 0.8), 0 0 60px rgba(215, 38, 56, 0.25), inset 0 1px 2px rgba(255, 255, 255, 0.2);
    color: #ffffff;
    position: relative;
    overflow: hidden;
  }

  /* Artistic Teacher Silhouette / Background Watermark */
  .video-showcase-wrapper::before {
    content: "";
    position: absolute;
    top: 0; right: 0; bottom: 0; left: 0;
    background-image: url('profile.png');
    background-repeat: no-repeat;
    background-position: right -15px center;
    background-size: 380px auto;
    opacity: 0.13;
    filter: grayscale(15%) contrast(1.15) drop-shadow(0 0 35px rgba(246, 190, 31, 0.4));
    pointer-events: none;
    z-index: 1;
    mask-image: radial-gradient(circle at right center, rgba(0,0,0,1) 30%, rgba(0,0,0,0) 80%);
    -webkit-mask-image: radial-gradient(circle at right center, rgba(0,0,0,1) 30%, rgba(0,0,0,0) 80%);
  }

  /* Background grid lines */
  .video-showcase-wrapper::after {
    content: "";
    position: absolute;
    top: 0; right: 0; bottom: 0; left: 0;
    background: repeating-linear-gradient(0deg, rgba(255,255,255,0.01) 0px, rgba(255,255,255,0.01) 1px, transparent 1px, transparent 32px);
    pointer-events: none;
    z-index: 1;
  }

  /* Horizontal Row Header */
  .video-showcase-header {
    display: flex !important;
    flex-direction: row !important;
    align-items: stretch !important;
    justify-content: space-between !important;
    gap: 20px !important;
    margin-bottom: 28px !important;
    position: relative !important;
    z-index: 3 !important;
    width: 100% !important;
  }
  @media (max-width: 900px) {
    .video-showcase-header {
      flex-direction: column !important;
      gap: 16px !important;
    }
  }

  /* Right Side: Teacher Profile Glass Card */
  .profile-hero-card {
    display: flex !important;
    align-items: center !important;
    gap: 18px !important;
    background: linear-gradient(135deg, rgba(30, 24, 40, 0.75) 0%, rgba(20, 16, 28, 0.85) 100%) !important;
    border: 1.5px solid rgba(246, 190, 31, 0.45) !important;
    border-radius: 26px !important;
    padding: 16px 24px !important;
    backdrop-filter: blur(20px) !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), 0 0 25px rgba(246, 190, 31, 0.18) !important;
    flex: 1 1 0 !important;
    min-width: 0 !important;
  }
  .profile-avatar-ring {
    width: 86px;
    height: 86px;
    border-radius: 50%;
    background: linear-gradient(135deg, #f6be1f 0%, #d72638 50%, #a855f7 100%);
    padding: 3.5px;
    box-shadow: 0 0 25px rgba(246, 190, 31, 0.6), 0 6px 18px rgba(0,0,0,0.7);
    flex-shrink: 0;
    position: relative;
    animation: avatarPulse 4s infinite alternate ease-in-out;
  }
  @keyframes avatarPulse {
    0% { transform: scale(1); box-shadow: 0 0 20px rgba(246, 190, 31, 0.45); }
    100% { transform: scale(1.04); box-shadow: 0 0 35px rgba(215, 38, 56, 0.7); }
  }
  .profile-avatar-img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
    background: #110e1a;
    display: block;
  }
  .profile-info {
    display: flex;
    flex-direction: column;
    gap: 4px;
    text-align: right;
    min-width: 0;
  }
  .profile-name-row {
    display: flex;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
  }
  .profile-name-row h2 {
    font-family: 'The Year of Handicrafts', 'Cairo', sans-serif;
    font-size: 27px;
    font-weight: 800;
    color: #ffffff;
    margin: 0;
    text-shadow: 0 2px 14px rgba(0,0,0,0.9), 0 0 25px rgba(246, 190, 31, 0.4);
    letter-spacing: 0.5px;
    line-height: 1.2;
    white-space: nowrap;
  }
  .verified-badge {
    background: linear-gradient(135deg, #f6be1f 0%, #d49f0f 100%);
    color: #0c0910;
    font-size: 12px;
    font-weight: 900;
    padding: 3px 10px;
    border-radius: 20px;
    display: inline-flex;
    align-items: center;
    gap: 4px;
    box-shadow: 0 2px 10px rgba(246, 190, 31, 0.5);
    white-space: nowrap;
  }
  .profile-role {
    font-size: 14px;
    color: #f8fafc;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 6px;
    white-space: nowrap;
  }
  .profile-tagline {
    font-size: 12px;
    color: #cbd5e1;
    opacity: 0.95;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  /* Left Side: Semicolon Academy Branding Card with Logo */
  .academy-branding-card {
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    gap: 18px !important;
    background: linear-gradient(135deg, rgba(30, 24, 40, 0.75) 0%, rgba(28, 14, 20, 0.85) 100%) !important;
    border: 1.5px solid rgba(215, 38, 56, 0.5) !important;
    border-radius: 26px !important;
    padding: 16px 24px !important;
    backdrop-filter: blur(20px) !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), 0 0 25px rgba(215, 38, 56, 0.22) !important;
    flex: 1 1 0 !important;
    min-width: 0 !important;
  }
  .academy-logo-container {
    width: 68px;
    height: 68px;
    background: rgba(215, 38, 56, 0.12);
    border: 1.5px solid rgba(215, 38, 56, 0.4);
    border-radius: 20px;
    padding: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    box-shadow: 0 0 20px rgba(215, 38, 56, 0.35);
  }
  .academy-logo-svg {
    width: 100%;
    height: 100%;
    object-fit: contain;
    filter: drop-shadow(0 0 8px rgba(246, 190, 31, 0.4));
  }
  .academy-text-details {
    display: flex;
    flex-direction: column;
    gap: 4px;
    text-align: right;
    min-width: 0;
    flex: 1;
  }
  .academy-logo-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(215, 38, 56, 0.25);
    border: 1px solid rgba(215, 38, 56, 0.6);
    padding: 3px 12px;
    border-radius: 20px;
    box-shadow: 0 0 15px rgba(215, 38, 56, 0.4);
    width: fit-content;
  }
  .semicolon-symbol {
    font-family: 'Exo 2', monospace;
    font-size: 18px;
    font-weight: 900;
    color: #ff3344;
    text-shadow: 0 0 10px #ff3344;
    line-height: 1;
  }
  .academy-brand-text {
    font-family: 'Exo 2', sans-serif;
    font-size: 13px;
    font-weight: 900;
    letter-spacing: 1.8px;
    color: #ffffff;
    text-transform: uppercase;
  }
  .academy-arabic-name {
    font-family: 'The Year of Handicrafts', 'Cairo', sans-serif;
    font-size: 16.5px;
    font-weight: 800;
    color: #f6be1f;
    text-shadow: 0 2px 10px rgba(0,0,0,0.7);
    white-space: nowrap;
    margin-top: 2px;
  }
  .grade-unit-badge {
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.18);
    color: #f1f5f9;
    font-size: 12px;
    font-weight: 700;
    padding: 3px 10px;
    border-radius: 20px;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    white-space: nowrap;
    width: fit-content;
  }

  /* ================= Enlarged Studio Laptop Mockup ================= */
  .laptop-mockup-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 20px 0 28px;
    position: relative;
    z-index: 3;
    width: 100%;
  }
  .laptop-mockup-container::before {
    content: "";
    position: absolute;
    width: 85%;
    height: 70%;
    background: radial-gradient(ellipse at center, rgba(230, 57, 70, 0.45) 0%, rgba(246, 190, 31, 0.28) 45%, transparent 75%);
    filter: blur(60px);
    z-index: 1;
    pointer-events: none;
  }
  .laptop-device {
    width: 100%;
    max-width: 1060px;
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
    z-index: 2;
  }
  .laptop-lid {
    width: 100%;
    background: #0d0c14;
    border: 4px solid #3c3850;
    border-bottom: none;
    border-radius: 26px 26px 4px 4px;
    padding: 14px 18px 22px;
    box-shadow: 0 -15px 45px rgba(0,0,0,0.8), inset 0 1px 3px rgba(255,255,255,0.3);
    position: relative;
  }
  .laptop-camera {
    width: 8px;
    height: 8px;
    background: #020204;
    border: 1.5px solid #635f7c;
    border-radius: 50%;
    margin: 0 auto 12px;
    box-shadow: 0 0 6px rgba(255,255,255,0.35);
  }
  .laptop-screen {
    position: relative;
    width: 100%;
    padding-bottom: 56.25%;
    background: #000000;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: inset 0 0 30px rgba(0,0,0,0.98), 0 0 25px rgba(0,0,0,0.7);
  }
  .laptop-base {
    width: 114%;
    height: 28px;
    background: linear-gradient(to bottom, #504d64 0%, #323042 40%, #1a1824 100%);
    border-radius: 4px 4px 28px 28px;
    box-shadow: 0 25px 60px rgba(0, 0, 0, 0.9), 0 8px 20px rgba(0, 0, 0, 0.65);
    position: relative;
    display: flex;
    justify-content: center;
  }
  .laptop-notch {
    width: 120px;
    height: 8px;
    background: #14131c;
    border-radius: 0 0 8px 8px;
    box-shadow: inset 0 1px 3px rgba(0,0,0,0.9);
  }

  /* Bottom Footer & Contacts Bar (Centered Luxury Studio Bar) */
  .video-showcase-footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    margin-top: 20px;
    flex-wrap: wrap;
    position: relative;
    z-index: 3;
    background: rgba(18, 14, 26, 0.85);
    border: 1.5px solid rgba(255, 255, 255, 0.15);
    border-radius: 50px;
    padding: 12px 28px;
    backdrop-filter: blur(16px);
  }
  @media (max-width: 768px) {
    .video-showcase-footer {
      flex-direction: column;
      text-align: center;
      padding: 14px 18px;
    }
  }
  .footer-contact-group {
    display: flex;
    align-items: center;
    gap: 14px;
    flex-wrap: wrap;
  }
  .contact-pill-item {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: rgba(255, 255, 255, 0.07);
    border: 1px solid rgba(255, 255, 255, 0.22);
    border-radius: 30px;
    padding: 7px 18px;
    color: #ffffff;
    font-family: 'Exo 2', 'Cairo', sans-serif;
    font-size: 15px;
    font-weight: 800;
    letter-spacing: 0.5px;
    direction: ltr;
    box-shadow: 0 2px 8px rgba(0,0,0,0.3);
  }
  .phone-dot-icon {
    width: 26px;
    height: 26px;
    background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
    color: #ffffff;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 13px;
    box-shadow: 0 0 12px rgba(37, 211, 102, 0.5);
  }
  .footer-social-cta {
    font-size: 14.5px;
    font-weight: 700;
    color: #f6be1f;
    display: flex;
    align-items: center;
    gap: 8px;
    text-shadow: 0 2px 8px rgba(0,0,0,0.6);
  }
"""

# Replace showcase CSS block
css_search_pattern = r'/\* ================= Semicolon Video Showcase.*?/\* ================= School Textbook Exercises Component ================= \*/'
if re.search(css_search_pattern, html, flags=re.DOTALL):
    html = re.sub(css_search_pattern, updated_showcase_css + '\n\n  /* ================= School Textbook Exercises Component ================= */', html, flags=re.DOTALL)
    print("Replaced showcase CSS with background watermark and logo styles successfully!")

# New Showcase HTML without start/stop button and with academy logo
new_showcase_html = """  <!-- =================== SEMICOLON VIP VIDEO SHOWCASE (BEFORE CHAPTER 6) =================== -->
  <div class="video-showcase-wrapper">
    <!-- Top Header Bar with 2 Balanced VIP Cards -->
    <div class="video-showcase-header">
      
      <!-- Right Side: Teacher Profile Glass Card -->
      <div class="profile-hero-card">
        <div class="profile-avatar-ring">
          <img src="profile.png" alt="م. ريهام جمال" class="profile-avatar-img">
        </div>
        <div class="profile-info">
          <div class="profile-name-row">
            <h2>م. ريهام جمال</h2>
            <span class="verified-badge">✓ معتمد</span>
          </div>
          <div class="profile-role">
            <span>خبير ومُعلم مادة البرمجة والذكاء الاصطناعي</span>
          </div>
          <div class="profile-tagline">
            <span>✨ إعداد وشرح المنهج الرقمي التفاعلي لطلاب الصف الأول الثانوي</span>
          </div>
        </div>
      </div>

      <!-- Left Side: Semicolon Academy Branding Card with Logo -->
      <div class="academy-branding-card">
        <div class="academy-logo-container">
          <img src="icon.svg" alt="Semicolon Academy Logo" class="academy-logo-svg">
        </div>
        <div class="academy-text-details">
          <div class="academy-logo-pill">
            <span class="semicolon-symbol">;</span>
            <span class="academy-brand-text">SEMICOLON ACADEMY</span>
          </div>
          <div class="academy-arabic-name">أكاديمية سيمي كولون للبرمجة والذكاء الاصطناعي</div>
          <div class="grade-unit-badge">
            <span>📘 الصف الأول الثانوي (بكالوريا) — شرح الوحدة السادسة: تصميم المعلومات</span>
          </div>
        </div>
      </div>

    </div>

    <!-- Enlarged Studio Laptop Mockup Device -->
    <div class="laptop-mockup-container">
      <div class="laptop-device">
        <!-- Screen Lid -->
        <div class="laptop-lid">
          <div class="laptop-camera"></div>
          <div class="laptop-screen" id="laptop-screen-box">
            <video id="unit6-video-player" controls preload="metadata" poster="https://img.youtube.com/vi/Vq04T0Cwj5Y/maxresdefault.jpg" style="width:100%; height:100%; position:absolute; top:0; left:0; border-radius:10px; background:#000; object-fit:contain;">
              <source src="unit6_video.webm" type="video/webm">
              <source src="unit6_video.mp4" type="video/mp4">
              متصفحك لا يدعم تشغيل الفيديو المباشر.
            </video>
          </div>
        </div>
        <!-- Laptop Base / Deck -->
        <div class="laptop-base">
          <div class="laptop-notch"></div>
        </div>
      </div>
    </div>

    <!-- Bottom Footer Bar with Contacts & Social CTA (No Start/Stop Button) -->
    <div class="video-showcase-footer">
      <div class="footer-contact-group">
        <div class="contact-pill-item">
          <span class="phone-dot-icon">📞</span>
          <span>01158659437</span>
        </div>
        <div class="contact-pill-item">
          <span class="phone-dot-icon">📱</span>
          <span>01221315065</span>
        </div>
      </div>

      <div class="footer-social-cta">
        <span>🌟 تابعوا صفحتنا الرسمية (Semicolon Academy) لمشاهدة جميع الشروحات والمراجعات الشاملة</span>
      </div>
    </div>
  </div>"""

# Replace showcase HTML
html_search_pattern = r'<!-- =================== SEMICOLON VIP VIDEO SHOWCASE \(BEFORE CHAPTER 6\) =================== -->\s*<div class="video-showcase-wrapper">.*?</div>\s*</div>\s*(?=\s*<div class="unit-title" id="unit6">)'

if re.search(html_search_pattern, html, flags=re.DOTALL):
    html = re.sub(html_search_pattern, new_showcase_html + '\n\n  ', html, flags=re.DOTALL)
    print("Replaced showcase HTML successfully!")
else:
    print("Direct pattern match failed, using delimiter replacement...")
    start_pos = html.find('id="unit6-video-player"')
    if start_pos != -1:
        wrap_start = html.rfind('<div class="video-showcase-wrapper">', 0, start_pos)
        unit6_start = html.find('<div class="unit-title" id="unit6">', start_pos)
        html = html[:wrap_start] + new_showcase_html + '\n\n  ' + html[unit6_start:]
        print("Replaced via index bounds successfully!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html completely updated!")
