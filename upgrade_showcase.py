# -*- coding: utf-8 -*-
"""
Design a breathtaking showcase section with the teacher's profile photo (profile.png)
and Semicolon Academy branding for video recording and social media sharing.
"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Enhanced Showcase CSS
new_showcase_css = """
  /* ================= Semicolon Video Showcase (VIP Studio Design) ================= */
  .video-showcase-wrapper {
    margin: 55px 0 50px;
    background: radial-gradient(circle at 50% 10%, #20172e 0%, #100c19 55%, #07050b 100%);
    border: 2px solid rgba(246, 190, 31, 0.45);
    border-radius: 36px;
    padding: 36px 42px 32px;
    box-shadow: 0 25px 65px rgba(0, 0, 0, 0.65), 0 0 50px rgba(215, 38, 56, 0.2), inset 0 1px 2px rgba(255, 255, 255, 0.15);
    color: #ffffff;
    position: relative;
    overflow: hidden;
  }
  .video-showcase-wrapper::before {
    content: "";
    position: absolute;
    top: 0; right: 0; bottom: 0; left: 0;
    background: 
      radial-gradient(circle at 15% 20%, rgba(246, 190, 31, 0.08) 0%, transparent 40%),
      radial-gradient(circle at 85% 20%, rgba(215, 38, 56, 0.12) 0%, transparent 40%),
      repeating-linear-gradient(0deg, rgba(255,255,255,0.012) 0px, rgba(255,255,255,0.012) 1px, transparent 1px, transparent 28px);
    pointer-events: none;
  }

  .video-showcase-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 24px;
    flex-wrap: wrap;
    margin-bottom: 28px;
    position: relative;
    z-index: 2;
  }

  /* Right Side Profile Box */
  .profile-hero-box {
    display: flex;
    align-items: center;
    gap: 18px;
  }
  .profile-avatar-ring {
    width: 78px;
    height: 78px;
    border-radius: 50%;
    background: linear-gradient(135deg, #f6be1f 0%, #d72638 50%, #a855f7 100%);
    padding: 3px;
    box-shadow: 0 0 25px rgba(246, 190, 31, 0.5), 0 4px 15px rgba(0,0,0,0.5);
    flex-shrink: 0;
    position: relative;
    animation: avatarPulse 4s infinite alternate ease-in-out;
  }
  @keyframes avatarPulse {
    0% { transform: scale(1); box-shadow: 0 0 20px rgba(246, 190, 31, 0.4); }
    100% { transform: scale(1.03); box-shadow: 0 0 35px rgba(215, 38, 56, 0.6); }
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
    gap: 8px;
  }
  .profile-name-row h2 {
    font-family: 'The Year of Handicrafts', 'Cairo', sans-serif;
    font-size: 26px;
    font-weight: 800;
    color: #ffffff;
    margin: 0;
    text-shadow: 0 2px 12px rgba(0,0,0,0.8), 0 0 20px rgba(246, 190, 31, 0.25);
    letter-spacing: 0.5px;
  }
  .verified-badge {
    background: linear-gradient(135deg, #f6be1f 0%, #d49f0f 100%);
    color: #0c0910;
    font-size: 11.5px;
    font-weight: 900;
    padding: 2px 8px;
    border-radius: 20px;
    display: inline-flex;
    align-items: center;
    gap: 4px;
    box-shadow: 0 2px 8px rgba(246, 190, 31, 0.4);
  }
  .profile-role {
    font-size: 13.5px;
    color: #f1f5f9;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .profile-role .dot {
    color: #e63946;
  }
  .profile-tagline {
    font-size: 12px;
    color: #cbd5e1;
    opacity: 0.9;
  }

  /* Left Side Academy Branding Box */
  .academy-branding-box {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 5px;
    text-align: left;
  }
  @media (max-width: 768px) {
    .academy-branding-box {
      align-items: flex-start;
      text-align: right;
    }
  }
  .academy-logo-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(215, 38, 56, 0.16);
    border: 1.5px solid rgba(215, 38, 56, 0.5);
    padding: 5px 14px;
    border-radius: 30px;
    box-shadow: 0 0 20px rgba(215, 38, 56, 0.3);
  }
  .semicolon-symbol {
    font-family: 'Exo 2', monospace;
    font-size: 20px;
    font-weight: 900;
    color: #ff3344;
    text-shadow: 0 0 10px #ff3344;
    line-height: 1;
  }
  .academy-brand-text {
    font-family: 'Exo 2', sans-serif;
    font-size: 14px;
    font-weight: 900;
    letter-spacing: 1.8px;
    color: #ffffff;
    text-transform: uppercase;
  }
  .academy-arabic-name {
    font-family: 'Cairo', sans-serif;
    font-size: 15px;
    font-weight: 800;
    color: #f6be1f;
    text-shadow: 0 2px 10px rgba(0,0,0,0.6);
  }
  .grade-unit-badge {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.15);
    color: #e2e8f0;
    font-size: 12px;
    font-weight: 700;
    padding: 3px 12px;
    border-radius: 20px;
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }

  /* Ambient Screen Glow & Laptop Device */
  .laptop-mockup-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 15px 0 25px;
    position: relative;
    z-index: 2;
  }
  .laptop-mockup-container::before {
    content: "";
    position: absolute;
    width: 75%;
    height: 60%;
    background: radial-gradient(ellipse at center, rgba(230, 57, 70, 0.35) 0%, rgba(246, 190, 31, 0.2) 45%, transparent 75%);
    filter: blur(45px);
    z-index: 1;
    pointer-events: none;
  }
  .laptop-device {
    width: 100%;
    max-width: 860px;
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
    z-index: 2;
  }
  .laptop-lid {
    width: 100%;
    background: #0d0c14;
    border: 3.5px solid #38354a;
    border-bottom: none;
    border-radius: 22px 22px 4px 4px;
    padding: 12px 16px 18px;
    box-shadow: 0 -12px 35px rgba(0,0,0,0.7), inset 0 1px 3px rgba(255,255,255,0.25);
    position: relative;
  }
  .laptop-camera {
    width: 7px;
    height: 7px;
    background: #020204;
    border: 1.5px solid #5a5770;
    border-radius: 50%;
    margin: 0 auto 10px;
    box-shadow: 0 0 5px rgba(255,255,255,0.3);
  }
  .laptop-screen {
    position: relative;
    width: 100%;
    padding-bottom: 56.25%; /* 16:9 */
    background: #000000;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: inset 0 0 25px rgba(0,0,0,0.95), 0 0 20px rgba(0,0,0,0.6);
  }
  .laptop-base {
    width: 114%;
    height: 24px;
    background: linear-gradient(to bottom, #4c495e 0%, #2f2d3d 40%, #1a1824 100%);
    border-radius: 4px 4px 26px 26px;
    box-shadow: 0 22px 50px rgba(0, 0, 0, 0.85), 0 6px 16px rgba(0, 0, 0, 0.6);
    position: relative;
    display: flex;
    justify-content: center;
  }
  .laptop-notch {
    width: 100px;
    height: 7px;
    background: #14131c;
    border-radius: 0 0 7px 7px;
    box-shadow: inset 0 1px 3px rgba(0,0,0,0.85);
  }

  /* Bottom Footer & Contacts Bar */
  .video-showcase-footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    margin-top: 18px;
    flex-wrap: wrap;
    position: relative;
    z-index: 2;
    background: rgba(18, 14, 26, 0.75);
    border: 1.5px solid rgba(255, 255, 255, 0.12);
    border-radius: 50px;
    padding: 8px 18px 8px 10px;
    backdrop-filter: blur(14px);
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
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 30px;
    padding: 6px 14px;
    color: #ffffff;
    font-family: 'Exo 2', 'Cairo', sans-serif;
    font-size: 14px;
    font-weight: 800;
    letter-spacing: 0.5px;
    direction: ltr;
  }
  .phone-dot-icon {
    width: 24px;
    height: 24px;
    background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
    color: #ffffff;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 12px;
    box-shadow: 0 0 10px rgba(37, 211, 102, 0.4);
  }
  .footer-social-cta {
    font-size: 13.5px;
    font-weight: 700;
    color: #f6be1f;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .yt-direct-btn {
    background: linear-gradient(135deg, #d72638 0%, #b31d2c 100%);
    color: #ffffff;
    border: 1.5px solid rgba(255, 255, 255, 0.35);
    border-radius: 30px;
    padding: 8px 20px;
    font-family: 'The Year of Handicrafts', 'Cairo', sans-serif;
    font-size: 13.5px;
    font-weight: 800;
    cursor: pointer;
    box-shadow: 0 4px 15px rgba(215, 38, 56, 0.4);
    transition: all 0.25s ease;
    display: inline-flex;
    align-items: center;
    gap: 8px;
  }
  .yt-direct-btn:hover {
    transform: translateY(-2px);
    background: linear-gradient(135deg, #ff3344 0%, #d72638 100%);
    box-shadow: 0 6px 22px rgba(255, 51, 68, 0.6);
    border-color: #ffffff;
  }
"""

# Replace old video showcase CSS
old_css_pattern = r'/\* ================= Semicolon Video Showcase \(Laptop Frame\) ================= \*/.*?\.footer-divider-line\s*\{.*?\}'
if re.search(old_css_pattern, html, flags=re.DOTALL):
    html = re.sub(old_css_pattern, new_showcase_css, html, flags=re.DOTALL)
    print("Replaced old showcase CSS successfully!")
else:
    html = html.replace('</style>', new_showcase_css + '\n</style>')
    print("Appended new showcase CSS successfully!")

# New Showcase HTML Markup with Profile Photo (profile.png) and Luxury Academy Branding
new_showcase_html = """  <!-- =================== SEMICOLON VIP VIDEO SHOWCASE (BEFORE CHAPTER 6) =================== -->
  <div class="video-showcase-wrapper">
    <!-- Top Header Bar with Profile & Academy Branding -->
    <div class="video-showcase-header">
      
      <!-- Right Side: Teacher Profile -->
      <div class="profile-hero-box">
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
            <span class="dot">•</span>
            <span style="color:#f6be1f;">Semicolon Academy</span>
          </div>
          <div class="profile-tagline">
            <span>✨ إعداد وشرح المنهج الرقمي التفاعلي لطلاب الصف الأول الثانوي</span>
          </div>
        </div>
      </div>

      <!-- Left Side: Semicolon Academy Branding -->
      <div class="academy-branding-box">
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

    <!-- Laptop Mockup Device Frame -->
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

    <!-- Bottom Footer Bar with Phone & Social Info -->
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
old_showcase_pattern = r'<!-- =================== SEMICOLON VIDEO SHOWCASE \(BEFORE CHAPTER 6\) =================== -->\s*<div class="video-showcase-wrapper">.*?</div>\s*</div>\s*(?=\s*<div class="unit-title" id="unit6">)'

if re.search(old_showcase_pattern, html, flags=re.DOTALL):
    html = re.sub(old_showcase_pattern, new_showcase_html + '\n\n  ', html, flags=re.DOTALL)
    print("Replaced old showcase HTML with new VIP design successfully!")
else:
    print("Showcase pattern search failed, attempting fallback replacement...")
    # Find start
    start_pos = html.find('<div class="video-showcase-wrapper">')
    if start_pos != -1:
        end_pos = html.find('<div class="unit-title" id="unit6">', start_pos)
        html = html[:start_pos] + new_showcase_html + '\n\n  ' + html[end_pos:]
        print("Fallback replacement done!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html with teacher profile photo and academy branding!")
