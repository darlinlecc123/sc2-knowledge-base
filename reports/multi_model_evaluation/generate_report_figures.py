#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从已有审计 JSON 生成多模型评测 CSV 与科研图；不调用模型 API。"""
from __future__ import annotations
import csv, hashlib, json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
DATA, FIG = OUT / "data", OUT / "figures"
SRC_MODEL = ROOT / "knowledge/evals/analysis/20260906_gpt54mini_vs_deepseek/comparison.json"
SRC_V06 = ROOT / "knowledge/evals/analysis/20260906_deepseek_challenge_v0.6_post_three_conditions/audit.json"
SRC_BLIND = ROOT / "knowledge/evals/analysis/20260906_challenge_v0.6_first_blind/audit.json"

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'Arial', 'DejaVu Sans', 'Liberation Sans']
mpl.rcParams.update({"svg.fonttype": "none", "pdf.fonttype": 42})
plt.rcParams.update({'font.size': 7, 'axes.spines.right': False, 'axes.spines.top': False,
                     'axes.linewidth': 0.8, 'legend.frameon': False,
                     'figure.facecolor': 'white', 'axes.facecolor': 'white'})

C = {'gpt':'#484878', 'deepseek':'#3775BA', 'no_kb':'#B4C0E4',
     'full':'#7884B4', 'rag':'#B64342', 'pass':'#2E9E44',
     'fail':'#E53935', 'neutral':'#A8A8A8', 'grid':'#E7E7E7'}
COND = {'no_knowledge_base':'no-KB', 'full_compact_context':'full-context',
        'full_context':'full-context', 'retrieval_augmented':'RAG'}
MODELS = {'gpt':'GPT-5.4-mini*', 'deepseek':'DeepSeek v4 Flash'}
ML = {'behavior_accuracy':'Behavior accuracy', 'variable_hit_rate':'Variable recall',
      'variable_precision':'Variable precision', 'variable_exact_match_rate':'Exact match',
      'evidence_hit_rate':'Evidence hit rate', 'refusal_accuracy':'Refusal accuracy',
      'native_json_compliance_rate':'Native JSON'}

def load(p): return json.loads(p.read_text(encoding='utf-8'))
def file_hash(p): return hashlib.sha256(p.read_bytes()).hexdigest().upper()

def save(fig, name):
    fig.tight_layout(pad=1.1)
    fig.savefig(FIG / (name + '.svg'), bbox_inches='tight')
    fig.savefig(FIG / (name + '.pdf'), bbox_inches='tight')
    fig.savefig(FIG / (name + '.png'), dpi=600, bbox_inches='tight')
    fig.savefig(FIG / (name + '.tiff'), dpi=600, bbox_inches='tight')
    plt.close(fig)

def panel(ax, s):
    ax.text(-0.13, 1.06, s, transform=ax.transAxes, fontsize=9,
            fontweight='bold', va='top')

def label_bars(ax, bars, percent=True, rotate=0, fontsize=6.0):
    for b in bars:
        v = b.get_height()
        text = f'{v:.1f}%' if percent else f'{v:,.0f}'
        ax.annotate(text, (b.get_x()+b.get_width()/2, v), xytext=(0,2),
                    textcoords='offset points', ha='center', va='bottom',
                    fontsize=fontsize, rotation=rotate)

def write_csv(name, rows):
    with (DATA/name).open('w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)

def export_tables(model, v06, blind):
    rows=[]
    for cond,item in model['conditions'].items():
        for mk,sk in [('gpt','gpt_summary'),('deepseek','deepseek_summary')]:
            s=item[sk]
            rows.append({'benchmark':model['benchmark'], 'question_count':model['question_count'],
              'condition':COND[cond], 'model':MODELS[mk], 'behavior_accuracy':s['behavior_accuracy'],
              'variable_hit_rate':s['variable_hit_rate'], 'variable_precision':s['variable_precision'],
              'variable_exact_match_rate':s['variable_exact_match_rate'],
              'evidence_hit_rate':s['evidence_hit_rate'], 'refusal_accuracy':s['refusal_accuracy'],
              'native_json_compliance_rate':s['native_json_compliance_rate'],
              'tokens_total':int(s['tokens']['total']), 'latency_mean_ms':s['latency_ms']['mean'],
              'model_error_count':s['model_error_count']})
    write_csv('model_comparison_challenge_v0.3.csv',rows)
    rows=[]
    for cond,item in v06['conditions'].items():
        s=item['summary']
        rows.append({'benchmark':v06['benchmark']['name'],'question_count':v06['benchmark']['question_count'],
          'model':v06['model']['name'],'condition':COND[cond], 'behavior_accuracy':s['behavior_accuracy'],
          'variable_hit_rate':s['variable_hit_rate'],'variable_precision':s['variable_precision'],
          'variable_exact_match_rate':s['variable_exact_match_rate'],'evidence_hit_rate':s['evidence_hit_rate'],
          'refusal_accuracy':s['refusal_accuracy'],'native_json_compliance_rate':s['native_json_compliance_rate'],
          'tokens_total':int(s['tokens']['total']),'latency_mean_ms':s['latency_ms']['mean'],
          'model_error_count':s['model_error_count'],'format_repaired_count':s['format_repaired_count']})
    write_csv('deepseek_challenge_v0.6_three_conditions.csv',rows)
    rows=[]
    for metric,item in blind['thresholds'].items():
        rows.append({'benchmark':blind['protocol']['challenge_version'],'model':blind['protocol']['model'],
          'metric':metric,'actual':item['actual'],'minimum':item['minimum'],'passed':item['passed']})
    write_csv('challenge_v0.6_blind_thresholds.csv',rows)
    hashes={'challenge_v0.3_model_comparison':file_hash(SRC_MODEL),
            'challenge_v0.6_three_conditions':file_hash(SRC_V06),
            'challenge_v0.6_first_blind':file_hash(SRC_BLIND)}
    (DATA/'source_hashes.json').write_text(json.dumps(hashes,ensure_ascii=False,indent=2),encoding='utf-8')

# Log-scale inputs are clipped to remain strictly positive.
def fig1(model):
    conds=list(model['conditions']); labels=[COND[x] for x in conds]
    x=np.arange(len(conds)); width=.34
    fig,axs=plt.subplots(1,3,figsize=(7.2,2.65),gridspec_kw={'width_ratios':[1.15,1,1]})
    specs=[(-width/2,'gpt','gpt_summary',C['gpt']),(width/2,'deepseek','deepseek_summary',C['deepseek'])]
    for off,m,k,color in specs:
        vals=[100*model['conditions'][q][k]['behavior_accuracy'] for q in conds]
        bars=axs[0].bar(x+off,vals,width,color=color,label=MODELS[m]); label_bars(axs[0],bars)
    axs[0].set(xticks=x,xticklabels=labels,ylim=(0,108),ylabel='Behavior accuracy (%)')
    handles, legend_labels = axs[0].get_legend_handles_labels()
    axs[0].legend(handles, legend_labels, loc='lower left', bbox_to_anchor=(0.0, 1.01), ncol=1, fontsize=6.0); axs[0].grid(axis='y',color=C['grid'],lw=.6); panel(axs[0],'a')
    for off,m,k,color in specs:
        vals=np.clip([model['conditions'][q][k]['tokens']['total'] for q in conds], 1, None)
        bars=axs[1].bar(x+off,vals,width,color=color)
        for b,v in zip(bars,vals): axs[1].annotate(f'{v/1000:.0f}k',(b.get_x()+b.get_width()/2,v),xytext=(0,2),textcoords='offset points',ha='center',fontsize=5.7)
    axs[1].set(xticks=x,xticklabels=labels,yscale='log',ylabel='Total tokens (log scale)')
    axs[1].grid(axis='y',color=C['grid'],lw=.6,which='both'); panel(axs[1],'b')
    for off,m,k,color in specs:
        vals=np.clip([model['conditions'][q][k]['latency_ms']['mean']/1000 for q in conds], 1e-6, None)
        bars=axs[2].bar(x+off,vals,width,color=color)
        for b,v in zip(bars,vals): axs[2].annotate(f'{v:.1f}s',(b.get_x()+b.get_width()/2,v),xytext=(0,2),textcoords='offset points',ha='center',fontsize=5.7)
    axs[2].set(xticks=x,xticklabels=labels,yscale='log',ylabel='Mean latency (s, log scale)')
    axs[2].grid(axis='y',color=C['grid'],lw=.6,which='both'); panel(axs[2],'c')
    fig.suptitle('Same-benchmark model comparison: challenge v0.3 (n = 41)',fontsize=9,y=1.02)
    save(fig,'fig1_model_comparison_challenge_v0.3')

def fig2(model):
    metrics=['behavior_accuracy','variable_hit_rate','variable_precision','evidence_hit_rate','refusal_accuracy','native_json_compliance_rate']
    rows=[]; labels=[]
    for cond,item in model['conditions'].items():
        for m,k in [('gpt','gpt_summary'),('deepseek','deepseek_summary')]:
            rows.append([100*item[k][z] for z in metrics]); labels.append(COND[cond]+' · '+MODELS[m])
    arr=np.array(rows); fig,ax=plt.subplots(figsize=(7.2,3.35))
    cmap=mpl.colors.LinearSegmentedColormap.from_list('softblue',['#F3F5FA','#B4C0E4','#484878'])
    im=ax.imshow(arr,cmap=cmap,vmin=0,vmax=100,aspect='auto')
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]): ax.text(j,i,f'{arr[i,j]:.1f}',ha='center',va='center',fontsize=6.3,color='white' if arr[i,j]>=65 else '#272727')
    ax.set_xticks(range(len(metrics)),[ML[m] for m in metrics],rotation=25,ha='right')
    ax.set_yticks(range(len(labels)),labels); ax.tick_params(length=0)
    for s in ax.spines.values(): s.set_visible(False)
    cb=fig.colorbar(im,ax=ax,fraction=.025,pad=.02); cb.set_label('Score (%)')
    ax.set_title('Metric profile on challenge v0.3',fontsize=9)
    save(fig,'fig2_metric_heatmap_challenge_v0.3')

def fig3(v06):
    conds=list(v06['conditions']); labels=[COND[x] for x in conds]; colors=[C['no_kb'],C['full'],C['rag']]
    metrics=['behavior_accuracy','variable_hit_rate','variable_precision','evidence_hit_rate']; x=np.arange(len(metrics)); width=.23
    fig,axs=plt.subplots(1,2,figsize=(7.2,2.8),gridspec_kw={'width_ratios':[1.7,1]})
    for i,(cond,label,color) in enumerate(zip(conds,labels,colors)):
        s=v06['conditions'][cond]['summary']; vals=[100*s[m] for m in metrics]
        bars=axs[0].bar(x+(i-1)*width,vals,width,label=label,color=color); label_bars(axs[0],bars,rotate=90,fontsize=5.4)
    axs[0].set_xticks(x,[ML[m] for m in metrics],rotation=15,ha='right'); axs[0].set_ylim(0,108)
    axs[0].set_ylabel('Score (%)'); axs[0].legend(loc='upper left',ncol=3,fontsize=6.2); axs[0].grid(axis='y',color=C['grid'],lw=.6); panel(axs[0],'a')
    vals=np.clip([v06['conditions'][q]['summary']['tokens']['total'] for q in conds], 1, None)
    bars=axs[1].bar(labels,vals,color=colors,width=.62)
    for b,v in zip(bars,vals): axs[1].annotate(f'{v/1000:.0f}k',(b.get_x()+b.get_width()/2,v),xytext=(0,2),textcoords='offset points',ha='center',fontsize=6.2)
    axs[1].set_yscale('log'); axs[1].set_ylabel('Total tokens (log scale)'); axs[1].grid(axis='y',color=C['grid'],lw=.6,which='both'); panel(axs[1],'b')
    fig.suptitle('Optimized DeepSeek pipeline: challenge v0.6 post-regression (n = 60)',fontsize=9,y=1.02)
    save(fig,'fig3_deepseek_challenge_v0.6_three_conditions')

def fig4(blind):
    order=['behavior_accuracy','variable_hit_rate','variable_precision','evidence_hit_rate','refusal_accuracy','native_json_compliance_rate']
    actual=np.array([100*blind['thresholds'][m]['actual'] for m in order]); minimum=np.array([100*blind['thresholds'][m]['minimum'] for m in order])
    passed=[blind['thresholds'][m]['passed'] for m in order]; y=np.arange(len(order))[::-1]
    colors=[C['pass'] if p else C['fail'] for p in passed]
    fig,ax=plt.subplots(figsize=(7.2,3.0)); ax.hlines(y,minimum,actual,color=colors,lw=2.4,alpha=.75)
    ax.scatter(minimum,y,s=33,facecolor='white',edgecolor=C['neutral'],linewidth=1.2,label='Predefined threshold',zorder=3)
    ax.scatter(actual,y,s=40,color=colors,label='Observed',zorder=4)
    for yi,a,m,p,col in zip(y,actual,minimum,passed,colors): ax.text(max(a,m)+.55,yi,f"{a:.2f}% ({'pass' if p else 'fail'})",va='center',fontsize=6.5,color=col)
    ax.set_yticks(y,[ML[m] for m in order]); ax.set_xlim(80,102.5); ax.set_xlabel('Score (%)'); ax.grid(axis='x',color=C['grid'],lw=.6)
    ax.legend(loc='upper right',fontsize=6.3); ax.set_title('First-blind RAG assessment: challenge v0.6 (n = 60)',fontsize=9)
    save(fig,'fig4_challenge_v0.6_blind_thresholds')

def main():
    DATA.mkdir(parents=True,exist_ok=True); FIG.mkdir(parents=True,exist_ok=True)
    model,v06,blind=load(SRC_MODEL),load(SRC_V06),load(SRC_BLIND)
    export_tables(model,v06,blind); fig1(model); fig2(model); fig3(v06); fig4(blind)
    print('Generated CSV and figures in',OUT)
if __name__=='__main__': main()
