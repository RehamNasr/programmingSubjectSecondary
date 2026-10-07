# -*- coding: utf-8 -*-
"""
Inject School Textbook Questions & Exercises (Pages 64-67) into index.html
"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Clean duplicate leftover block around lines 6980-7200 in index.html
# Look for the duplicated quiz-wrap-u6-l2
first_quiz_pos = html.find('<div class="lesson-quiz-wrap" id="quiz-wrap-u6-l2">')
second_quiz_pos = html.find('<div class="lesson-quiz-wrap" id="quiz-wrap-u6-l2">', first_quiz_pos + 1)

if second_quiz_pos != -1:
    # There is a duplicate quiz-wrap-u6-l2. Let's inspect where it ends and remove the duplicate.
    print(f"Found duplicate at {first_quiz_pos} and {second_quiz_pos}")
    # Remove the first duplicate block from first_quiz_pos up to second_quiz_pos
    html = html[:first_quiz_pos] + html[second_quiz_pos:]
    print("Removed duplicate quiz-wrap-u6-l2 block successfully!")

# Also clean any orphaned q-card before quiz-wrap-u6-l2
orphan_pattern = r'<div class="q-card" data-type="ministry" id="q-u6-l2-9">.*?</div>\s*</div>\s*</div>\s*(?=\s*<!-- Interactive Quiz & Assessment Card for u6-l2 -->)'
html = re.sub(orphan_pattern, '', html, flags=re.DOTALL)

# CSS for School Textbook Exercises Component
book_css = """
  /* ================= School Textbook Exercises Component ================= */
  .book-exercises-wrap {
    margin-top: 35px;
    background: linear-gradient(135deg, rgba(20, 16, 28, 0.98) 0%, rgba(12, 10, 18, 0.99) 100%);
    border: 1.5px solid rgba(168, 85, 247, 0.4);
    border-radius: 24px;
    padding: 28px 32px;
    box-shadow: 0 15px 45px rgba(0, 0, 0, 0.5), 0 0 30px rgba(168, 85, 247, 0.08);
    position: relative;
    overflow: hidden;
    color: #f1f5f9;
  }
  .book-exercises-wrap::before {
    content: "";
    position: absolute;
    top: 0; right: 0; bottom: 0; left: 0;
    background: repeating-linear-gradient(45deg, rgba(168, 85, 247, 0.015) 0px, rgba(168, 85, 247, 0.015) 2px, transparent 2px, transparent 16px);
    pointer-events: none;
  }
  .book-section-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    padding-bottom: 20px;
    border-bottom: 1.5px solid rgba(168, 85, 247, 0.25);
    flex-wrap: wrap;
    position: relative;
    z-index: 2;
  }
  .book-title-group h3 {
    font-family: 'The Year of Handicrafts', 'Cairo', sans-serif;
    font-size: 20px;
    font-weight: 800;
    color: #c084fc;
    margin: 0 0 6px;
    display: flex;
    align-items: center;
    gap: 10px;
    text-shadow: 0 0 15px rgba(192, 132, 252, 0.3);
  }
  .book-title-group p {
    font-size: 13.5px;
    color: #94a3b8;
    margin: 0;
  }
  .book-badge-source {
    background: linear-gradient(135deg, rgba(168, 85, 247, 0.2) 0%, rgba(215, 38, 56, 0.15) 100%);
    border: 1.5px solid rgba(168, 85, 247, 0.5);
    color: #e9d5ff;
    font-size: 13px;
    font-weight: 800;
    padding: 6px 16px;
    border-radius: 30px;
    box-shadow: 0 2px 10px rgba(168, 85, 247, 0.2);
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }

  .book-tabs-nav {
    display: flex;
    gap: 10px;
    margin: 22px 0 20px;
    flex-wrap: wrap;
    position: relative;
    z-index: 2;
  }
  .book-tab-btn {
    background: rgba(30, 27, 44, 0.8);
    border: 1.5px solid rgba(255, 255, 255, 0.1);
    color: #cbd5e1;
    font-family: 'The Year of Handicrafts', 'Cairo', sans-serif;
    font-size: 13.5px;
    font-weight: 700;
    padding: 8px 18px;
    border-radius: 20px;
    cursor: pointer;
    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  }
  .book-tab-btn:hover {
    border-color: #c084fc;
    color: #ffffff;
    transform: translateY(-1px);
  }
  .book-tab-btn.active {
    background: linear-gradient(135deg, #a855f7 0%, #7e22ce 100%);
    border-color: #c084fc;
    color: #ffffff;
    font-weight: 800;
    box-shadow: 0 4px 16px rgba(168, 85, 247, 0.4);
  }

  .book-tab-pane {
    display: none;
    flex-direction: column;
    gap: 18px;
    position: relative;
    z-index: 2;
  }
  .book-tab-pane.active {
    display: flex;
  }

  .book-card {
    background: rgba(18, 15, 26, 0.85);
    border: 1.5px solid rgba(168, 85, 247, 0.2);
    border-radius: 16px;
    padding: 20px 22px;
    transition: all 0.25s ease;
    backdrop-filter: blur(10px);
  }
  .book-card:hover {
    border-color: rgba(168, 85, 247, 0.45);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
  }
  .book-card-head {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    margin-bottom: 12px;
    flex-wrap: wrap;
  }
  .book-q-tag {
    font-size: 11.5px;
    font-weight: 800;
    padding: 3px 12px;
    border-radius: 6px;
    background: rgba(168, 85, 247, 0.18);
    color: #d8b4fe;
    border: 1px solid rgba(168, 85, 247, 0.35);
  }
  .book-page-ref {
    font-size: 11.5px;
    color: #94a3b8;
    background: rgba(255,255,255,0.05);
    padding: 2px 8px;
    border-radius: 4px;
  }
  .book-q-text {
    font-size: 15px;
    font-weight: 700;
    line-height: 1.75;
    color: #f8fafc;
    margin-bottom: 14px;
  }
  .book-q-text b {
    color: #f6be1f;
  }

  .book-btn-toggle {
    background: linear-gradient(135deg, rgba(168, 85, 247, 0.15) 0%, rgba(99, 102, 241, 0.12) 100%);
    border: 1.5px solid rgba(168, 85, 247, 0.35);
    color: #e9d5ff;
    font-family: 'The Year of Handicrafts', 'Cairo', sans-serif;
    font-size: 13px;
    font-weight: 700;
    padding: 8px 18px;
    border-radius: 10px;
    cursor: pointer;
    transition: all 0.2s ease;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    width: 100%;
    justify-content: center;
    margin-top: 4px;
  }
  .book-btn-toggle:hover {
    background: linear-gradient(135deg, rgba(168, 85, 247, 0.3) 0%, rgba(99, 102, 241, 0.25) 100%);
    border-color: #c084fc;
    color: #ffffff;
    box-shadow: 0 4px 14px rgba(168, 85, 247, 0.25);
  }
  .book-ans-drawer {
    display: none;
    margin-top: 14px;
    background: rgba(10, 8, 15, 0.95);
    border: 1px solid rgba(168, 85, 247, 0.3);
    border-right: 4px solid #a855f7;
    border-radius: 12px;
    padding: 16px 20px;
    line-height: 1.85;
    font-size: 14px;
    color: #e2e8f0;
    animation: fadeInSlide 0.3s ease-out forwards;
  }
  .book-ans-drawer.show {
    display: block;
  }
  .book-final-ans-pill {
    background: rgba(45, 212, 160, 0.15);
    border: 1px solid rgba(45, 212, 160, 0.4);
    color: #34d399;
    font-weight: 800;
    padding: 6px 14px;
    border-radius: 8px;
    display: inline-block;
    margin-bottom: 10px;
  }
  .book-math-box {
    background: rgba(0, 0, 0, 0.3);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 8px;
    padding: 12px 16px;
    margin-top: 10px;
    font-family: 'Cairo', sans-serif;
    font-size: 13.5px;
    direction: rtl;
  }
  .book-math-box .step-item {
    margin-bottom: 6px;
    display: flex;
    align-items: baseline;
    gap: 8px;
  }
  .step-num {
    background: #a855f7;
    color: #ffffff;
    font-size: 11px;
    font-weight: 800;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }
  .ladder-table {
    width: 100%;
    max-width: 380px;
    margin: 10px 0;
    border-collapse: collapse;
    font-size: 13px;
    text-align: center;
  }
  .ladder-table th {
    background: rgba(168, 85, 247, 0.25);
    color: #f1f5f9;
    padding: 6px 10px;
    border: 1px solid rgba(168, 85, 247, 0.3);
  }
  .ladder-table td {
    padding: 6px 10px;
    border: 1px solid rgba(255, 255, 255, 0.08);
    background: rgba(255, 255, 255, 0.02);
  }
  .ladder-table tr:hover td {
    background: rgba(168, 85, 247, 0.1);
  }
"""

if '.book-exercises-wrap {' not in html:
    html = html.replace('</style>', book_css + '\n</style>')

# JS for tab switching & answer drawers
book_js = """
    function switchBookTab(paneId, btn) {
      var wrap = btn.closest('.book-exercises-wrap');
      if (!wrap) return;
      wrap.querySelectorAll('.book-tab-btn').forEach(function(b) { b.classList.remove('active'); });
      wrap.querySelectorAll('.book-tab-pane').forEach(function(p) { p.classList.remove('active'); });
      btn.classList.add('active');
      var pane = wrap.querySelector('#' + paneId);
      if (pane) pane.classList.add('active');
    }

    function toggleBookAns(btn) {
      var drawer = btn.nextElementSibling;
      if (drawer && drawer.classList.contains('book-ans-drawer')) {
        var isShown = drawer.classList.toggle('show');
        btn.innerHTML = isShown ? '🔒 إخفاء الإجابة والخطوات' : '🔍 اضغط لإظهار الإجابة النموذجية والخطوات بالتفصيل';
      }
    }
"""

if 'function switchBookTab' not in html:
    html = html.replace('</script>', book_js + '\n</script>')

# Build the complete HTML for the textbook exercises section
book_section_html = """
  <!-- ================= SCHOOL TEXTBOOK EXERCISES (PAGES 64 - 67) ================= -->
  <div class="book-exercises-wrap" id="book-ex-u6-l2">
    <!-- Header -->
    <div class="book-section-header">
      <div class="book-title-group">
        <h3>📖 أسئلة وتدريبات كتاب المدرسة المعتمد — الدرس 2: النظام الثنائي وكمية البيانات</h3>
        <p>حلول نموذجية وشاملة لجميع تدريبات "تحدي معلوماتك" و"جرب بنفسك" و"تمارين وتطبيقات الكتاب" مع الشرح والخطوات الرياضية بالتفصيل</p>
      </div>
      <div class="book-badge-source">
        <span>📘 الكتاب المدرسي (الصفحات: 64، 65، 66، 67)</span>
      </div>
    </div>

    <!-- Category Tabs Navigation -->
    <div class="book-tabs-nav">
      <button type="button" class="book-tab-btn active" onclick="switchBookTab('pane-challenge-u6-l2', this)">🌟 تحدي معلوماتك (ص 64 - 65)</button>
      <button type="button" class="book-tab-btn" onclick="switchBookTab('pane-try-u6-l2', this)">🧪 جرب بنفسك (ص 66)</button>
      <button type="button" class="book-tab-btn" onclick="switchBookTab('pane-exercises-u6-l2', this)">📐 تمارين ومسائل وتطبيقات الكتاب (ص 67)</button>
    </div>

    <!-- TAB 1: تحدي معلوماتك -->
    <div class="book-tab-pane active" id="pane-challenge-u6-l2">

      <!-- Challenge Q1 -->
      <div class="book-card">
        <div class="book-card-head">
          <span class="book-q-tag">تحدي معلوماتك • أكمل الفراغات</span>
          <span class="book-page-ref">كتاب الوزارة ص 64 - 65</span>
        </div>
        <div class="book-q-text">
          <b>(1) [1] أكمل الجمل التالية بملء الفراغات (أ) إلى (هـ) بالمصطلحات والأرقام المناسبة:</b><br>
          « أصغر وحدة بيانات تسمى الـ bit، وهي تتوافق مع رقم <b>( أ )</b> في نظام العد الثنائي. هذا يجعل من الممكن تمثيل <b>( ب )</b> من بيانات. بالإضافة إلى ذلك، مجموعة من <b>( ج )</b> bit تسمى <b>( د )</b> واحد، ويتم تمثيلها بـ 1B. على سبيل المثال، 24 bit = <b>( هـ )</b> Byte. »
        </div>
        <button type="button" class="book-btn-toggle" onclick="toggleBookAns(this)">🔍 اضغط لإظهار الإجابة النموذجية والخطوات بالتفصيل</button>
        <div class="book-ans-drawer">
          <div class="book-final-ans-pill">🎯 الإجابة النموذجية المعتمدة:</div>
          <div class="book-math-box">
            <div class="step-item"><span class="step-num">أ</span> <b>(أ) = رقم واحد في النظام الثنائي (يمكن أن يمثل قيمتين: 0 أو 1).</b></div>
            <div class="step-item"><span class="step-num">ب</span> <b>(ب) = احتمالين (2) من البيانات</b> (لأن 2¹ = 2).</div>
            <div class="step-item"><span class="step-num">ج</span> <b>(ج) = 8</b> (يتكون البايت من 8 بت).</div>
            <div class="step-item"><span class="step-num">د</span> <b>(د) = Byte (بايت)</b> واحد.</div>
            <div class="step-item"><span class="step-num">هـ</span> <b>(هـ) = 3 Byte</b> (حيث: 24 bit ÷ 8 = 3 بايت).</div>
          </div>
        </div>
      </div>

      <!-- Challenge Q2 -->
      <div class="book-card">
        <div class="book-card-head">
          <span class="book-q-tag">تحدي معلوماتك • مسألة احصائية</span>
          <span class="book-page-ref">كتاب الوزارة ص 65</span>
        </div>
        <div class="book-q-text">
          <b>[2] كم من bit مطلوب لتمثيل جميع النتائج الممكنة عند رمي نردين؟</b>
        </div>
        <button type="button" class="book-btn-toggle" onclick="toggleBookAns(this)">🔍 اضغط لإظهار الإجابة النموذجية والخطوات بالتفصيل</button>
        <div class="book-ans-drawer">
          <div class="book-final-ans-pill">🎯 الإجابة النهائية: 6 bits (6 بت)</div>
          <div class="book-math-box">
            <div class="step-item"><span class="step-num">1</span> عند رمي نردين، فإن عدد النتائج الممكنة = <b>6 × 6 = 36 احتمالاً مختلفاً</b>.</div>
            <div class="step-item"><span class="step-num">2</span> لحساب عدد البتات n المطلوبة، نبحث عن أصغر قيمة تحقق الشرط: <b>2ⁿ ≥ 36</b>:</div>
            <div style="margin: 8px 0 8px 28px; color:#cbd5e1;">
              • إذا استخدمنا <b>5 bits</b>: 2⁵ = 32 احتمالاً (أقل من 36 ولا تكفي لتغطية كافة النتائج).<br>
              • إذا استخدمنا <b>6 bits</b>: 2⁶ = 64 مجموعة/احتمالاً (أكبر من 36 وتكفي لتمثيل كافة النتائج).
            </div>
            <div class="step-item"><span class="step-num">3</span> <b>إذن عدد البتات المطلوبة = 6 bits.</b></div>
          </div>
        </div>
      </div>

      <!-- Challenge Q3 -->
      <div class="book-card">
        <div class="book-card-head">
          <span class="book-q-tag">تحدي معلوماتك • حساب السعات والأسس</span>
          <span class="book-page-ref">كتاب الوزارة ص 65</span>
        </div>
        <div class="book-q-text">
          <b>[3] كم Byte يوجد في [ 1 MB ]؟ أجب على شكل أس للعدد 2.</b>
        </div>
        <button type="button" class="book-btn-toggle" onclick="toggleBookAns(this)">🔍 اضغط لإظهار الإجابة النموذجية والخطوات بالتفصيل</button>
        <div class="book-ans-drawer">
          <div class="book-final-ans-pill">🎯 الإجابة النهائية: 2²⁰ Byte (2 أس 20 بايت = 1,048,576 بايت)</div>
          <div class="book-math-box">
            <div class="step-item"><span class="step-num">1</span> 1 KB = 1024 Byte = <b>2¹⁰ Byte</b>.</div>
            <div class="step-item"><span class="step-num">2</span> 1 MB = 1024 KB = 1,024 × 1,024 Byte = <b>2¹⁰ × 2¹⁰ Byte = 2²⁰ Byte</b>.</div>
            <div class="step-item"><span class="step-num">3</span> الناتج على شكل أس للعدد 2 هو: <b>2²⁰ بايت (Byte)</b>.</div>
          </div>
        </div>
      </div>

      <!-- Challenge Q4 -->
      <div class="book-card">
        <div class="book-card-head">
          <span class="book-q-tag">تحدي معلوماتك • مقارنة السعات</span>
          <span class="book-page-ref">كتاب الوزارة ص 65</span>
        </div>
        <div class="book-q-text">
          <b>[4] كم مرة تكون 4 bit من البيانات أكبر مقارنة بـ 2 bit من البيانات؟</b>
        </div>
        <button type="button" class="book-btn-toggle" onclick="toggleBookAns(this)">🔍 اضغط لإظهار الإجابة النموذجية والخطوات بالتفصيل</button>
        <div class="book-ans-drawer">
          <div class="book-final-ans-pill">🎯 الإجابة النهائية: 4 مرات (تزيد بمقدار 4 أضعاف)</div>
          <div class="book-math-box">
            <div class="step-item"><span class="step-num">1</span> كمية البيانات التي يمكن تمثيلها بـ 2 bit هي: <b>2² = 4 احتمالات</b>.</div>
            <div class="step-item"><span class="step-num">2</span> كمية البيانات التي يمكن تمثيلها بـ 4 bit هي: <b>2⁴ = 16 احتمالاً</b>.</div>
            <div class="step-item"><span class="step-num">3</span> نسبة الزيادة = 16 ÷ 4 = <b>4 مرات</b> (أو باستخدام قوانين الأسس: 2⁴ ÷ 2² = 2⁴⁻² = 2² = <b>4 مرات</b>).</div>
          </div>
        </div>
      </div>

      <!-- Challenge Q5 -->
      <div class="book-card">
        <div class="book-card-head">
          <span class="book-q-tag">تحدي معلوماتك • تحويل من ثنائي إلى عشري</span>
          <span class="book-page-ref">كتاب الوزارة ص 65</span>
        </div>
        <div class="book-q-text">
          <b>(2) [1] عبّر عن الأرقام الثنائية التالية في الصورة العشرية:</b><br>
          (أ) (11010)₂ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (ب) (101011)₂
        </div>
        <button type="button" class="book-btn-toggle" onclick="toggleBookAns(this)">🔍 اضغط لإظهار الإجابة النموذجية والخطوات بالتفصيل</button>
        <div class="book-ans-drawer">
          <div class="book-final-ans-pill">🎯 الناتج: (أ) = 26 &nbsp;|&nbsp; (ب) = 43</div>
          <div class="book-math-box">
            <b>• خطوات حل (أ) (11010)₂ :</b><br>
            = (1 × 2⁴) + (1 × 2³) + (0 × 2²) + (1 × 2¹) + (0 × 2⁰)<br>
            = 16 + 8 + 0 + 2 + 0 = <b>26</b> في النظام العشري.<br><br>
            <b>• خطوات حل (ب) (101011)₂ :</b><br>
            = (1 × 2⁵) + (0 × 2⁴) + (1 × 2³) + (0 × 2²) + (1 × 2¹) + (1 × 2⁰)<br>
            = 32 + 0 + 8 + 0 + 2 + 1 = <b>43</b> في النظام العشري.
          </div>
        </div>
      </div>

      <!-- Challenge Q6 -->
      <div class="book-card">
        <div class="book-card-head">
          <span class="book-q-tag">تحدي معلوماتك • تحويل من عشري إلى ثنائي</span>
          <span class="book-page-ref">كتاب الوزارة ص 65</span>
        </div>
        <div class="book-q-text">
          <b>[2] عبّر عن الأرقام العشرية التالية في الصورة الثنائية (باستخدام سلم القسمة على 2):</b><br>
          (أ) 39 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (ب) 120
        </div>
        <button type="button" class="book-btn-toggle" onclick="toggleBookAns(this)">🔍 اضغط لإظهار الإجابة النموذجية والخطوات بالتفصيل</button>
        <div class="book-ans-drawer">
          <div class="book-final-ans-pill">🎯 الناتج: (أ) 39 = (100111)₂ &nbsp;|&nbsp; (ب) 120 = (1111000)₂</div>
          <div class="book-math-box">
            <b>• خطوات قسمة العدد 39 على 2:</b>
            <table class="ladder-table">
              <tr><th>العملية</th><th>ناتج القسمة</th><th>باقي القسمة</th></tr>
              <tr><td>39 ÷ 2</td><td>19</td><td><b>1</b> (الخانة الأولى)</td></tr>
              <tr><td>19 ÷ 2</td><td>9</td><td><b>1</b></td></tr>
              <tr><td>9 ÷ 2</td><td>4</td><td><b>1</b></td></tr>
              <tr><td>4 ÷ 2</td><td>2</td><td><b>0</b></td></tr>
              <tr><td>2 ÷ 2</td><td>1</td><td><b>0</b></td></tr>
              <tr><td>1 ÷ 2</td><td>0</td><td><b>1</b> (الخانة الأخيرة)</td></tr>
            </table>
            نقرأ البواقي من الأسفل للأعلى (من اليسار لليمين ثنائياً): <b>(100111)₂</b>.<br><br>

            <b>• خطوات قسمة العدد 120 على 2:</b>
            <table class="ladder-table">
              <tr><th>العملية</th><th>ناتج القسمة</th><th>باقي القسمة</th></tr>
              <tr><td>120 ÷ 2</td><td>60</td><td><b>0</b></td></tr>
              <tr><td>60 ÷ 2</td><td>30</td><td><b>0</b></td></tr>
              <tr><td>30 ÷ 2</td><td>15</td><td><b>0</b></td></tr>
              <tr><td>15 ÷ 2</td><td>7</td><td><b>1</b></td></tr>
              <tr><td>7 ÷ 2</td><td>3</td><td><b>1</b></td></tr>
              <tr><td>3 ÷ 2</td><td>1</td><td><b>1</b></td></tr>
              <tr><td>1 ÷ 2</td><td>0</td><td><b>1</b></td></tr>
            </table>
            نقرأ البواقي من الأسفل للأعلى: <b>(1111000)₂</b>.
          </div>
        </div>
      </div>

    </div>

    <!-- TAB 2: جرب بنفسك -->
    <div class="book-tab-pane" id="pane-try-u6-l2">

      <!-- Try Q1 -->
      <div class="book-card">
        <div class="book-card-head">
          <span class="book-q-tag">جرب بنفسك • أكمل الفراغات</span>
          <span class="book-page-ref">كتاب الوزارة ص 66</span>
        </div>
        <div class="book-q-text">
          <b>[1] أكمل الجمل التالية بملء الفراغات [1] إلى [3] بالمصطلحات والأرقام المناسبة:</b><br>
          « الأرقام التي نستخدمها في حياتنا اليومية يتم التعبير عنها بالنظام <b>[ 1 ]</b>، باستخدام الأرقام من 0 إلى 9. يوجد أيضاً النظام <b>[ 2 ]</b> الذي يستخدم الرقمين 0 و 1، والبيانات التي يتعامل معها الكمبيوتر تستخدم بشكل أساسي النظام <b>[ 2 ]</b>. ومع ذلك نظراً لأن هذه الوحدة صغيرة جداً ويصعب فهمها، غالباً ما يتم استخدام البايت الواحد، والذي يتكون من <b>[ 3 ]</b> bit، لتمثيل البيانات. »
        </div>
        <button type="button" class="book-btn-toggle" onclick="toggleBookAns(this)">🔍 اضغط لإظهار الإجابة النموذجية والخطوات بالتفصيل</button>
        <div class="book-ans-drawer">
          <div class="book-final-ans-pill">🎯 الإجابة النموذجية:</div>
          <div class="book-math-box">
            • <b>[ 1 ] = النظام العشري (Decimal System)</b>.<br>
            • <b>[ 2 ] = النظام الثنائي (Binary System)</b>.<br>
            • <b>[ 3 ] = 8</b> (يتكون البايت الواحد من 8 bits).
          </div>
        </div>
      </div>

      <!-- Try Q2 - Q5 Grid Cards -->
      <div class="book-card">
        <div class="book-card-head">
          <span class="book-q-tag">جرب بنفسك • أسئلة السعات والوحدات</span>
          <span class="book-page-ref">كتاب الوزارة ص 66</span>
        </div>
        <div class="book-q-text">
          <b>(2) كم عدد الـ bit في 5 Byte؟</b><br>
          <b>(3) كم عدد القطع المختلفة التي يمكن تمثيلها بـ 3 Byte؟</b><br>
          <b>(4) كم مرة تزيد كمية البيانات في 5 bit مقارنة بكمية البيانات في 3 bit؟</b><br>
          <b>(5) كم ميغابايت (MB) في جيجابايت 1 GB؟ وكم بايت (B)؟ أجب على شكل أس للعدد 2.</b>
        </div>
        <button type="button" class="book-btn-toggle" onclick="toggleBookAns(this)">🔍 اضغط لإظهار الإجابة النموذجية والخطوات بالتفصيل</button>
        <div class="book-ans-drawer">
          <div class="book-final-ans-pill">🎯 الإجابات والحلول الرياضية:</div>
          <div class="book-math-box">
            <b>• حل (2):</b> بما أن 1 Byte = 8 bits، إذن 5 Byte = 5 × 8 = <b>40 bit</b>.<br><br>
            <b>• حل (3):</b> 3 Byte = 3 × 8 = 24 bit. عدد القطع والاحتمالات الممكن تمثيلها = <b>2²⁴ = 16,777,216 قطعة واحتمالاً</b>.<br><br>
            <b>• حل (4):</b> كمية بيانات 5 bit هي 2⁵ = 32، وكمية بيانات 3 bit هي 2³ = 8.<br>
            نسبة الزيادة = 32 ÷ 8 = <b>4 مرات</b> (أو 2⁵⁻³ = 2² = <b>4 مرات</b>).<br><br>
            <b>• حل (5):</b><br>
            - عدد الميجابايت في 1 GB = 1024 MB = <b>2¹⁰ MB</b>.<br>
            - عدد البايت في 1 GB = 1024 × 1024 × 1024 Byte = <b>2³⁰ Byte</b> (2 أس 30 بايت).
          </div>
        </div>
      </div>

      <!-- Try Q6 - Q8 Real-world bit representations -->
      <div class="book-card">
        <div class="book-card-head">
          <span class="book-q-tag">جرب بنفسك • تمثيل الحالات الحياتية بالبت</span>
          <span class="book-page-ref">كتاب الوزارة ص 66</span>
        </div>
        <div class="book-q-text">
          <b>(6) كم bit من البيانات اللازمة لتمثيل الفصول الأربعة: الربيع، والصيف، والخريف، والشتاء؟</b><br>
          <b>(7) كم bit من البيانات اللازمة لتمثيل مجموعة مكونة من 52 ورقة لعب، باستثناء الجوكر؟</b><br>
          <b>(8) كم bit من البيانات اللازمة لتسجيل جميع النتائج الممكنة عند رمي عملة معدنية ثلاث مرات؟</b>
        </div>
        <button type="button" class="book-btn-toggle" onclick="toggleBookAns(this)">🔍 اضغط لإظهار الإجابة النموذجية والخطوات بالتفصيل</button>
        <div class="book-ans-drawer">
          <div class="book-final-ans-pill">🎯 الإجابات والشرح:</div>
          <div class="book-math-box">
            <b>• حل (6) الفصول الأربعة:</b> لدينا 4 حالات. بما أن 2² = 4، فإننا نحتاج إلى <b>2 bits</b> فقط (مثلاً: 00 الربيع، 01 الصيف، 10 الخريف، 11 الشتاء).<br><br>
            <b>• حل (7) 52 ورقة لعب:</b> لدينا 52 حالة. إذا استخدمنا 5 bits (2⁵ = 32) لا تكفي، أما 6 bits (2⁶ = 64) فتتسع لجميع الأوراق. إذن نحتاج إلى <b>6 bits</b>.<br><br>
            <b>• حل (8) رمي عملة 3 مرات:</b> في كل رمية هناك احتمالان (صورة/كتابة). إجمالي النتائج = 2 × 2 × 2 = 8 = 2³. إذن نحتاج إلى <b>3 bits</b>.
          </div>
        </div>
      </div>

      <!-- Try Q9 - Conversions -->
      <div class="book-card">
        <div class="book-card-head">
          <span class="book-q-tag">جرب بنفسك • التحويلات العددية</span>
          <span class="book-page-ref">كتاب الوزارة ص 66</span>
        </div>
        <div class="book-q-text">
          <b>[2] (1) عبّر عن الأعداد الثنائية التالية بالصيغة العشرية:</b> [1] (110)₂ &nbsp;&nbsp;|&nbsp;&nbsp; [2] (10100)₂ &nbsp;&nbsp;|&nbsp;&nbsp; [3] (111001)₂<br>
          <b>[2] (2) عبّر عن الأعداد العشرية التالية بالصيغة الثنائية:</b> [1] 65 &nbsp;&nbsp;|&nbsp;&nbsp; [2] 106 &nbsp;&nbsp;|&nbsp;&nbsp; [3] 143
        </div>
        <button type="button" class="book-btn-toggle" onclick="toggleBookAns(this)">🔍 اضغط لإظهار الإجابة النموذجية والخطوات بالتفصيل</button>
        <div class="book-ans-drawer">
          <div class="book-final-ans-pill">🎯 نواتج التحويلات:</div>
          <div class="book-math-box">
            <b>أولاً: من ثنائي إلى عشري:</b><br>
            • [1] (110)₂ = (1×4) + (1×2) + (0×1) = 4 + 2 + 0 = <b>6</b>.<br>
            • [2] (10100)₂ = (1×16) + (0×8) + (1×4) + (0×2) + (0×1) = 16 + 4 = <b>20</b>.<br>
            • [3] (111001)₂ = (1×32) + (1×16) + (1×8) + (0×4) + (0×2) + (1×1) = 32 + 16 + 8 + 1 = <b>57</b>.<br><br>
            <b>ثانياً: من عشري إلى ثنائي:</b><br>
            • [1] 65 = 64 + 1 = <b>(1000001)₂</b>.<br>
            • [2] 106 = 64 + 32 + 8 + 2 = <b>(1101010)₂</b>.<br>
            • [3] 143 = 128 + 8 + 4 + 2 + 1 = <b>(10001111)₂</b>.
          </div>
        </div>
      </div>

    </div>

    <!-- TAB 3: تمارين ومسائل وتطبيقات الكتاب -->
    <div class="book-tab-pane" id="pane-exercises-u6-l2">

      <!-- Exercise 1: DVD Problem -->
      <div class="book-card">
        <div class="book-card-head">
          <span class="book-q-tag">مسألة تطبيقية • أقراص DVD والقرص الصلب</span>
          <span class="book-page-ref">كتاب الوزارة ص 67</span>
        </div>
        <div class="book-q-text">
          <b>⭐ مسألة: كم عدد أقراص DVD بسعة 4.7 GB يمكن تخزينها على قرص صلب بسعة 1 تيرابايت 1 TB؟ قرّب إجابتك إلى أقرب عدد صحيح.</b>
        </div>
        <button type="button" class="book-btn-toggle" onclick="toggleBookAns(this)">🔍 اضغط لإظهار الإجابة النموذجية والخطوات بالتفصيل</button>
        <div class="book-ans-drawer">
          <div class="book-final-ans-pill">🎯 الإجابة: حوالي 218 قرص DVD (أو 217 قرصاً كاملاً)</div>
          <div class="book-math-box">
            <div class="step-item"><span class="step-num">1</span> نحول سعة القرص الصلب من TB إلى GB: <b>1 TB = 1024 GB</b>.</div>
            <div class="step-item"><span class="step-num">2</span> نحسب عدد أقراص DVD بقسمة السعة الإجمالية على سعة القرص الواحد:</div>
            <div style="margin: 8px 0 8px 28px; color:#f8fafc; font-weight:700;">
              عدد الأقراص = 1024 GB ÷ 4.7 GB = <b>217.872</b>
            </div>
            <div class="step-item"><span class="step-num">3</span> بالتقريب لأقرب عدد صحيح: <b>218 قرص DVD</b> (السعة الكاملة تتسع لـ 217 قرصاً كاملاً مع مساحة متبقية).</div>
          </div>
        </div>
      </div>

      <!-- Exercise 2: USB Images Problem -->
      <div class="book-card">
        <div class="book-card-head">
          <span class="book-q-tag">مسألة تطبيقية • تخزين الصور على فلاش USB</span>
          <span class="book-page-ref">كتاب الوزارة ص 67</span>
        </div>
        <div class="book-q-text">
          <b>⭐ مسألة: كم عدد الصور، حجم كل منها 2 ميجابايت 2 MB، التي يمكن تخزينها على محرك أقراص فلاش USB بسعة 32 جيجابايت 32 GB؟</b>
        </div>
        <button type="button" class="book-btn-toggle" onclick="toggleBookAns(this)">🔍 اضغط لإظهار الإجابة النموذجية والخطوات بالتفصيل</button>
        <div class="book-ans-drawer">
          <div class="book-final-ans-pill">🎯 الإجابة: 16,384 صورة</div>
          <div class="book-math-box">
            <div class="step-item"><span class="step-num">1</span> نحول سعة الفلاشة من GB إلى MB: <b>32 GB = 32 × 1024 MB = 32,768 MB</b>.</div>
            <div class="step-item"><span class="step-num">2</span> نقسم السعة الإجمالية على حجم الصورة الواحدة (2 MB):</div>
            <div style="margin: 8px 0 8px 28px; color:#f8fafc; font-weight:700;">
              عدد الصور = 32,768 MB ÷ 2 MB = <b>16,384 صورة</b> (أو 32 × 512 = 16,384).
            </div>
          </div>
        </div>
      </div>

      <!-- Exercise 3: Fill in blanks [1] to [6] -->
      <div class="book-card">
        <div class="book-card-head">
          <span class="book-q-tag">تمرين الكتاب • اختر العدد أو المعادلة الأنسب [1] إلى [6]</span>
          <span class="book-page-ref">كتاب الوزارة ص 67</span>
        </div>
        <div class="book-q-text">
          <b>(1) اختر العدد أو المعادلة الأنسب لملء الفراغات من [1] إلى [6] من الخيارات (أ) إلى (ر):</b><br>
          « كمية الاحتمالات التي يمكن تمثيلها بـ 1 bit هي <b>[ 1 ]</b>. بالإضافة إلى ذلك، بما أن 1 بايت يتكون من <b>[ 2 ]</b> bit، فإن كمية البيانات التي يمكن تمثيلها بـ 1 بايت هي <b>[ 3 ]</b>. على سبيل المثال، 32 bit تساوي <b>[ 4 ]</b> بايت. بالإضافة إلى ذلك، يتم التعبير عن 1 كيلوبايت على أنها <b>[ 5 ]</b> بايت. لحساب عدد الـ bit في 24 كيلوبايت، عليك حساب التعبير <b>[ 6 ]</b>. »
        </div>
        <button type="button" class="book-btn-toggle" onclick="toggleBookAns(this)">🔍 اضغط لإظهار الإجابة النموذجية والخطوات بالتفصيل</button>
        <div class="book-ans-drawer">
          <div class="book-final-ans-pill">🎯 الاختيارات الصحيحة من جدول الخيارات:</div>
          <div class="book-math-box">
            • <b>[ 1 ] = 2</b> (الخيار ب) — 1 bit يمثل حالتين فقط.<br>
            • <b>[ 2 ] = 8</b> (الخيار ث) — 1 بايت = 8 bit.<br>
            • <b>[ 3 ] = 256</b> (الخيار ج) — 2⁸ = 256 احتمالاً.<br>
            • <b>[ 4 ] = 4</b> (الخيار ت) — 32 bit ÷ 8 = 4 بايت.<br>
            • <b>[ 5 ] = 1,024</b> (الخيار ح) — 1 KB = 1024 Byte.<br>
            • <b>[ 6 ] = 8 × 1024 × 24</b> (الخيار ر أو د: 24 × 1024 × 8) — للتحويل من KB إلى Byte نضرب في 1024، ثم من Byte إلى bit نضرب في 8.
          </div>
        </div>
      </div>

      <!-- Exercise 4: Unit Order & Real-life Questions -->
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
      </div>

      <!-- Exercise 5: Conversions -->
      <div class="book-card">
        <div class="book-card-head">
          <span class="book-q-tag">تمرين الكتاب • مسائل التحويلات العددية</span>
          <span class="book-page-ref">كتاب الوزارة ص 67</span>
        </div>
        <div class="book-q-text">
          <b>[2] (1) عبر عن الأعداد الثنائية التالية بالصيغة العشرية:</b> [1] (101)₂ &nbsp;&nbsp;|&nbsp;&nbsp; [2] (10101)₂ &nbsp;&nbsp;|&nbsp;&nbsp; [3] (101101)₂<br>
          <b>[2] (2) عبر عن الأعداد العشرية التالية بالصيغة الثنائية:</b> [1] 13 &nbsp;&nbsp;|&nbsp;&nbsp; [2] 128 &nbsp;&nbsp;|&nbsp;&nbsp; [3] 138
        </div>
        <button type="button" class="book-btn-toggle" onclick="toggleBookAns(this)">🔍 اضغط لإظهار الإجابة النموذجية والخطوات بالتفصيل</button>
        <div class="book-ans-drawer">
          <div class="book-final-ans-pill">🎯 نواتج التحويلات:</div>
          <div class="book-math-box">
            <b>أولاً: من ثنائي إلى عشري:</b><br>
            • [1] (101)₂ = 4 + 1 = <b>5</b>.<br>
            • [2] (10101)₂ = 16 + 4 + 1 = <b>21</b>.<br>
            • [3] (101101)₂ = 32 + 8 + 4 + 1 = <b>45</b>.<br><br>
            <b>ثانياً: من عشري إلى ثنائي:</b><br>
            • [1] 13 = 8 + 4 + 1 = <b>(1101)₂</b>.<br>
            • [2] 128 = 2⁷ = <b>(10000000)₂</b>.<br>
            • [3] 138 = 128 + 8 + 2 = <b>(10001010)₂</b>.
          </div>
        </div>
      </div>

    </div>
  </div>
"""

# Inject book_section_html right after the quiz-wrap-u6-l2 in index.html
# We find where quiz-wrap-u6-l2 closes (or right before unit 6 lesson 3)
insert_target = '<!-- =================== UNIT6 - LESSON 3 =================== -->'
if '<div class="book-exercises-wrap" id="book-ex-u6-l2">' not in html:
    html = html.replace(insert_target, book_section_html + '\n\n  ' + insert_target)
    print("Injected book_section_html before Lesson 3 successfully!")
else:
    # Replace existing
    old_section_pattern = r'<!-- ================= SCHOOL TEXTBOOK EXERCISES.*?</div>\s*</div>\s*(?=<!-- =================== UNIT6 - LESSON 3)'
    html = re.sub(old_section_pattern, book_section_html + '\n\n  ', html, flags=re.DOTALL)
    print("Replaced existing book_section_html successfully!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html successfully!")
