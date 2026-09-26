# -*- coding: utf-8 -*-
import re

# Read the HTML template
with open('خريطة_ذهنية_الوحدة_الثانية (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove all old details.qbank from inside the mind map nodes so the diagram remains clean!
html = re.sub(r'\s*<details class="qbank">.*?</details>', '', html, flags=re.DOTALL)

# Add CSS for the Interactive Quiz Engine if not already present
quiz_css = """
  /* ================= Interactive Lesson Quiz & Assessment Engine ================= */
  .lesson-quiz-wrap {
    margin-top: 48px;
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

# Inject CSS before </style>
if '.lesson-quiz-wrap' not in html:
    html = html.replace('</style>', quiz_css + '\n</style>')

print("CSS injected successfully.")
