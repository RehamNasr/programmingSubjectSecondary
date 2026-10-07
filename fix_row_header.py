# -*- coding: utf-8 -*-
"""
Fix video showcase header to be strictly a horizontal row (side-by-side) and clean up CSS
"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix CSS for video-showcase-header and media queries
clean_showcase_css = """
  /* ================= Semicolon Video Showcase (VIP Studio Design) ================= */
  .video-showcase-wrapper {
    margin: 45px 0 50px;
    background: radial-gradient(circle at 50% 10%, #1e162b 0%, #0f0c18 55%, #06040a 100%);
    border: 2px solid rgba(246, 190, 31, 0.5);
    border-radius: 36px;
    padding: 34px 38px 30px;
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

  /* Force Horizontal Row layout for the top header */
  .video-showcase-header {
    display: flex !important;
    flex-direction: row !important;
    align-items: stretch !important;
    justify-content: space-between !important;
    gap: 20px !important;
    margin-bottom: 28px !important;
    position: relative !important;
    z-index: 2 !important;
    width: 100% !important;
  }

  /* Right Side: Teacher Profile Glass Card */
  .profile-hero-card {
    display: flex !important;
    align-items: center !important;
    gap: 16px !important;
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(246, 190, 31, 0.04) 100%) !important;
    border: 1.5px solid rgba(246, 190, 31, 0.4) !important;
    border-radius: 24px !important;
    padding: 14px 22px !important;
    backdrop-filter: blur(16px) !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4), 0 0 20px rgba(246, 190, 31, 0.15) !important;
    flex: 1 1 0 !important;
    min-width: 0 !important;
  }
  .profile-avatar-ring {
    width: 82px;
    height: 82px;
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
    font-size: 26px;
    font-weight: 800;
    color: #ffffff;
    margin: 0;
    text-shadow: 0 2px 14px rgba(0,0,0,0.9), 0 0 25px rgba(246, 190, 31, 0.35);
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
    box-shadow: 0 2px 10px rgba(246, 190, 31, 0.45);
    white-space: nowrap;
  }
  .profile-role {
    font-size: 13.5px;
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

  /* Left Side: Semicolon Academy Branding Card */
  .academy-branding-card {
    display: flex !important;
    flex-direction: column !important;
    align-items: flex-start !important;
    justify-content: center !important;
    gap: 6px !important;
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(215, 38, 56, 0.05) 100%) !important;
    border: 1.5px solid rgba(215, 38, 56, 0.45) !important;
    border-radius: 24px !important;
    padding: 14px 22px !important;
    backdrop-filter: blur(16px) !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4), 0 0 20px rgba(215, 38, 56, 0.18) !important;
    flex: 1 1 0 !important;
    min-width: 0 !important;
    text-align: right !important;
  }
  .academy-logo-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(215, 38, 56, 0.2);
    border: 1.5px solid rgba(215, 38, 56, 0.55);
    padding: 4px 14px;
    border-radius: 30px;
    box-shadow: 0 0 20px rgba(215, 38, 56, 0.35);
  }
  .semicolon-symbol {
    font-family: 'Exo 2', monospace;
    font-size: 20px;
    font-weight: 900;
    color: #ff3344;
    text-shadow: 0 0 12px #ff3344;
    line-height: 1;
  }
  .academy-brand-text {
    font-family: 'Exo 2', sans-serif;
    font-size: 14px;
    font-weight: 900;
    letter-spacing: 2px;
    color: #ffffff;
    text-transform: uppercase;
  }
  .academy-arabic-name {
    font-family: 'The Year of Handicrafts', 'Cairo', sans-serif;
    font-size: 16px;
    font-weight: 800;
    color: #f6be1f;
    text-shadow: 0 2px 10px rgba(0,0,0,0.7);
    white-space: nowrap;
  }
  .grade-unit-badge {
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.18);
    color: #f1f5f9;
    font-size: 12px;
    font-weight: 700;
    padding: 4px 12px;
    border-radius: 20px;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    white-space: nowrap;
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

# Replace all old showcase CSS completely from /* ================= Semicolon Video Showcase to /* ================= School Textbook Exercises Component
old_css_full_block = r'/\* ================= Semicolon Video Showcase.*?/\* ================= School Textbook Exercises Component ================= \*/'
if re.search(old_css_full_block, html, flags=re.DOTALL):
    html = re.sub(old_css_full_block, clean_showcase_css + '\n\n  /* ================= School Textbook Exercises Component ================= */', html, flags=re.DOTALL)
    print("Replaced full showcase CSS block successfully!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html successfully!")
