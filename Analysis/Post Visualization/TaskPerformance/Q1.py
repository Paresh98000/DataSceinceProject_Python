#Q1

import pandas as p
import pandasql as s
import pylab as g

task_d = p.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","TaskPerformance")

for x in task_d.columns:
    g.figure(figsize=(13,8))
    g.title("Histogram of "+x)
    a,b,c = g.hist(task_d[x], histtype='bar', rwidth=0.9)
    cnt=0
    while cnt<len(a):
        g.text(b.item(cnt)+0.40,a.item(cnt),str(round(b.item(cnt),2))+" - "+str(int(a.item(cnt))),fontweight="bold",size="small")
        cnt+=1
    g.savefig("fig-"+x+".png",figsize=(13,8))
    g.close()
