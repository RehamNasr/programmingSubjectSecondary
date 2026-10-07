# -*- coding: utf-8 -*-
"""
Upgrade Showcase Header Layout and Enlarge Laptop Mockup
"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# CSS for Studio Header & Enlarged Laptop
header_and_laptop_css = """
  /* ================= Semicolon Video Showcase (VIP Studio Design) ================= */
  .video-showcase-wrapper {
    margin: 45px 0 50px;
    background: radial-gradient(circle at 50% 10%, #1e162b 0%, #0f0c18 55%, #06040a 100%);
    border: 2px solid rgba(246, 190, 31, 0.5);
    border-radius: 36px;
    padding: 36px 36px 32px;
    box-shadow: 0 30px 80px rgba(0, 0, 0, 0.75), 0 0 60px rgba(215, 38, 56, 0.22), inset 0 1px 2px rgba(255, 255, 255, 0.2);
    color: #ffffff;
    position: relative;
    overflow: hidden;
  }
  .video-showcase-wrapper::before {
    content: "";
    position: absolute;
    top: 0; right: 0; bottom: 0; left: 0;
    background: 
      radial-gradient(circle at 10% 15%, rgba(246, 190, 31, 0.1) 0%, transparent 45%),
      radial-gradient(circle at 90% 15%, rgba(215, 38, 56, 0.15) 0%, transparent 45%),
      repeating-linear-gradient(0deg, rgba(255,255,255,0.012) 0px, rgba(255,255,255,0.012) 1px, transparent 1px, transparent 30px);
    pointer-events: none;
  }

  /* Two-column perfectly separated VIP Header */
  .video-showcase-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    margin-bottom: 28px;
    position: relative;
    z-index: 2;
    width: 100%;
  }
  @media (max-width: 900px) {
    .video-showcase-header {
      flex-direction: column;
      align-items: stretch;
      gap: 16px;
    }
  }

  /* Right Side: Teacher Profile Glass Card */
  .profile-hero-card {
    display: flex;
    align-items: center;
    gap: 18px;
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(246, 190, 31, 0.04) 100%);
    border: 1.5px solid rgba(246, 190, 31, 0.4);
    border-radius: 26px;
    padding: 14px 22px 14px 18px;
    backdrop-filter: blur(16px);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4), 0 0 20px rgba(246, 190, 31, 0.15);
    flex: 1;
    max-width: 520px;
  }
  .profile-avatar-ring {
    width: 84px;
    height: 84px;
    border-radius: 50%;
    background: linear-gradient(135deg, #f6be1f 0%, #d72638 50%, #a855f7 100%);
    padding: 3.5px;
    box-shadow: 0 0 25px rgba(246, 190, 31, 0.55), 0 6px 18px rgba(0,0,0,0.6);
    flex-shrink: 0;
    position: relative;
    animation: avatarPulse 4s infinite alternate ease-in-out;
  }
  @keyframes avatarPulse {
    0% { transform: scale(1); box-shadow: 0 0 20px rgba(246, 190, 31, 0.4); }
    100% { transform: scale(1.04); box-shadow: 0 0 35px rgba(215, 38, 56, 0.65); }
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
  }
  .profile-name-row {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .profile-name-row h2 {
    font-family: 'The Year of Handicrafts', 'Cairo', sans-serif;
    font-size: 28px;
    font-weight: 800;
    color: #ffffff;
    margin: 0;
    text-shadow: 0 2px 14px rgba(0,0,0,0.9), 0 0 25px rgba(246, 190, 31, 0.35);
    letter-spacing: 0.5px;
    line-height: 1.2;
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
    box-shadow: 0 2px 10px rgba(246, 190, 31, 0.45);
    white-space: nowrap;
  }
  .profile-role {
    font-size: 14px;
    color: #f8fafc;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 6px;
    margin-top: 2px;
  }
  .profile-role .academy-highlight {
    color: #f6be1f;
    font-weight: 800;
  }
  .profile-tagline {
    font-size: 12.5px;
    color: #cbd5e1;
    opacity: 0.95;
    margin-top: 2px;
  }

  /* Left Side: Semicolon Academy Branding Card */
  .academy-branding-card {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 6px;
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(215, 38, 56, 0.05) 100%);
    border: 1.5px solid rgba(215, 38, 56, 0.45);
    border-radius: 26px;
    padding: 14px 22px;
    backdrop-filter: blur(16px);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4), 0 0 20px rgba(215, 38, 56, 0.18);
    flex: 1;
    max-width: 520px;
    text-align: left;
  }
  @media (max-width: 900px) {
    .academy-branding-card {
      align-items: flex-start;
      text-align: right;
    }
  }
  .academy-logo-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(215, 38, 56, 0.2);
    border: 1.5px solid rgba(215, 38, 56, 0.55);
    padding: 5px 16px;
    border-radius: 30px;
    box-shadow: 0 0 20px rgba(215, 38, 56, 0.35);
  }
  .semicolon-symbol {
    font-family: 'Exo 2', monospace;
    font-size: 22px;
    font-weight: 900;
    color: #ff3344;
    text-shadow: 0 0 12px #ff3344;
    line-height: 1;
  }
  .academy-brand-text {
    font-family: 'Exo 2', sans-serif;
    font-size: 15px;
    font-weight: 900;
    letter-spacing: 2px;
    color: #ffffff;
    text-transform: uppercase;
  }
  .academy-arabic-name {
    font-family: 'The Year of Handicrafts', 'Cairo', sans-serif;
    font-size: 17px;
    font-weight: 800;
    color: #f6be1f;
    text-shadow: 0 2px 10px rgba(0,0,0,0.7);
    margin-top: 2px;
  }
  .grade-unit-badge {
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.18);
    color: #f1f5f9;
    font-size: 12.5px;
    font-weight: 700;
    padding: 4px 14px;
    border-radius: 20px;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    margin-top: 2px;
  }

  /* ================= Enlarged Studio Laptop Mockup ================= */
  .laptop-mockup-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 20px 0 30px;
    position: relative;
    z-index: 2;
    width: 100%;
  }
  .laptop-mockup-container::before {
    content: "";
    position: absolute;
    width: 85%;
    height: 70%;
    background: radial-gradient(ellipse at center, rgba(230, 57, 70, 0.4) 0%, rgba(246, 190, 31, 0.25) 45%, transparent 75%);
    filter: blur(55px);
    z-index: 1;
    pointer-events: none;
  }
  .laptop-device {
    width: 100%;
    max-width: 1060px; /* ENLARGED LAPTOP */
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
    padding-bottom: 56.25%; /* 16:9 widescreen */
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

  /* Bottom Footer & Contacts Bar */
  .video-showcase-footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 18px;
    margin-top: 22px;
    flex-wrap: wrap;
    position: relative;
    z-index: 2;
    background: rgba(18, 14, 26, 0.8);
    border: 1.5px solid rgba(255, 255, 255, 0.15);
    border-radius: 50px;
    padding: 10px 22px 10px 14px;
    backdrop-filter: blur(16px);
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
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.22);
    border-radius: 30px;
    padding: 7px 16px;
    color: #ffffff;
    font-family: 'Exo 2', 'Cairo', sans-serif;
    font-size: 15px;
    font-weight: 800;
    letter-spacing: 0.5px;
    direction: ltr;
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
    font-size: 14px;
    font-weight: 700;
    color: #f6be1f;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .yt-direct-btn {
    background: linear-gradient(135deg, #d72638 0%, #b31d2c 100%);
    color: #ffffff;
    border: 1.5px solid rgba(255, 255, 255, 0.4);
    border-radius: 30px;
    padding: 10px 24px;
    font-family: 'The Year of Handicrafts', 'Cairo', sans-serif;
    font-size: 14.5px;
    font-weight: 800;
    cursor: pointer;
    box-shadow: 0 4px 18px rgba(215, 38, 56, 0.45);
    transition: all 0.25s ease;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    white-space: nowrap;
  }
  .yt-direct-btn:hover {
    transform: translateY(-2px);
    background: linear-gradient(135deg, #ff3344 0%, #d72638 100%);
    box-shadow: 0 8px 26px rgba(255, 51, 68, 0.65);
    border-color: #ffffff;
  }
"""

# Replace showcase CSS
old_css_pattern = r'/\* ================= Semicolon Video Showcase \(VIP Studio Design\) ================= \*/.*?\.yt-direct-btn:hover\s*\{.*?\}'
if re.search(old_css_pattern, html, flags=re.DOTALL):
    html = re.sub(old_css_pattern, header_and_laptop_css, html, flags=re.DOTALL)
    print("Replaced showcase CSS successfully!")
else:
    html = html.replace('</style>', header_and_laptop_css + '\n</style>')
    print("Appended new showcase CSS!")

# New Showcase HTML with 2 separate VIP cards in the top row and enlarged laptop
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

      <!-- Left Side: Semicolon Academy Branding Card -->
      <div class="academy-branding-card">
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

      <button type="button" class="yt-direct-btn" onclick="togglePlayLocalVideo()">
        <span id="video-play-btn-text">▶️ تشغيل / إيقاف الفيديو</span>
      </button>
    </div>
  </div>"""

# Replace old showcase HTML
old_showcase_pattern = r'<!-- =================== SEMICOLON VIP VIDEO SHOWCASE \(BEFORE CHAPTER 6\) =================== -->\s*<div class="video-showcase-wrapper">.*?</div>\s*</div>\s*(?=\s*<div class="unit-title" id="unit6">)'

if re.search(old_showcase_pattern, html, flags=re.DOTALL):
    html = re.sub(old_showcase_pattern, new_showcase_html + '\n\n  ', html, flags=re.DOTALL)
    print("Replaced showcase HTML with enlarged studio layout successfully!")
else:
    print("Could not match exact pattern, searching for start...")
    start_pos = html.find('id="unit6-video-player"')
    if start_pos != -1:
        wrap_start = html.rfind('<div class="video-showcase-wrapper">', 0, start_pos)
        unit6_start = html.find('<div class="unit-title" id="unit6">', start_pos)
        html = html[:wrap_start] + new_showcase_html + '\n\n  ' + html[unit6_start:]
        print("Replaced via index bounds successfully!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html successfully!")
