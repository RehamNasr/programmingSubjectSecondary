# -*- coding: utf-8 -*-
"""
Robust generator for index.html with all Mind Maps and Interactive Quizzes.
"""
import re
import json

# Import quiz data and mind map blocks
from run_update import quizzes_data, generate_quiz_html
from update_all_curriculum import mindmap_blocks

with open('خريطة_ذهنية_الوحدة_الثانية (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Clean old details.qbank
html = re.sub(r'\s*<details class="qbank">.*?</details>', '', html, flags=re.DOTALL)

# 2. Inject Quiz Engine CSS
quiz_css = """

  /* ================= Semicolon Video Showcase (Laptop Frame) ================= */
  .video-showcase-wrapper {
    margin: 50px 0 45px;
    background: radial-gradient(circle at 50% 20%, #1c1524 0%, #0c0910 80%, #050407 100%);
    border: 1.5px solid rgba(215, 38, 56, 0.45);
    border-radius: 32px;
    padding: 36px 40px;
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4), 0 0 40px rgba(215, 38, 56, 0.12);
    color: #ffffff;
    position: relative;
    overflow: hidden;
  }
  .video-showcase-wrapper::before {
    content: "";
    position: absolute;
    top: 0; right: 0; bottom: 0; left: 0;
    background: repeating-linear-gradient(0deg, rgba(255,255,255,0.015) 0px, rgba(255,255,255,0.015) 1px, transparent 1px, transparent 24px);
    pointer-events: none;
  }
  .video-showcase-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    flex-wrap: wrap;
    margin-bottom: 30px;
    position: relative;
    z-index: 2;
  }
  .eng-title {
    font-family: 'The Year of Handicrafts', 'Cairo', sans-serif;
    font-size: 30px;
    font-weight: 800;
    color: #ffffff;
    text-shadow: 0 2px 10px rgba(0,0,0,0.7);
    letter-spacing: 0.5px;
  }
  .academy-brand {
    text-align: left;
  }
  .brand-badge {
    font-family: 'Exo 2', sans-serif;
    font-size: 13.5px;
    font-weight: 800;
    color: #e63946;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 4px;
    text-shadow: 0 0 12px rgba(230, 57, 70, 0.4);
  }
  .grade-title {
    font-family: 'Cairo', sans-serif;
    font-size: 16px;
    font-weight: 700;
    color: #f1faee;
    text-align: left;
  }

  /* Laptop Mockup Styles */
  .laptop-mockup-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 20px 0 35px;
    position: relative;
    z-index: 2;
  }
  .laptop-device {
    width: 100%;
    max-width: 820px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .laptop-lid {
    width: 100%;
    background: #111018;
    border: 3px solid #323040;
    border-bottom: none;
    border-radius: 20px 20px 4px 4px;
    padding: 12px 14px 16px;
    box-shadow: 0 -8px 30px rgba(0,0,0,0.6), inset 0 1px 2px rgba(255,255,255,0.15);
    position: relative;
  }
  .laptop-camera {
    width: 6px;
    height: 6px;
    background: #050508;
    border: 1px solid #4a485a;
    border-radius: 50%;
    margin: 0 auto 10px;
    box-shadow: 0 0 3px rgba(255,255,255,0.2);
  }
  .laptop-screen {
    position: relative;
    width: 100%;
    padding-bottom: 56.25%; /* 16:9 Aspect Ratio */
    background: #000000;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: inset 0 0 10px rgba(0,0,0,0.8);
  }
  .laptop-screen iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border: 0;
  }
  .laptop-base {
    width: 116%;
    height: 22px;
    background: linear-gradient(to bottom, #444254 0%, #2b2938 40%, #1a1824 100%);
    border-radius: 4px 4px 24px 24px;
    box-shadow: 0 20px 45px rgba(0, 0, 0, 0.8), 0 4px 12px rgba(0, 0, 0, 0.5);
    position: relative;
    display: flex;
    justify-content: center;
  }
  .laptop-notch {
    width: 90px;
    height: 6px;
    background: #181720;
    border-radius: 0 0 6px 6px;
    box-shadow: inset 0 1px 2px rgba(0,0,0,0.7);
  }

  /* Bottom Footer & Contacts */
  .video-showcase-footer {
    display: flex;
    align-items: center;
    gap: 16px;
    margin-top: 15px;
    flex-wrap: wrap;
    position: relative;
    z-index: 2;
  }
  .contact-pill {
    display: inline-flex;
    align-items: center;
    gap: 12px;
    background: rgba(255, 255, 255, 0.04);
    border: 1.5px solid rgba(255, 255, 255, 0.45);
    border-radius: 50px;
    padding: 6px 20px 6px 10px;
    backdrop-filter: blur(10px);
    transition: all 0.3s ease;
  }
  .contact-pill:hover {
    border-color: #e63946;
    background: rgba(230, 57, 70, 0.1);
    transform: translateY(-2px);
  }
  .phone-icon-circle {
    width: 32px;
    height: 32px;
    background: #d72638;
    color: #ffffff;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 2px 8px rgba(215, 38, 56, 0.5);
  }
  .phone-numbers {
    font-family: 'Exo 2', 'Cairo', sans-serif;
    font-size: 15px;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: 1px;
    direction: ltr;
  }
  .footer-divider-line {
    flex: 1;
    min-width: 40px;
    height: 1.5px;
    background: linear-gradient(90deg, rgba(255,255,255,0.4) 0%, rgba(255,255,255,0.05) 100%);
    border-radius: 2px;
  }
  .yt-direct-btn {
    font-family: 'Cairo', sans-serif;
    font-size: 13.5px;
    font-weight: 800;
    color: #ffffff;
    background: linear-gradient(135deg, #d72638 0%, #a01120 100%);
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 30px;
    padding: 8px 22px;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    box-shadow: 0 4px 15px rgba(215, 38, 56, 0.4);
    transition: all 0.25s ease;
  }
  .yt-direct-btn:hover {
    transform: translateY(-2px) scale(1.03);
    box-shadow: 0 6px 20px rgba(215, 38, 56, 0.6);
    color: #ffffff;
  }

  @media (max-width: 768px) {
    .video-showcase-wrapper {
      padding: 24px 20px;
      border-radius: 24px;
    }
    .video-showcase-header {
      flex-direction: column;
      align-items: flex-start;
      gap: 12px;
    }
    .eng-title { font-size: 24px; }
    .laptop-base { width: 108%; }
    .contact-pill { width: 100%; justify-content: center; padding: 6px 14px; }
    .footer-divider-line { display: none; }
    .yt-direct-btn { width: 100%; justify-content: center; }
  }


  /* ================= Interactive Lesson Quiz & Assessment Engine ================= */
  .lesson-quiz-wrap {
    margin-top: 40px;
    margin-bottom: 30px;
    background: var(--bg-card);
    border: 1.5px solid var(--border-card);
    border-radius: 24px;
    padding: 28px 30px;
    box-shadow: var(--shadow-md);
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;
  }
  .lesson-quiz-wrap:hover {
    box-shadow: var(--shadow-lg);
    border-color: var(--brand-gold);
  }
  .quiz-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    flex-wrap: wrap;
    padding-bottom: 20px;
    border-bottom: 2px dashed var(--border-sub);
    margin-bottom: 22px;
  }
  .quiz-title-box h3 {
    font-family: 'Cairo', sans-serif;
    font-weight: 900;
    font-size: 19px;
    margin: 0 0 4px;
    color: var(--text-primary);
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .quiz-title-box p {
    margin: 0;
    font-size: 13px;
    color: var(--text-muted);
  }
  .quiz-header-actions {
    display: flex;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
  }
  .quiz-score-badge {
    font-family: 'Exo 2', 'Cairo', sans-serif;
    font-weight: 800;
    font-size: 14px;
    background: var(--brand-gold-light);
    color: var(--brand-gold-deep);
    border: 1.5px solid var(--brand-gold-border);
    padding: 6px 16px;
    border-radius: 30px;
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }
  .quiz-reset-btn {
    font-family: 'Cairo', sans-serif;
    font-size: 12.5px;
    font-weight: 700;
    color: var(--text-primary);
    background: var(--bg-card-sub);
    border: 1px solid var(--border-sub);
    padding: 6px 14px;
    border-radius: 20px;
    cursor: pointer;
    transition: all 0.2s ease;
  }
  .quiz-reset-btn:hover {
    background: var(--brand-red);
    color: #fff;
    border-color: var(--brand-red);
  }
  .quiz-filters {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-bottom: 22px;
  }
  .quiz-filter-btn {
    font-family: 'Cairo', sans-serif;
    font-weight: 700;
    font-size: 12.5px;
    padding: 6px 16px;
    border-radius: 20px;
    border: 1px solid var(--border-sub);
    background: var(--bg-card-sub);
    color: var(--text-secondary);
    cursor: pointer;
    transition: all 0.2s ease;
  }
  .quiz-filter-btn.active, .quiz-filter-btn:hover {
    background: linear-gradient(135deg, var(--brand-red) 0%, var(--brand-red-deep) 100%);
    color: #fff;
    border-color: var(--brand-red);
    box-shadow: 0 2px 8px rgba(215,38,56,0.3);
  }
  .q-card {
    background: var(--bg-card-sub);
    border: 1.5px solid var(--border-sub);
    border-radius: 18px;
    padding: 18px 22px;
    margin-bottom: 16px;
    transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  }
  .q-card:hover {
    border-color: var(--border-card);
  }
  .q-card.answered-correct {
    border-color: var(--brand-emerald) !important;
    background: var(--brand-emerald-light) !important;
  }
  .q-card.answered-wrong {
    border-color: var(--brand-red) !important;
    background: var(--brand-red-light) !important;
  }
  .q-head {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    margin-bottom: 12px;
  }
  .q-badge {
    font-size: 11px;
    font-weight: 800;
    font-family: 'Cairo', sans-serif;
    padding: 3px 10px;
    border-radius: 6px;
    flex-shrink: 0;
  }
  .q-badge.mcq { background: var(--brand-gold); color: #16141e; }
  .q-badge.tf { background: var(--brand-emerald); color: #fff; }
  .q-badge.term { background: var(--blue); color: #fff; }
  .q-badge.ministry { background: var(--brand-red); color: #fff; }
  .q-text {
    font-family: 'Cairo', sans-serif;
    font-weight: 700;
    font-size: 14.5px;
    color: var(--text-primary);
    line-height: 1.6;
    flex: 1;
  }
  .q-options {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 12px;
  }
  @media (max-width: 680px) {
    .q-options { grid-template-columns: 1fr; }
  }
  .quiz-btn {
    font-family: 'Tajawal', 'Cairo', sans-serif;
    font-size: 13.5px;
    font-weight: 600;
    color: var(--text-primary);
    background: var(--bg-card);
    border: 1.5px solid var(--border-sub);
    border-radius: 12px;
    padding: 10px 16px;
    text-align: right;
    cursor: pointer;
    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 8px;
    user-select: none;
  }
  .quiz-btn:hover:not(:disabled) {
    border-color: var(--brand-gold);
    transform: translateY(-2px);
    box-shadow: var(--shadow-sm);
  }
  .quiz-btn.correct {
    background: var(--brand-emerald) !important;
    color: #ffffff !important;
    border-color: var(--brand-emerald) !important;
    font-weight: 800;
    box-shadow: 0 4px 14px rgba(27,135,102,0.4);
  }
  .quiz-btn.wrong {
    background: var(--brand-red) !important;
    color: #ffffff !important;
    border-color: var(--brand-red) !important;
    font-weight: 800;
    animation: shake 0.35s ease;
  }
  @keyframes shake {
    0%, 100% { transform: translateX(0); }
    20%, 60% { transform: translateX(-6px); }
    40%, 80% { transform: translateX(6px); }
  }
  .q-feedback {
    margin-top: 12px;
    padding: 10px 16px;
    border-radius: 10px;
    font-size: 13px;
    line-height: 1.6;
    display: none;
    font-weight: 600;
  }
  .q-feedback.show { display: block; }
  .q-feedback.correct {
    background: rgba(27,135,102,0.14);
    color: var(--brand-emerald);
    border: 1px solid var(--brand-emerald-border);
  }
  .q-feedback.wrong {
    background: rgba(215,38,56,0.12);
    color: var(--brand-red);
    border: 1px solid var(--brand-red-border);
  }
  .written-ans-toggle {
    margin-top: 10px;
    font-family: 'Cairo', sans-serif;
    font-weight: 700;
    font-size: 12.5px;
    color: var(--brand-gold-deep);
    background: var(--brand-gold-light);
    border: 1px solid var(--brand-gold-border);
    border-radius: 8px;
    padding: 6px 14px;
    cursor: pointer;
    transition: all 0.2s ease;
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }
  .written-ans-toggle:hover {
    background: var(--brand-gold);
    color: #16141e;
  }
  .written-ans-box {
    margin-top: 10px;
    background: var(--bg-card);
    border: 1.5px solid var(--border-card);
    border-radius: 12px;
    padding: 12px 16px;
    font-size: 13px;
    line-height: 1.7;
    color: var(--text-primary);
    display: none;
  }
  .written-ans-box.show { display: block; }
"""

if '.lesson-quiz-wrap' not in html:
    html = html.replace('</style>', quiz_css + '\n</style>')

# 3. Update Print styles for all lessons
new_print_css = """      body[data-print-target="u1-l1"] #u1-l1,
      body[data-print-target="u1-l2"] #u1-l2,
      body[data-print-target="u2-l1"] #u2-l1,
      body[data-print-target="u2-l2"] #u2-l2,
      body[data-print-target="u2-l3"] #u2-l3,
      body[data-print-target="u3-l1"] #u3-l1,
      body[data-print-target="u3-l2"] #u3-l2,
      body[data-print-target="u3-l3"] #u3-l3,
      body[data-print-target="u3-l4"] #u3-l4,
      body[data-print-target="u3-l5"] #u3-l5,
      body[data-print-target="u6-l2"] #u6-l2,
      body[data-print-target="u6-l3"] #u6-l3,
      body[data-print-target="u6-l4"] #u6-l4,
      body[data-print-target="u6-l5"] #u6-l5,
      body[data-print-target="u6-l6"] #u6-l6,
      body[data-print-target="u6-l8"] #u6-l8,
      body[data-print-target="u6-l10"] #u6-l10 {"""

html = re.sub(r'body\[data-print-target="u1-l1"\] #u1-l1,.*?body\[data-print-target="u6-l4"\] #u6-l4 \{', new_print_css, html, flags=re.DOTALL)

# 4. Update TOC for Unit 3 & Unit 6
new_toc_u3 = """    <div class="toc-unit">
      <div class="toc-unit-title"><a href="#unit3">🛡️ الوحدة الثالثة: أمن المعلومات</a></div>
      <ul class="toc-lessons">
        <li class="included"><a href="#u3-l1">الدرس 1: تهديدات وإجراءات مواجهة أمن المعلومات (1)</a></li>
        <li class="included"><a href="#u3-l2">الدرس 2: التهديدات والتدابير المضادة في أمن المعلومات (2)</a></li>
        <li class="included"><a href="#u3-l3">الدرس 3: التهديدات والتدابير المضادة في أمن المعلومات (3)</a></li>
        <li class="included"><a href="#u3-l4">الدرس 4: تقنيات المعلومات للسلامة (1) — التشفير</a></li>
        <li class="included"><a href="#u3-l5">الدرس 5: تقنيات المعلومات للسلامة (2) — التوقيع الرقمي و SSL/TLS</a></li>
      </ul>
    </div>"""

html = re.sub(r'<div class="toc-unit">\s*<div class="toc-unit-title"><a href="#unit3">🛡️ الوحدة الثالثة: أمن المعلومات</a></div>.*?</ul>\s*</div>', new_toc_u3, html, flags=re.DOTALL)

new_toc_u6 = """    <div class="toc-unit">
      <div class="toc-unit-title"><a href="#unit6">🔢 الوحدة السادسة: تصميم المعلومات</a></div>
      <ul class="toc-lessons">
        <li class="included"><a href="#u6-l2">الدرس 2: النظام الثنائي وكمية البيانات</a></li>
        <li class="included"><a href="#u6-l3">الدرس 3: النظام السادس عشر (Hexadecimal)</a></li>
        <li class="included"><a href="#u6-l4">الدرس 4: التمثيل الرقمي للأحرف</a></li>
        <li class="included"><a href="#u6-l5">الدرس 5: العمليات الحسابية العددية (1) — الجمع والطرح الثنائي</a></li>
        <li class="included"><a href="#u6-l6">الدرس 6: العمليات الحسابية العددية (2) — المكملات وتمثيل الأعداد السالبة</a></li>
        <li class="included"><a href="#u6-l8">الدرس 8: التمثيل الرقمي للصور</a></li>
        <li class="included"><a href="#u6-l10">الدرس 10: تصميم المعلومات والتصميم الشامل</a></li>
      </ul>
    </div>"""

html = re.sub(r'<div class="toc-unit">\s*<div class="toc-unit-title"><a href="#unit6">🔢 الوحدة السادسة: تصميم المعلومات</a></div>.*?</ul>\s*</div>', new_toc_u6, html, flags=re.DOTALL)

# 5. Split by lesson blocks and inject quizzes precisely
# Let's find each lesson block in original html
lesson_ids = ['u1-l1', 'u1-l2', 'u2-l1', 'u2-l2', 'u2-l3', 'u3-l1', 'u3-l2', 'u3-l3', 'u6-l2', 'u6-l3', 'u6-l4']

# For each existing lesson block, we find where it ends (before next lesson block or unit title)
# A reliable way: find `<div class="lesson-block" id="{id}">` and the subsequent next `<div class="lesson-block"` or `<div class="unit-title"` or `<footer>`
for l_id in lesson_ids:
    if l_id in quizzes_data:
        quiz_html = generate_quiz_html(l_id, quizzes_data[l_id])
        
        # Look for the lesson block in html
        pattern = rf'(<div class="lesson-block" id="{l_id}">.*?)(\s*<!-- =================== UNIT|\s*<div class="unit-title"|\s*<div class="lesson-block"|\s*<footer>|\s*<script|\Z)'
        m = re.search(pattern, html, flags=re.DOTALL)
        if m:
            block_content = m.group(1).rstrip()
            rest = m.group(2)
            html = html[:m.start(1)] + block_content + "\n" + quiz_html + "\n" + rest + html[m.end():]
            print(f"Quiz injected for {l_id}")

# 6. Insert new lessons:
# Unit 3: u3-l4 and u3-l5 after u3-l3's quiz wrap
u3_l4_full = mindmap_blocks["u3-l4"] + "\n" + generate_quiz_html("u3-l4", quizzes_data["u3-l4"])
u3_l5_full = mindmap_blocks["u3-l5"] + "\n" + generate_quiz_html("u3-l5", quizzes_data["u3-l5"])

target_u3 = 'id="quiz-wrap-u3-l3"'
idx_u3 = html.find(target_u3)
if idx_u3 != -1:
    # Find the end of quiz-wrap-u3-l3
    # quiz-wrap ends with </div>\n    </div>\n
    m = re.search(r'id="quiz-wrap-u3-l3">.*?</div>\s*</div>', html[idx_u3:], flags=re.DOTALL)
    if m:
        insert_pos = idx_u3 + m.end()
        html = html[:insert_pos] + "\n" + u3_l4_full + "\n" + u3_l5_full + "\n" + html[insert_pos:]
        print("Unit 3 Lessons 4 & 5 inserted.")

# Unit 6: u6-l5, u6-l6, u6-l8, u6-l10 after u6-l4's quiz wrap
u6_l5_full = mindmap_blocks["u6-l5"] + "\n" + generate_quiz_html("u6-l5", quizzes_data["u6-l5"])
u6_l6_full = mindmap_blocks["u6-l6"] + "\n" + generate_quiz_html("u6-l6", quizzes_data["u6-l6"])
u6_l8_full = mindmap_blocks["u6-l8"] + "\n" + generate_quiz_html("u6-l8", quizzes_data["u6-l8"])
u6_l10_full = mindmap_blocks["u6-l10"] + "\n" + generate_quiz_html("u6-l10", quizzes_data["u6-l10"])

target_u6 = 'id="quiz-wrap-u6-l4"'
idx_u6 = html.find(target_u6)
if idx_u6 != -1:
    m = re.search(r'id="quiz-wrap-u6-l4">.*?</div>\s*</div>', html[idx_u6:], flags=re.DOTALL)
    if m:
        insert_pos = idx_u6 + m.end()
        html = html[:insert_pos] + "\n" + u6_l5_full + "\n" + u6_l6_full + "\n" + u6_l8_full + "\n" + u6_l10_full + "\n" + html[insert_pos:]
        print("Unit 6 Lessons 5, 6, 8, 10 inserted.")

# 7. Inject Quiz Engine JavaScript before </body>
quiz_js = """
  <script>
    // Global state for quiz scores
    var quizScores = {};

    function updateScoreDisplay(lessonId) {
      var badge = document.getElementById('score-' + lessonId);
      if (!badge) return;
      var score = quizScores[lessonId] || 0;
      var total = document.querySelectorAll('#qlist-' + lessonId + ' .q-card[data-type="mcq"], #qlist-' + lessonId + ' .q-card[data-type="tf"]').length;
      badge.innerHTML = '🎯 النتيجة: ' + score + ' / ' + total;
      if (score === total && total > 0) {
        badge.style.background = 'var(--brand-emerald)';
        badge.style.color = '#fff';
      }
    }

    function checkOption(btn, lessonId, qNum, expText) {
      var card = document.getElementById('q-' + lessonId + '-' + qNum);
      if (!card) return;

      var buttons = card.querySelectorAll('.quiz-btn');
      var isAlreadyAnswered = card.classList.contains('answered-correct') || card.classList.contains('answered-wrong');
      if (isAlreadyAnswered) return;

      var isCorrect = btn.getAttribute('data-correct') === 'true';

      buttons.forEach(function (b) {
        b.disabled = true;
        var bIsCorrect = b.getAttribute('data-correct') === 'true';
        var icon = b.querySelector('.opt-icon');
        if (bIsCorrect) {
          b.classList.add('correct');
          if (icon) icon.innerHTML = '✔️';
        } else if (b === btn && !isCorrect) {
          b.classList.add('wrong');
          if (icon) icon.innerHTML = '❌';
        }
      });

      var feedback = document.getElementById('feedback-' + lessonId + '-' + qNum);
      if (feedback) {
        feedback.classList.add('show');
        if (isCorrect) {
          card.classList.add('answered-correct');
          feedback.classList.add('correct');
          feedback.innerHTML = '🎉 <b>إجابة صحيحة وممتازة!</b> ' + (expText ? '— ' + expText : '');
          if (!quizScores[lessonId]) quizScores[lessonId] = 0;
          quizScores[lessonId]++;
        } else {
          card.classList.add('answered-wrong');
          feedback.classList.add('wrong');
          feedback.innerHTML = '💡 <b>إجابة غير صحيحة!</b> ' + (expText ? '— ' + expText : '');
        }
      }

      updateScoreDisplay(lessonId);
    }

    function resetQuiz(lessonId) {
      quizScores[lessonId] = 0;
      var wrap = document.getElementById('quiz-wrap-' + lessonId);
      if (!wrap) return;

      wrap.querySelectorAll('.q-card').forEach(function (card) {
        card.classList.remove('answered-correct', 'answered-wrong');
        card.querySelectorAll('.quiz-btn').forEach(function (b) {
          b.disabled = false;
          b.classList.remove('correct', 'wrong');
          var icon = b.querySelector('.opt-icon');
          if (icon) icon.innerHTML = '';
        });
        var fb = card.querySelector('.q-feedback');
        if (fb) {
          fb.className = 'q-feedback';
          fb.innerHTML = '';
        }
        var wb = card.querySelector('.written-ans-box');
        if (wb) wb.classList.remove('show');
        var btn = card.querySelector('.written-ans-toggle');
        if (btn) {
          if (btn.innerText.includes('توزيع') || btn.innerText.includes('نموذج')) {
            btn.innerHTML = '📋 اعرض نموذج الإجابة وتوزيع الدرجات';
          } else {
            btn.innerHTML = '🔍 اضغط لإظهار الإجابة النموذجية';
          }
        }
      });

      var scoreBadge = document.getElementById('score-' + lessonId);
      if (scoreBadge) {
        scoreBadge.style.background = '';
        scoreBadge.style.color = '';
      }
      updateScoreDisplay(lessonId);
    }

    function filterQuiz(lessonId, category, btn) {
      var wrap = document.getElementById('quiz-wrap-' + lessonId);
      if (!wrap) return;

      wrap.querySelectorAll('.quiz-filter-btn').forEach(function (b) { b.classList.remove('active'); });
      if (btn) btn.classList.add('active');

      wrap.querySelectorAll('.q-card').forEach(function (card) {
        var type = card.getAttribute('data-type');
        if (category === 'all' || type === category) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    }

    function playLaptopVideo() {
      var screen = document.getElementById('laptop-screen-box');
      if (!screen) return;
      screen.innerHTML = '<iframe src="https://www.youtube.com/embed/Vq04T0Cwj5Y?autoplay=1&playsinline=1&rel=0&enablejsapi=1" title="شرح مادة البرمجة والذكاء الاصطناعي - الوحدة السادسة" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="position:absolute; top:0; left:0; width:100%; height:100%; border:0; border-radius:8px;"></iframe>';
    }

    function toggleWrittenAns(btn) {
      var box = btn.nextElementSibling;
      if (box && box.classList.contains('written-ans-box')) {
        var isShown = box.classList.toggle('show');
        if (btn.innerText.includes('توزيع') || btn.innerText.includes('نموذج')) {
          btn.innerHTML = isShown ? '🔒 إخفاء نموذج الإجابة' : '📋 اعرض نموذج الإجابة وتوزيع الدرجات';
        } else {
          btn.innerHTML = isShown ? '🔒 إخفاء الإجابة النموذجية' : '🔍 اضغط لإظهار الإجابة النموذجية';
        }
      }
    }
  </script>
"""

if 'function checkOption' not in html:
    html = html.replace('</body>', quiz_js + '\n</body>')


if '<div class="video-showcase-wrapper">' not in html:
    html = html.replace('<div class="unit-title" id="unit6">', '\n  <!-- =================== SEMICOLON VIDEO SHOWCASE (BEFORE CHAPTER 6) =================== -->\n  <div class="video-showcase-wrapper">\n    <!-- Top Header Bar -->\n    <div class="video-showcase-header">\n      <div class="eng-title">مهندسة : ريهام جمال</div>\n      <div class="academy-brand">\n        <div class="brand-badge">SEMICOLON ACADEMY • PROGRAMMING</div>\n        <div class="grade-title">الصف الأول بكالوريا - برمجة وذكاء اصطناعي</div>\n      </div>\n    </div>\n\n    <!-- Laptop Mockup Frame -->\n    <div class="laptop-mockup-container">\n      <div class="laptop-device">\n        <!-- Screen Lid -->\n        <div class="laptop-lid">\n          <div class="laptop-camera"></div>\n          <div class="laptop-screen">\n            <iframe \n              src="https://www.youtube.com/embed/Vq04T0Cwj5Y?si=KyYGll2W0k41Kh0h&rel=0" \n              title="شرح مادة البرمجة والذكاء الاصطناعي - الوحدة السادسة" \n              frameborder="0" \n              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" \n              allowfullscreen>\n            </iframe>\n          </div>\n        </div>\n        <!-- Laptop Base / Keyboard deck -->\n        <div class="laptop-base">\n          <div class="laptop-notch"></div>\n        </div>\n      </div>\n    </div>\n\n    <!-- Bottom Footer Bar with Phone & Link -->\n    <div class="video-showcase-footer">\n      <div class="contact-pill">\n        <div class="phone-icon-circle">\n          <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">\n            <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>\n          </svg>\n        </div>\n        <span class="phone-numbers">01158659437 - 01221315065</span>\n      </div>\n      <div class="footer-divider-line"></div>\n      <a href="https://youtu.be/Vq04T0Cwj5Y?si=KyYGll2W0k41Kh0h" target="_self" class="yt-direct-btn">\n        <span>▶️ شاهد الشرح على YouTube</span>\n      </a>\n    </div>\n  </div>\n' + '

  <div class="unit-title" id="unit6">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html completely regenerated and saved successfully!")
