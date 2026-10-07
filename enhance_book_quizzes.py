# -*- coding: utf-8 -*-
"""
Add textbook quiz cards with data-type="book" and filter button to quiz-wrap-u6-l2
"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Filter buttons update
old_filters = """      <div class="quiz-filters">
        <button type="button" class="quiz-filter-btn active" onclick="filterQuiz('u6-l2', 'all', this)">⭐ جميع الأسئلة (8)</button>
        <button type="button" class="quiz-filter-btn" onclick="filterQuiz('u6-l2', 'mcq', this)">🔘 اختيار من متعدد</button>
        <button type="button" class="quiz-filter-btn" onclick="filterQuiz('u6-l2', 'tf', this)">✔️ صح أو خطأ</button>
        <button type="button" class="quiz-filter-btn" onclick="filterQuiz('u6-l2', 'term', this)">🏷️ مصطلحات وأكمل</button>
        <button type="button" class="quiz-filter-btn" onclick="filterQuiz('u6-l2', 'ministry', this)">📋 تقييمات الوزارة والواجبات</button>
      </div>"""

new_filters = """      <div class="quiz-filters">
        <button type="button" class="quiz-filter-btn active" onclick="filterQuiz('u6-l2', 'all', this)">⭐ جميع الأسئلة (14)</button>
        <button type="button" class="quiz-filter-btn" onclick="filterQuiz('u6-l2', 'mcq', this)">🔘 اختيار من متعدد</button>
        <button type="button" class="quiz-filter-btn" onclick="filterQuiz('u6-l2', 'tf', this)">✔️ صح أو خطأ</button>
        <button type="button" class="quiz-filter-btn" onclick="filterQuiz('u6-l2', 'term', this)">🏷️ مصطلحات وأكمل</button>
        <button type="button" class="quiz-filter-btn" onclick="filterQuiz('u6-l2', 'ministry', this)">📋 تقييمات الوزارة والواجبات</button>
        <button type="button" class="quiz-filter-btn" onclick="filterQuiz('u6-l2', 'book', this)">📖 تدريبات كتاب المدرسة</button>
      </div>"""

if old_filters in html:
    html = html.replace(old_filters, new_filters)

# Add interactive book cards inside qlist-u6-l2
book_q_cards = """
        <!-- Book Question 1: Dice -->
        <div class="q-card" data-type="book" id="q-u6-l2-9">
          <div class="q-head">
            <span class="q-badge book" style="background:rgba(168,85,247,0.18);color:#d8b4fe;border:1px solid rgba(168,85,247,0.35);">📖 كتاب المدرسة • ص65</span>
            <div class="q-text"><b>س9 (تحدي معلوماتك - كتاب المدرسة):</b> كم من bit مطلوب لتمثيل جميع النتائج الممكنة عند رمي نردين؟</div>
          </div>
          <div class="q-options">
            <button type="button" class="quiz-btn" data-correct="true" onclick="checkOption(this, 'u6-l2', '9', 'نردين = 6 × 6 = 36 احتمالاً. 5 بت تعطي 32 احتمالاً (لا تكفي)، أما 6 بت فتعطي 64 احتمالاً (تكفي وتغطي كافة النتائج).')"><span>أ) 6 bits (6 بت)</span> <span class="opt-icon"></span></button>
            <button type="button" class="quiz-btn" data-correct="false" onclick="checkOption(this, 'u6-l2', '9', 'نردين = 6 × 6 = 36 احتمالاً. 5 بت تعطي 32 احتمالاً (لا تكفي)، أما 6 بت فتعطي 64 احتمالاً (تكفي وتغطي كافة النتائج).')"><span>ب) 5 bits</span> <span class="opt-icon"></span></button>
            <button type="button" class="quiz-btn" data-correct="false" onclick="checkOption(this, 'u6-l2', '9', 'نردين = 6 × 6 = 36 احتمالاً. 5 بت تعطي 32 احتمالاً (لا تكفي)، أما 6 بت فتعطي 64 احتمالاً (تكفي وتغطي كافة النتائج).')"><span>ج) 8 bits</span> <span class="opt-icon"></span></button>
            <button type="button" class="quiz-btn" data-correct="false" onclick="checkOption(this, 'u6-l2', '9', 'نردين = 6 × 6 = 36 احتمالاً. 5 بت تعطي 32 احتمالاً (لا تكفي)، أما 6 بت فتعطي 64 احتمالاً (تكفي وتغطي كافة النتائج).')"><span>د) 12 bits</span> <span class="opt-icon"></span></button>
          </div>
          <div class="q-feedback" id="feedback-u6-l2-9"></div>
        </div>

        <!-- Book Question 2: Bytes in 1MB -->
        <div class="q-card" data-type="book" id="q-u6-l2-10">
          <div class="q-head">
            <span class="q-badge book" style="background:rgba(168,85,247,0.18);color:#d8b4fe;border:1px solid rgba(168,85,247,0.35);">📖 كتاب المدرسة • ص65</span>
            <div class="q-text"><b>س10 (تحدي معلوماتك - كتاب المدرسة):</b> كم Byte يوجد في [ 1 MB ] معبرًا عنه على شكل أس للعدد 2؟</div>
          </div>
          <div class="q-options">
            <button type="button" class="quiz-btn" data-correct="true" onclick="checkOption(this, 'u6-l2', '10', '1 KB = 2¹⁰ B، و 1 MB = 1024 KB = 2¹⁰ × 2¹⁰ = 2²⁰ Byte.')"><span>أ) 2²⁰ Byte (2 أس 20 بايت)</span> <span class="opt-icon"></span></button>
            <button type="button" class="quiz-btn" data-correct="false" onclick="checkOption(this, 'u6-l2', '10', '1 KB = 2¹⁰ B، و 1 MB = 1024 KB = 2¹⁰ × 2¹⁰ = 2²⁰ Byte.')"><span>ب) 2¹⁰ Byte</span> <span class="opt-icon"></span></button>
            <button type="button" class="quiz-btn" data-correct="false" onclick="checkOption(this, 'u6-l2', '10', '1 KB = 2¹⁰ B، و 1 MB = 1024 KB = 2¹⁰ × 2¹⁰ = 2²⁰ Byte.')"><span>ج) 2³⁰ Byte</span> <span class="opt-icon"></span></button>
            <button type="button" class="quiz-btn" data-correct="false" onclick="checkOption(this, 'u6-l2', '10', '1 KB = 2¹⁰ B، و 1 MB = 1024 KB = 2¹⁰ × 2¹⁰ = 2²⁰ Byte.')"><span>د) 2⁸ Byte</span> <span class="opt-icon"></span></button>
          </div>
          <div class="q-feedback" id="feedback-u6-l2-10"></div>
        </div>

        <!-- Book Question 3: 4bit vs 2bit -->
        <div class="q-card" data-type="book" id="q-u6-l2-11">
          <div class="q-head">
            <span class="q-badge book" style="background:rgba(168,85,247,0.18);color:#d8b4fe;border:1px solid rgba(168,85,247,0.35);">📖 كتاب المدرسة • ص65</span>
            <div class="q-text"><b>س11 (تحدي معلوماتك - كتاب المدرسة):</b> كم مرة تكون 4 bit من البيانات أكبر مقارنة بـ 2 bit من البيانات؟</div>
          </div>
          <div class="q-options">
            <button type="button" class="quiz-btn" data-correct="true" onclick="checkOption(this, 'u6-l2', '11', 'كمية بيانات 4 بت = 2⁴ = 16، وكمية بيانات 2 بت = 2² = 4. إذن 16 ÷ 4 = 4 مرات.')"><span>أ) 4 مرات (تزيد بمقدار 4 أضعاف)</span> <span class="opt-icon"></span></button>
            <button type="button" class="quiz-btn" data-correct="false" onclick="checkOption(this, 'u6-l2', '11', 'كمية بيانات 4 بت = 2⁴ = 16، وكمية بيانات 2 بت = 2² = 4. إذن 16 ÷ 4 = 4 مرات.')"><span>ب) مرتان</span> <span class="opt-icon"></span></button>
            <button type="button" class="quiz-btn" data-correct="false" onclick="checkOption(this, 'u6-l2', '11', 'كمية بيانات 4 بت = 2⁴ = 16، وكمية بيانات 2 بت = 2² = 4. إذن 16 ÷ 4 = 4 مرات.')"><span>ج) 8 مرات</span> <span class="opt-icon"></span></button>
            <button type="button" class="quiz-btn" data-correct="false" onclick="checkOption(this, 'u6-l2', '11', 'كمية بيانات 4 بت = 2⁴ = 16، وكمية بيانات 2 بت = 2² = 4. إذن 16 ÷ 4 = 4 مرات.')"><span>د) 16 مرة</span> <span class="opt-icon"></span></button>
          </div>
          <div class="q-feedback" id="feedback-u6-l2-11"></div>
        </div>

        <!-- Book Question 4: DVD Problem -->
        <div class="q-card" data-type="book" id="q-u6-l2-12">
          <div class="q-head">
            <span class="q-badge book" style="background:rgba(168,85,247,0.18);color:#d8b4fe;border:1px solid rgba(168,85,247,0.35);">📖 كتاب المدرسة • ص67</span>
            <div class="q-text"><b>س12 (تمرين الكتاب المدرسي):</b> كم عدد أقراص DVD بسعة 4.7 GB التي يمكن تخزينها على قرص صلب بسعة 1 تيرابايت 1 TB (مقرباً لأقرب عدد صحيح)؟</div>
          </div>
          <div class="q-options">
            <button type="button" class="quiz-btn" data-correct="true" onclick="checkOption(this, 'u6-l2', '12', '1 TB = 1024 GB. عدد الأقراص = 1024 ÷ 4.7 = 217.87 ≈ 218 قرص DVD.')"><span>أ) 218 قرص DVD (أو 217 قرصاً كاملاً)</span> <span class="opt-icon"></span></button>
            <button type="button" class="quiz-btn" data-correct="false" onclick="checkOption(this, 'u6-l2', '12', '1 TB = 1024 GB. عدد الأقراص = 1024 ÷ 4.7 = 217.87 ≈ 218 قرص DVD.')"><span>ب) 100 قرص DVD</span> <span class="opt-icon"></span></button>
            <button type="button" class="quiz-btn" data-correct="false" onclick="checkOption(this, 'u6-l2', '12', '1 TB = 1024 GB. عدد الأقراص = 1024 ÷ 4.7 = 217.87 ≈ 218 قرص DVD.')"><span>ج) 512 قرص DVD</span> <span class="opt-icon"></span></button>
            <button type="button" class="quiz-btn" data-correct="false" onclick="checkOption(this, 'u6-l2', '12', '1 TB = 1024 GB. عدد الأقراص = 1024 ÷ 4.7 = 217.87 ≈ 218 قرص DVD.')"><span>د) 1024 قرص DVD</span> <span class="opt-icon"></span></button>
          </div>
          <div class="q-feedback" id="feedback-u6-l2-12"></div>
        </div>

        <!-- Book Question 5: USB Flash Images -->
        <div class="q-card" data-type="book" id="q-u6-l2-13">
          <div class="q-head">
            <span class="q-badge book" style="background:rgba(168,85,247,0.18);color:#d8b4fe;border:1px solid rgba(168,85,247,0.35);">📖 كتاب المدرسة • ص67</span>
            <div class="q-text"><b>س13 (مسألة الكتاب المدرسي):</b> كم عدد الصور، حجم كل منها 2 MB، التي يمكن تخزينها على محرك أقراص فلاش USB بسعة 32 GB؟</div>
          </div>
          <div class="q-options">
            <button type="button" class="quiz-btn" data-correct="true" onclick="checkOption(this, 'u6-l2', '13', '32 GB = 32 × 1024 MB = 32,768 MB. عدد الصور = 32,768 ÷ 2 = 16,384 صورة.')"><span>أ) 16,384 صورة</span> <span class="opt-icon"></span></button>
            <button type="button" class="quiz-btn" data-correct="false" onclick="checkOption(this, 'u6-l2', '13', '32 GB = 32 × 1024 MB = 32,768 MB. عدد الصور = 32,768 ÷ 2 = 16,384 صورة.')"><span>ب) 8,192 صورة</span> <span class="opt-icon"></span></button>
            <button type="button" class="quiz-btn" data-correct="false" onclick="checkOption(this, 'u6-l2', '13', '32 GB = 32 × 1024 MB = 32,768 MB. عدد الصور = 32,768 ÷ 2 = 16,384 صورة.')"><span>ج) 32,000 صورة</span> <span class="opt-icon"></span></button>
            <button type="button" class="quiz-btn" data-correct="false" onclick="checkOption(this, 'u6-l2', '13', '32 GB = 32 × 1024 MB = 32,768 MB. عدد الصور = 32,768 ÷ 2 = 16,384 صورة.')"><span>د) 64,000 صورة</span> <span class="opt-icon"></span></button>
          </div>
          <div class="q-feedback" id="feedback-u6-l2-13"></div>
        </div>

        <!-- Book Question 6: Real world Governorates -->
        <div class="q-card" data-type="book" id="q-u6-l2-14">
          <div class="q-head">
            <span class="q-badge book" style="background:rgba(168,85,247,0.18);color:#d8b4fe;border:1px solid rgba(168,85,247,0.35);">📖 كتاب المدرسة • ص67</span>
            <div class="q-text"><b>س14 (تطبيق الكتاب المدرسي):</b> ما هو الحد الأدنى من الـ bits اللازمة لتمثيل 47 محافظة؟</div>
          </div>
          <div class="q-options">
            <button type="button" class="quiz-btn" data-correct="true" onclick="checkOption(this, 'u6-l2', '14', '2⁵ = 32 (أقل من 47 ولا تكفي)، بينما 2⁶ = 64 (أكبر من 47 وتكفي لكافة المحافظات). إذن الحد الأدنى هو 6 bits.')"><span>أ) 6 bits (6 بت)</span> <span class="opt-icon"></span></button>
            <button type="button" class="quiz-btn" data-correct="false" onclick="checkOption(this, 'u6-l2', '14', '2⁵ = 32 (أقل من 47 ولا تكفي)، بينما 2⁶ = 64 (أكبر من 47 وتكفي لكافة المحافظات). إذن الحد الأدنى هو 6 bits.')"><span>ب) 5 bits</span> <span class="opt-icon"></span></button>
            <button type="button" class="quiz-btn" data-correct="false" onclick="checkOption(this, 'u6-l2', '14', '2⁵ = 32 (أقل من 47 ولا تكفي)، بينما 2⁶ = 64 (أكبر من 47 وتكفي لكافة المحافظات). إذن الحد الأدنى هو 6 bits.')"><span>ج) 7 bits</span> <span class="opt-icon"></span></button>
            <button type="button" class="quiz-btn" data-correct="false" onclick="checkOption(this, 'u6-l2', '14', '2⁵ = 32 (أقل من 47 ولا تكفي)، بينما 2⁶ = 64 (أكبر من 47 وتكفي لكافة المحافظات). إذن الحد الأدنى هو 6 bits.')"><span>د) 4 bits</span> <span class="opt-icon"></span></button>
          </div>
          <div class="q-feedback" id="feedback-u6-l2-14"></div>
        </div>
"""

# Insert inside qlist-u6-l2 right before its closing </div>
target_end = '<!-- ================= SCHOOL TEXTBOOK EXERCISES (PAGES 64 - 67) ================= -->'
# Find q-u6-l2-8 closing div
q8_pos = html.find('id="q-u6-l2-8"')
if q8_pos != -1:
    closing_div_pos = html.find('</div>\n    </div>', q8_pos)
    if 'id="q-u6-l2-9"' not in html:
        html = html[:closing_div_pos] + '</div>\n' + book_q_cards + '\n      ' + html[closing_div_pos:]
        print("Injected book question cards into qlist-u6-l2 successfully!")

# Update score display count in header
html = html.replace('<div class="quiz-score-badge" id="score-u6-l2">🎯 النتيجة: 0 / 6</div>', '<div class="quiz-score-badge" id="score-u6-l2">🎯 النتيجة: 0 / 12</div>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html successfully updated with book questions filter and interactive cards!")
