import json,sys
d=json.load(open(sys.argv[1]))
print({k:round((v['score'] or 0)*100) for k,v in d['categories'].items()})
a=d['audits']
for k in ['largest-contentful-paint','cumulative-layout-shift','total-blocking-time','first-contentful-paint','speed-index','total-byte-weight']:
    print(' ',k, a[k].get('displayValue'))
for cat in d['categories'].values():
    for r in cat['auditRefs']:
        au=a[r['id']]
        if au['score'] is not None and au['score']<0.9 and r.get('weight',0)>0:
            print('  FAIL',cat['id'],r['id'],au['score'],au.get('displayValue',''))
            for it in (au.get('details',{}) or {}).get('items',[])[:4]:
                n=it.get('node',{}); print('     ', (n.get('snippet') or it.get('url') or str(it))[:160])
