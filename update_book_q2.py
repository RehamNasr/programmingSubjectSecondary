# -*- coding: utf-8 -*-
"""
Update Textbook Question 2 (Unit Order) with full options and separate all exercises in index.html
"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the grouped Exercise 4 card in pane-exercises-u6-l2 with distinct, detailed cards
old_pane_section = """      <!-- Exercise 4: Unit Order & Real-life Questions -->
      <div class="book-card">
        <div class="book-card-head">
          <span class="book-q-tag">تمرين الكتاب • أسئلة متنوعة وتحويلات</span>
          <span class="book-page-ref">كتاب الوزارة ص 67</span>
        </div>
        <div class="book-q-text">
          <b>(2) اختر خياراً واحداً يمثل الترتيب الصحيح لكمية البيانات:</b><br>
          <b>(3) كم عدد المجموعات المختلفة من التصاميم التي يمكن إنشاؤها باستخدام عملة واحدة بقيمة 100 جنيه، وعملة بقيمة 50 جنيه، وعملة بقيمة 10 جنيه؟ وأيضاً كم bit يمثل هذا؟</b><br>
          <b>1. كم bit من البيانات يلزم لتمثيل 16 اتجاهاً؟</b><br>
          <b>2. ما هو الحد الأدنى من bits اللازمة لتمثيل 47 محافظة؟</b>
        </div>
        <button type="button" class="book-btn-toggle" onclick="toggleBookAns(this)">🔍 اضغط لإظهار الإجابة النموذجية والخطوات بالتفصيل</button>
        <div class="book-ans-drawer">
          <div class="book-final-ans-pill">🎯 الإجابات النموذجية:</div>
          <div class="book-math-box">
            <b>• ترتيب الوحدات الصحيح:</b> (أ) 1 كيلوبايت KB &lt; 1 ميجابايت MB &lt; 1 جيجابايت GB &lt; 1 تيرابايت TB.<br><br>
            <b>• مسألة العملات الثلاث (100، 50، 10 جنيه):</b><br>
            لدينا 3 عملات، كل منها له حالتان (مستخدمة / غير مستخدمة).<br>
            عدد المجموعات = 2³ = <b>8 مجموعات تصاميم مختلفة</b>، ويمثل ذلك <b>3 bits</b>.<br><br>
            <b>• تمثيل 16 اتجاهاً:</b> بما أن 2⁴ = 16، إذن يلزم <b>4 bits</b>.<br><br>
            <b>• تمثيل 47 محافظة:</b> 2⁵ = 32 &lt; 47 ≤ 2⁶ = 64، إذن الحد الأدنى هو <b>6 bits</b>.
          </div>
        </div>
      </div>"""

new_pane_section = """      <!-- Exercise 4: Unit Order (Q2 from book) -->
      <div class="book-card">
        <div class="book-card-head">
          <span class="book-q-tag">تمرين الكتاب • ترتيب كمية البيانات (اختيار من متعدد)</span>
          <span class="book-page-ref">كتاب الوزارة ص 67</span>
        </div>
        <div class="book-q-text">
          <b>(2) اختر خياراً واحداً يمثل الترتيب الصحيح لكمية البيانات من الخيارات أ إلى ث:</b><br><br>
          <div style="display:flex; flex-direction:column; gap:10px; margin-right:8px; font-size:14.5px;">
            <div style="background:rgba(255,255,255,0.03); padding:8px 14px; border-radius:8px; border:1px solid rgba(255,255,255,0.07);">
              <b>(أ)</b> 1 كيلوبايت KB &lt; 1 ميجابايت MB &lt; 1 جيجابايت GB &lt; 1 تيرابايت TB
            </div>
            <div style="background:rgba(255,255,255,0.03); padding:8px 14px; border-radius:8px; border:1px solid rgba(255,255,255,0.07);">
              <b>(ب)</b> 1 كيلوبايت KB &lt; 1 ميجابايت MB &lt; 1 تيرابايت TB &lt; 1 جيجابايت GB
            </div>
            <div style="background:rgba(255,255,255,0.03); padding:8px 14px; border-radius:8px; border:1px solid rgba(255,255,255,0.07);">
              <b>(ت)</b> 1 تيرابايت TB &lt; 1 كيلوبايت KB &lt; 1 ميجابايت MB &lt; 1 جيجابايت GB
            </div>
            <div style="background:rgba(255,255,255,0.03); padding:8px 14px; border-radius:8px; border:1px solid rgba(255,255,255,0.07);">
              <b>(ث)</b> 1 كيلوبايت KB &lt; 1 تيرابايت TB &lt; 1 ميجابايت MB &lt; 1 جيجابايت GB
            </div>
          </div>
        </div>
        <button type="button" class="book-btn-toggle" onclick="toggleBookAns(this)">🔍 اضغط لإظهار الإجابة النموذجية والتوضيح</button>
        <div class="book-ans-drawer">
          <div class="book-final-ans-pill">🎯 الخيار الصحيح هو: (أ)</div>
          <div class="book-math-box">
            <b>• نص الإجابة الصحيحة:</b><br>
            <span style="color:#34d399; font-weight:800; font-size:15px;">(أ) 1 كيلوبايت KB &lt; 1 ميجابايت MB &lt; 1 جيجابايت GB &lt; 1 تيرابايت TB</span><br><br>
            <b>• التفسير العلمي لوحدات التخزين التصاعدية (من الأصغر للأكبر):</b><br>
            1. <b>الكيلوبايت (KB)</b> = 1,024 بايت (2¹⁰ B)<br>
            2. <b>الميجابايت (MB)</b> = 1,024 KB = 1,048,576 بايت (2²⁰ B)<br>
            3. <b>الجيجابايت (GB)</b> = 1,024 MB = 1,073,741,824 بايت (2³⁰ B)<br>
            4. <b>التيرابايت (TB)</b> = 1,024 GB = 1,099,511,627,776 بايت (2⁴⁰ B)<br>
            <i>(ملاحظة: طُبع في بعض نسخ الكتاب الرمز MG بدلاً من MB والمقصود به الميجابايت)</i>.
          </div>
        </div>
      </div>

      <!-- Exercise 5: Coin combinations (Q3 from book) -->
      <div class="book-card">
        <div class="book-card-head">
          <span class="book-q-tag">تمرين الكتاب • تمثيل البيانات بالعملات النقدية</span>
          <span class="book-page-ref">كتاب الوزارة ص 67</span>
        </div>
        <div class="book-q-text">
          <b>(3) كم عدد المجموعات المختلفة من التصاميم التي يمكن إنشاؤها باستخدام عملة واحدة بقيمة 100 جنيه، وعملة واحدة بقيمة 50 جنيه، وعملة واحدة بقيمة 10 جنيه؟ أيضاً، كم bit من البيانات يمثل هذا؟</b>
        </div>
        <button type="button" class="book-btn-toggle" onclick="toggleBookAns(this)">🔍 اضغط لإظهار الإجابة النموذجية والخطوات بالتفصيل</button>
        <div class="book-ans-drawer">
          <div class="book-final-ans-pill">🎯 الإجابة: 8 مجموعات من التصاميم ، ويمثلها 3 bits</div>
          <div class="book-math-box">
            <div class="step-item"><span class="step-num">1</span> لدينا 3 عملات نقدية (100 جنيه، 50 جنيه، 10 جنيه).</div>
            <div class="step-item"><span class="step-num">2</span> كل عملة لها حالتان فقط (مستخدمة / غير مستخدمة أو ملك / كتابة)، أي تمثل 1 bit.</div>
            <div class="step-item"><span class="step-num">3</span> إجمالي عدد المجموعات والتصاميم الممكنة = <b>2 × 2 × 2 = 2³ = 8 مجموعات مختلفة</b>.</div>
            <div class="step-item"><span class="step-num">4</span> عدد الـ bits اللازمة لتمثيل هذه المجموعات هو: <b>3 bits</b>.</div>
          </div>
        </div>
      </div>

      <!-- Exercise 6: 16 Directions -->
      <div class="book-card">
        <div class="book-card-head">
          <span class="book-q-tag">تمرين الكتاب • تمثيل الاتجاهات</span>
          <span class="book-page-ref">كتاب الوزارة ص 67</span>
        </div>
        <div class="book-q-text">
          <b>1. كم bit من البيانات يلزم لتمثيل 16 اتجاهاً؟</b>
        </div>
        <button type="button" class="book-btn-toggle" onclick="toggleBookAns(this)">🔍 اضغط لإظهار الإجابة النموذجية والخطوات بالتفصيل</button>
        <div class="book-ans-drawer">
          <div class="book-final-ans-pill">🎯 الإجابة: 4 bits (4 بت)</div>
          <div class="book-math-box">
            <div class="step-item"><span class="step-num">1</span> عدد الحالات المطلوب تمثيلها = 16 حالة/اتجاه.</div>
            <div class="step-item"><span class="step-num">2</span> بما أن <b>2⁴ = 16</b>، فإننا نحتاج إلى <b>4 bits</b> بالتحديد.</div>
          </div>
        </div>
      </div>

      <!-- Exercise 7: 47 Governorates -->
      <div class="book-card">
        <div class="book-card-head">
          <span class="book-q-tag">تمرين الكتاب • تمثيل المحافظات</span>
          <span class="book-page-ref">كتاب الوزارة ص 67</span>
        </div>
        <div class="book-q-text">
          <b>2. ما هو الحد الأدنى من bits اللازمة لتمثيل 47 محافظة؟</b>
        </div>
        <button type="button" class="book-btn-toggle" onclick="toggleBookAns(this)">🔍 اضغط لإظهار الإجابة النموذجية والخطوات بالتفصيل</button>
        <div class="book-ans-drawer">
          <div class="book-final-ans-pill">🎯 الإجابة: 6 bits (6 بت)</div>
          <div class="book-math-box">
            <div class="step-item"><span class="step-num">1</span> عدد المحافظات = 47 محافظة.</div>
            <div class="step-item"><span class="step-num">2</span> نحسب قوى العدد 2:</div>
            <div style="margin: 6px 0 6px 28px; color:#cbd5e1;">
              • 5 bits تمثل 2⁵ = 32 (أقل من 47 ولا تكفي لتمثيل جميع المحافظات).<br>
              • 6 bits تمثل 2⁶ = 64 (أكبر من 47 وتتسع لجميع المحافظات).
            </div>
            <div class="step-item"><span class="step-num">3</span> إذن الحد الأدنى من الـ bits المطلوبة هو: <b>6 bits</b>.</div>
          </div>
        </div>
      </div>"""

if old_pane_section in html:
    html = html.replace(old_pane_section, new_pane_section)
    print("Replaced old_pane_section with individual cards successfully!")
else:
    print("old_pane_section not found directly, performing regex replacement...")
    regex_pattern = r'<!-- Exercise 4: Unit Order & Real-life Questions -->.*?</div>\s*</div>\s*</div>\s*(?=<!-- Exercise 5: Conversions -->)'
    html = re.sub(regex_pattern, new_pane_section + '\n\n      ', html, flags=re.DOTALL)
    print("Regex replacement completed!")

# Also check interactive card for question 2 in qlist-u6-l2
# Let's add or update question 2 as an interactive MCQ card with the exact 4 options
q_unit_order_mcq = """
        <!-- Book Question 7: Unit Order MCQ -->
        <div class="q-card" data-type="book" id="q-u6-l2-15">
          <div class="q-head">
            <span class="q-badge book" style="background:rgba(168,85,247,0.18);color:#d8b4fe;border:1px solid rgba(168,85,247,0.35);">📖 كتاب المدرسة • ص67</span>
            <div class="q-text"><b>س15 (تمرين الكتاب المدرسي - اختيار من متعدد):</b> اختر خياراً واحداً يمثل الترتيب الصحيح لكمية البيانات من الخيارات أ إلى ث:</div>
          </div>
          <div class="q-options">
            <button type="button" class="quiz-btn" data-correct="true" onclick="checkOption(this, 'u6-l2', '15', 'الترتيب التصاعدي الصحيح: 1 كيلوبايت KB < 1 ميجابايت MB < 1 جيجابايت GB < 1 تيرابايت TB.')"><span>(أ) 1 كيلوبايت KB &lt; 1 ميجابايت MB &lt; 1 جيجابايت GB &lt; 1 تيرابايت TB</span> <span class="opt-icon"></span></button>
            <button type="button" class="quiz-btn" data-correct="false" onclick="checkOption(this, 'u6-l2', '15', 'الترتيب التصاعدي الصحيح: 1 كيلوبايت KB < 1 ميجابايت MB < 1 جيجابايت GB < 1 تيرابايت TB.')"><span>(ب) 1 كيلوبايت KB &lt; 1 ميجابايت MB &lt; 1 تيرابايت TB &lt; 1 جيجابايت GB</span> <span class="opt-icon"></span></button>
            <button type="button" class="quiz-btn" data-correct="false" onclick="checkOption(this, 'u6-l2', '15', 'الترتيب التصاعدي الصحيح: 1 كيلوبايت KB < 1 ميجابايت MB < 1 جيجابايت GB < 1 تيرابايت TB.')"><span>(ت) 1 تيرابايت TB &lt; 1 كيلوبايت KB &lt; 1 ميجابايت MB &lt; 1 جيجابايت GB</span> <span class="opt-icon"></span></button>
            <button type="button" class="quiz-btn" data-correct="false" onclick="checkOption(this, 'u6-l2', '15', 'الترتيب التصاعدي الصحيح: 1 كيلوبايت KB < 1 ميجابايت MB < 1 جيجابايت GB < 1 تيرابايت TB.')"><span>(ث) 1 كيلوبايت KB &lt; 1 تيرابايت TB &lt; 1 ميجابايت MB &lt; 1 جيجابايت GB</span> <span class="opt-icon"></span></button>
          </div>
          <div class="q-feedback" id="feedback-u6-l2-15"></div>
        </div>
"""

if 'id="q-u6-l2-15"' not in html:
    # Insert right after q-u6-l2-14
    q14_pos = html.find('id="q-u6-l2-14"')
    if q14_pos != -1:
        closing_div_pos = html.find('</div>\n        </div>', q14_pos)
        if closing_div_pos != -1:
            closing_div_pos += len('</div>\n        </div>')
            html = html[:closing_div_pos] + '\n' + q_unit_order_mcq + html[closing_div_pos:]
            print("Injected q-u6-l2-15 into qlist-u6-l2 successfully!")

# Update filter count button
html = html.replace('⭐ جميع الأسئلة (14)', '⭐ جميع الأسئلة (15)')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html with full textbook question 2 and individual cards!")
