# -*- coding: utf-8 -*-
"""
Redesign showcase header into a compact, ultra-sleek, and optimized low-profile bar.
"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

compact_css = """
  /* ================= Semicolon Video Showcase (Compact Studio Design) ================= */
  .video-showcase-wrapper {
    margin: 35px 0 40px;
    background: 
      radial-gradient(circle at 85% 25%, rgba(215, 38, 56, 0.15) 0%, transparent 40%),
      radial-gradient(circle at 15% 25%, rgba(246, 190, 31, 0.12) 0%, transparent 40%),
      radial-gradient(circle at 50% 10%, #1a1324 0%, #0d0a14 55%, #050408 100%);
    border: 1.5px solid rgba(246, 190, 31, 0.4);
    border-radius: 28px;
    padding: 22px 26px 20px;
    box-shadow: 0 25px 70px rgba(0, 0, 0, 0.75), 0 0 45px rgba(215, 38, 56, 0.18);
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
    background-position: right -10px center;
    background-size: 320px auto;
    opacity: 0.11;
    filter: grayscale(15%) contrast(1.1) drop-shadow(0 0 30px rgba(246, 190, 31, 0.35));
    pointer-events: none;
    z-index: 1;
    mask-image: radial-gradient(circle at right center, rgba(0,0,0,1) 30%, rgba(0,0,0,0) 80%);
    -webkit-mask-image: radial-gradient(circle at right center, rgba(0,0,0,1) 30%, rgba(0,0,0,0) 80%);
  }
  .video-showcase-wrapper::after {
    content: "";
    position: absolute;
    top: 0; right: 0; bottom: 0; left: 0;
    background: repeating-linear-gradient(0deg, rgba(255,255,255,0.008) 0px, rgba(255,255,255,0.008) 1px, transparent 1px, transparent 28px);
    pointer-events: none;
    z-index: 1;
  }

  /* Compact Horizontal Row Header */
  .video-showcase-header {
    display: flex !important;
    flex-direction: row !important;
    align-items: center !important;
    justify-content: space-between !important;
    gap: 16px !important;
    margin-bottom: 18px !important;
    position: relative !important;
    z-index: 3 !important;
    width: 100% !important;
  }
  @media (max-width: 820px) {
    .video-showcase-header {
      flex-direction: column !important;
      gap: 12px !important;
    }
  }

  /* Right Side: Compact Teacher Profile Glass Card */
  .profile-hero-card {
    display: flex !important;
    align-items: center !important;
    gap: 12px !important;
    background: linear-gradient(135deg, rgba(26, 20, 36, 0.8) 0%, rgba(16, 12, 22, 0.9) 100%) !important;
    border: 1.2px solid rgba(246, 190, 31, 0.35) !important;
    border-radius: 18px !important;
    padding: 8px 16px 8px 12px !important;
    backdrop-filter: blur(16px) !important;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4), 0 0 15px rgba(246, 190, 31, 0.12) !important;
    flex: 1 1 0 !important;
    min-width: 0 !important;
  }
  .profile-avatar-ring {
    width: 52px;
    height: 52px;
    border-radius: 50%;
    background: linear-gradient(135deg, #f6be1f 0%, #d72638 50%, #a855f7 100%);
    padding: 2.5px;
    box-shadow: 0 0 16px rgba(246, 190, 31, 0.5), 0 4px 12px rgba(0,0,0,0.6);
    flex-shrink: 0;
    position: relative;
    animation: avatarPulse 4s infinite alternate ease-in-out;
  }
  @keyframes avatarPulse {
    0% { transform: scale(1); box-shadow: 0 0 14px rgba(246, 190, 31, 0.4); }
    100% { transform: scale(1.03); box-shadow: 0 0 25px rgba(215, 38, 56, 0.6); }
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
    gap: 2px;
    text-align: right;
    min-width: 0;
  }
  .profile-name-row {
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .profile-name-row h2 {
    font-family: 'The Year of Handicrafts', 'Cairo', sans-serif;
    font-size: 20px;
    font-weight: 800;
    color: #ffffff;
    margin: 0;
    text-shadow: 0 2px 10px rgba(0,0,0,0.8), 0 0 18px rgba(246, 190, 31, 0.3);
    letter-spacing: 0.3px;
    line-height: 1.2;
    white-space: nowrap;
  }
  .verified-badge {
    background: linear-gradient(135deg, #f6be1f 0%, #d49f0f 100%);
    color: #0c0910;
    font-size: 10.5px;
    font-weight: 900;
    padding: 2px 7px;
    border-radius: 12px;
    display: inline-flex;
    align-items: center;
    gap: 3px;
    box-shadow: 0 2px 6px rgba(246, 190, 31, 0.4);
    white-space: nowrap;
  }
  .profile-role {
    font-size: 12px;
    color: #f1f5f9;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 4px;
    white-space: nowrap;
  }

  /* Left Side: Compact Semicolon Academy Card */
  .academy-branding-card {
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    gap: 12px !important;
    background: linear-gradient(135deg, rgba(26, 20, 36, 0.8) 0%, rgba(24, 12, 18, 0.9) 100%) !important;
    border: 1.2px solid rgba(215, 38, 56, 0.4) !important;
    border-radius: 18px !important;
    padding: 8px 16px !important;
    backdrop-filter: blur(16px) !important;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4), 0 0 15px rgba(215, 38, 56, 0.15) !important;
    flex: 1 1 0 !important;
    min-width: 0 !important;
  }
  .academy-text-details {
    display: flex;
    flex-direction: column;
    gap: 2px;
    text-align: right;
    min-width: 0;
    flex: 1;
  }
  .academy-brand-row {
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
  }
  .academy-logo-pill {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    background: rgba(215, 38, 56, 0.22);
    border: 1px solid rgba(215, 38, 56, 0.5);
    padding: 2px 8px;
    border-radius: 14px;
    box-shadow: 0 0 10px rgba(215, 38, 56, 0.3);
  }
  .semicolon-symbol {
    font-family: 'Exo 2', monospace;
    font-size: 15px;
    font-weight: 900;
    color: #ff3344;
    text-shadow: 0 0 8px #ff3344;
    line-height: 1;
  }
  .academy-brand-text {
    font-family: 'Exo 2', sans-serif;
    font-size: 11.5px;
    font-weight: 900;
    letter-spacing: 1.2px;
    color: #ffffff;
    text-transform: uppercase;
  }
  .academy-arabic-name {
    font-family: 'The Year of Handicrafts', 'Cairo', sans-serif;
    font-size: 14.5px;
    font-weight: 800;
    color: #f6be1f;
    text-shadow: 0 2px 8px rgba(0,0,0,0.6);
    white-space: nowrap;
  }
  .grade-unit-badge {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.12);
    color: #e2e8f0;
    font-size: 11px;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 12px;
    display: inline-flex;
    align-items: center;
    gap: 4px;
    white-space: nowrap;
    width: fit-content;
  }

  /* ================= Enlarged Studio Laptop Mockup ================= */
  .laptop-mockup-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 14px 0 20px;
    position: relative;
    z-index: 3;
    width: 100%;
  }
  .laptop-mockup-container::before {
    content: "";
    position: absolute;
    width: 85%;
    height: 70%;
    background: radial-gradient(ellipse at center, rgba(230, 57, 70, 0.4) 0%, rgba(246, 190, 31, 0.22) 45%, transparent 75%);
    filter: blur(55px);
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
    border: 3.5px solid #3c3850;
    border-bottom: none;
    border-radius: 24px 24px 4px 4px;
    padding: 12px 16px 18px;
    box-shadow: 0 -14px 40px rgba(0,0,0,0.8), inset 0 1px 3px rgba(255,255,255,0.25);
    position: relative;
  }
  .laptop-camera {
    width: 7px;
    height: 7px;
    background: #020204;
    border: 1.5px solid #635f7c;
    border-radius: 50%;
    margin: 0 auto 10px;
    box-shadow: 0 0 5px rgba(255,255,255,0.3);
  }
  .laptop-screen {
    position: relative;
    width: 100%;
    padding-bottom: 56.25%;
    background: #000000;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: inset 0 0 30px rgba(0,0,0,0.98), 0 0 22px rgba(0,0,0,0.7);
  }
  .laptop-base {
    width: 114%;
    height: 26px;
    background: linear-gradient(to bottom, #504d64 0%, #323042 40%, #1a1824 100%);
    border-radius: 4px 4px 26px 26px;
    box-shadow: 0 22px 50px rgba(0, 0, 0, 0.9), 0 6px 16px rgba(0, 0, 0, 0.6);
    position: relative;
    display: flex;
    justify-content: center;
  }
  .laptop-notch {
    width: 110px;
    height: 7px;
    background: #14131c;
    border-radius: 0 0 7px 7px;
    box-shadow: inset 0 1px 3px rgba(0,0,0,0.9);
  }

  /* Bottom Footer & Contacts Bar */
  .video-showcase-footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    margin-top: 16px;
    flex-wrap: wrap;
    position: relative;
    z-index: 3;
    background: rgba(18, 14, 26, 0.85);
    border: 1.2px solid rgba(255, 255, 255, 0.12);
    border-radius: 50px;
    padding: 10px 22px;
    backdrop-filter: blur(14px);
  }
  @media (max-width: 768px) {
    .video-showcase-footer {
      flex-direction: column;
      text-align: center;
      padding: 12px 16px;
    }
  }
  .footer-contact-group {
    display: flex;
    align-items: center;
    gap: 12px;
    flex-wrap: wrap;
  }
  .contact-pill-item {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.18);
    border-radius: 24px;
    padding: 5px 14px;
    color: #ffffff;
    font-family: 'Exo 2', 'Cairo', sans-serif;
    font-size: 13.5px;
    font-weight: 800;
    letter-spacing: 0.5px;
    direction: ltr;
  }
  .phone-dot-icon {
    width: 22px;
    height: 22px;
    background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
    color: #ffffff;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 11.5px;
    box-shadow: 0 0 10px rgba(37, 211, 102, 0.4);
  }
  .footer-social-cta {
    font-size: 13px;
    font-weight: 700;
    color: #f6be1f;
    display: flex;
    align-items: center;
    gap: 6px;
  }
"""

# Replace CSS
css_search_pattern = r'/\* ================= Semicolon Video Showcase.*?/\* ================= School Textbook Exercises Component ================= \*/'
if re.search(css_search_pattern, html, flags=re.DOTALL):
    html = re.sub(css_search_pattern, compact_css + '\n\n  /* ================= School Textbook Exercises Component ================= */', html, flags=re.DOTALL)
    print("Replaced showcase CSS with compact studio design successfully!")

# Compact HTML Structure
compact_html = """  <!-- =================== SEMICOLON VIP VIDEO SHOWCASE (COMPACT STUDIO) =================== -->
  <div class="video-showcase-wrapper">
    <!-- Compact Top Header Bar with 2 Balanced Slim Cards -->
    <div class="video-showcase-header">
      
      <!-- Right Side: Teacher Profile Slim Card -->
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
        </div>
      </div>

      <!-- Left Side: Semicolon Academy Slim Card -->
      <div class="academy-branding-card">
        <div class="academy-text-details">
          <div class="academy-brand-row">
            <div class="academy-logo-pill">
              <span class="semicolon-symbol">;</span>
              <span class="academy-brand-text">SEMICOLON ACADEMY</span>
            </div>
            <div class="academy-arabic-name">أكاديمية سيمي كولون للبرمجة</div>
          </div>
          <div class="grade-unit-badge">
            <span>📘 الصف الأول الثانوي (بكالوريا) — الوحدة 6: تصميم المعلومات</span>
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

    <!-- Bottom Footer Bar with Contacts & Social CTA -->
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

# Replace HTML
html_search_pattern = r'<!-- =================== SEMICOLON VIP VIDEO SHOWCASE \(BEFORE CHAPTER 6\) =================== -->\s*<div class="video-showcase-wrapper">.*?</div>\s*</div>\s*(?=\s*<div class="unit-title" id="unit6">)'

if re.search(html_search_pattern, html, flags=re.DOTALL):
    html = re.sub(html_search_pattern, compact_html + '\n\n  ', html, flags=re.DOTALL)
    print("Replaced showcase HTML with compact design successfully!")
else:
    start_pos = html.find('id="unit6-video-player"')
    if start_pos != -1:
        wrap_start = html.rfind('<div class="video-showcase-wrapper">', 0, start_pos)
        unit6_start = html.find('<div class="unit-title" id="unit6">', start_pos)
        html = html[:wrap_start] + compact_html + '\n\n  ' + html[unit6_start:]
        print("Replaced via index bounds!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html completely updated with compact design!")
